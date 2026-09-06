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
    # Parse the last clock time in the string and apply the directory rule:
    # a close is "late" if it is after 11 PM (i.e. 12 AM through 4 AM, which
    # represent a next-day close, or any 11:xx PM close that is after 11 PM).
    found = False
    for m in re.finditer(r"(\d{1,2}):(\d{2})\s*(am|pm)", text):
        hour, minute, meridiem = int(m.group(1)), int(m.group(2)), m.group(3)
        if meridiem == "pm" and hour != 12:
            hour24 = hour + 12
        elif meridiem == "am" and hour == 12:
            hour24 = 0
        else:
            hour24 = hour
        total = hour24 * 60 + minute
        # after 11 PM (1380 minutes) — 11:00 PM exactly does not count, but 11:01 PM+
        # and 12 AM–4 AM do. Midnight (12:00 AM) counts as later than 11 PM.
        if total > 1380 or hour24 == 0 or (1 <= hour24 <= 4):
            return True
        found = True
    return False


def validate_transit(meta: dict, venues: list[dict]) -> None:
    transit = meta.get("transit")
    if not isinstance(transit, dict):
        fail("meta.transit is missing")
    snapshot_date = transit.get("snapshotDate")
    if not snapshot_date or snapshot_date != meta.get("verifiedOn"):
        fail("transit snapshotDate must match the dataset verifiedOn date")
    if transit.get("snapshotDay") not in {"Friday", "Saturday", "Sunday"}:
        fail("transit snapshotDay must be Friday, Saturday, or Sunday")
    if not transit.get("timezone") or not transit.get("originNote"):
        fail("transit timezone and originNote are required")
    for field in ("plannerUrl", "routeDirectoryUrl", "alertsUrl"):
        if not officialish(transit.get(field, "")):
            fail(f"transit {field} must be an official HTTPS source")

    lines = transit.get("lines")
    if not isinstance(lines, list) or not lines:
        fail("meta.transit.lines must be a non-empty list")
    line_ids: set[str] = set()
    for line in lines:
        line_id = line.get("id", "<unnamed>")
        if line_id in line_ids:
            fail(f"duplicate transit line id {line_id}")
        line_ids.add(line_id)
        for field in ("name", "mode", "todayWindow", "todayFrequency", "nightCoverage", "sourceQuote"):
            if not line.get(field):
                fail(f"transit line {line_id} is missing {field}")
        for field in ("routeUrl", "scheduleUrl"):
            if not officialish(line.get(field, "")):
                fail(f"transit line {line_id} has a non-official {field}")
        if line.get("checkedOn") != snapshot_date:
            fail(f"transit line {line_id} is not checked on the snapshot date")

    for venue in venues:
        name = venue.get("name", "<unnamed>")
        if not venue.get("neighborhoodGroup"):
            fail(f"neighborhoodGroup is missing for {name}")
        line_ids_for_venue = venue.get("access", {}).get("lineIds")
        if not isinstance(line_ids_for_venue, list) or not line_ids_for_venue:
            fail(f"transit line mapping is missing for {name}")
        unknown = set(line_ids_for_venue) - line_ids
        if unknown:
            fail(f"{name} references unknown transit line(s): {', '.join(sorted(unknown))}")


def main() -> None:
    try:
        data = json.loads(DATA_PATH.read_text())
    except Exception as exc:  # pragma: no cover - guardrail output
        fail(f"could not parse {DATA_PATH}: {exc}")

    venues = data.get("venues")
    if not isinstance(venues, list):
        fail("venues must be a list")
    meta = data.get("meta", {})
    if len(venues) != meta.get("recordCount"):
        fail("meta.recordCount does not match the number of venue records")
    if len(venues) != 134:
        fail(f"expected exactly 134 records, found {len(venues)}")

    validate_transit(meta, venues)

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

    print(f"OK: {len(venues)} records, seven-day schedules, official HTTPS sources, late-night evidence, neighborhood clusters, and transit snapshots all present.")
    print(f"Clean official matches: {sum(v['verification']['status'] == 'verified' for v in venues)}")
    print(f"Records with a documented source gap: {sum(v['verification']['status'] != 'verified' for v in venues)}")
    print(f"Transit lines with official service windows (Sunday snapshot): {len(data['meta']['transit']['lines'])}")


if __name__ == "__main__":
    main()
