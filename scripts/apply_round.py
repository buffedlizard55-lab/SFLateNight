#!/usr/bin/env python3
"""Reusable round-merge: apply a JSONL of new venue records to the dataset.

Usage: python3 scripts/apply_round.py <records.jsonl> [--date YYYY-MM-DD]

- Merges records (schema = one entry of data/venues.json "venues").
- Bumps meta.recordCount + scopeNote count, sets meta.verifiedOn.
- Patches the hardcoded expected count in scripts/validate_data.py.
- Rewrites the count strings in index.html and README.md (130 -> N).
- Refuses to run if there are id/address collisions or unknown lineIds.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "venues.json"
VALIDATOR = ROOT / "scripts" / "validate_data.py"
INDEX = ROOT / "index.html"
README = ROOT / "README.md"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("records")
    ap.add_argument("--date", default=None, help="verification date (defaults to current meta.verifiedOn)")
    args = ap.parse_args()

    new = [json.loads(l) for l in Path(args.records).read_text().splitlines() if l.strip()]
    if not new:
        raise SystemExit("no records in input")

    data = json.loads(DATA_PATH.read_text())
    venues, meta = data["venues"], data["meta"]
    before = len(venues)

    old_ids, old_addr = {v["id"] for v in venues}, {v["address"] for v in venues}
    line_ids = {l["id"] for l in meta["transit"]["lines"]}
    seen_ids, seen_addr = set(), set()
    for v in new:
        if v["id"] in old_ids or v["id"] in seen_ids:
            raise SystemExit(f"id collision: {v['id']}")
        seen_ids.add(v["id"])
        if v["address"] in old_addr or v["address"] in seen_addr:
            raise SystemExit(f"address collision: {v['address']}")
        seen_addr.add(v["address"])
        unknown = set(v["access"]["lineIds"]) - line_ids
        if unknown:
            raise SystemExit(f"{v['name']} unknown lineIds: {unknown}")

    venues.extend(new)
    after = len(venues)
    meta["verifiedOn"] = args.date or meta["verifiedOn"]
    meta["recordCount"] = after
    meta["scopeNote"] = (
        f"Static, source-linked directory of {after} verified records. It does not claim "
        "every San Francisco business is open or available; expand the master list only "
        "after a line-by-line source check."
    )
    DATA_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")

    # Validator: replace the hardcoded expected count.
    vt = VALIDATOR.read_text()
    vt2, n = re.subn(r"if len\(venues\) != \d+:", f"if len(venues) != {after}:", vt)
    vt2, _ = re.subn(r"expected exactly \d+ records", f"expected exactly {after} records", vt2)
    if n != 1:
        raise SystemExit("validator count pattern not found")
    VALIDATOR.write_text(vt2)

    # index.html count strings.
    it = INDEX.read_text()
    it = it.replace(f"directory of {before} San Francisco", f"directory of {after} San Francisco")
    it = it.replace(f"A source-checked {before}-record master list", f"A source-checked {after}-record master list")
    it = it.replace(f"<p>{before} places within the city", f"<p>{after} places within the city")
    it = it.replace(f'<strong id="hero-total">{before}</strong>', f'<strong id="hero-total">{after}</strong>')
    it = it.replace(f'>{before} places</span>', f'>{after} places</span>')
    it = it.replace(f"The current master list contains {before} records grouped", f"The current master list contains {after} records grouped")
    if str(before) in it and f"{after} records" not in it:
        for m in re.finditer(rf".*{before}.*", it, re.M):
            print("WARN leftover:", m.group(0)[:120])
    INDEX.write_text(it)

    # README count lines.
    rt = README.read_text()
    rt = rt.replace(f"- {before} San Francisco venue records", f"- {after} San Francisco venue records")
    rt = re.sub(
        r"The current master list is exactly \d+ verified records[^\.;]*;",
        f"The current master list is exactly {after} verified records;",
        rt,
    )
    rt = re.sub(
        r"The guardrail checks that there are exactly \d+ records,",
        f"The guardrail checks that there are exactly {after} records,",
        rt,
    )
    README.write_text(rt)

    print(f"merged {before} -> {after} (+{after - before})")


if __name__ == "__main__":
    main()
