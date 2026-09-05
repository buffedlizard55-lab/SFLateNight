#!/usr/bin/env python3
"""Small guardrail for the source-linked static directory."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "venues.json"
DAYS = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
LATE_DAYS = {"Friday", "Saturday", "Sunday"}
BLOCKED_DOMAINS = {"yelp.com", "tripadvisor.com", "restaurantji.com", "wanderlog.com", "google.com"}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def officialish(url: str) -> bool:
    parsed = urlparse(url)
    host = parsed.netloc.lower().removeprefix("www.")
    return parsed.scheme == "https" and host and not any(host == domain or host.endswith(f".{domain}") for domain in BLOCKED_DOMAINS)


def has_late_close(value: str) -> bool:
    text = value.lower()
    if "24 hour" in text:
        return True
    # This directory uses 12 AM / 1 AM / 2 AM / 3 AM to represent a next-day close.
    return bool(re.search(r"(?:until\s+)?(?:12|1|2|3)(?::\d{2})?\s*am", text))


def main() -> None:
    try:
        data = json.loads(DATA_PATH.read_text())
    except Exception as exc:  # pragma: no cover - guardrail output
        fail(f"could not parse {DATA_PATH}: {exc}")

    venues = data.get("venues")
    if not isinstance(venues, list):
        fail("venues must be a list")
    if len(venues) != data.get("meta", {}).get("recordCount"):
        fail("meta.recordCount does not match the number of venue records")
    if len(venues) != 20:
        fail(f"expected exactly 20 new records, found {len(venues)}")

    ids = set()
    addresses = set()
    for venue in venues:
        name = venue.get("name", "<unnamed>")
        if not venue.get("id") or venue["id"] in ids:
            fail(f"duplicate or missing id for {name}")
        ids.add(venue["id"])
        if not venue.get("address") or "San Francisco" not in venue["address"]:
            fail(f"missing San Francisco address for {name}")
        if venue["address"] in addresses:
            fail(f"duplicate address for {name}")
        addresses.add(venue["address"])
        if not venue.get("officialUrl") or not officialish(venue["officialUrl"]):
            fail(f"officialUrl is missing or not an official HTTPS venue domain for {name}")
        source = venue.get("source", {})
        if not source.get("url") or not officialish(source["url"]):
            fail(f"source URL is missing or not an official HTTPS venue domain for {name}")
        if not source.get("quote"):
            fail(f"source quote is empty for {name}")
        hours = venue.get("hours", {})
        if set(hours) != DAYS:
            fail(f"hours must contain all seven days for {name}")
        qualifying = set(venue.get("qualifyingDays", []))
        if not qualifying or not qualifying <= LATE_DAYS:
            fail(f"qualifyingDays must be a non-empty subset of Fri/Sat/Sun for {name}")
        for day in qualifying:
            if not has_late_close(hours[day]):
                fail(f"{name}: {day} is marked late but the published hour text has no late close: {hours[day]}")
        if not venue.get("flags"):
            fail(f"irregularities/operational notes are missing for {name}; flag uncertainty explicitly")
        if venue.get("verification", {}).get("status") not in {"verified", "verified-with-gap"}:
            fail(f"unexpected verification status for {name}")

    print(f"OK: {len(venues)} records, seven-day schedules, official HTTPS sources, and late-night evidence all present.")
    print(f"Clean official matches: {sum(v['verification']['status'] == 'verified' for v in venues)}")
    print(f"Records with a documented source gap: {sum(v['verification']['status'] != 'verified' for v in venues)}")


if __name__ == "__main__":
    main()
