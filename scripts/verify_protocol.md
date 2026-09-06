# Fast verification protocol (no-hallucination floor preserved)

Goal: cut per-candidate cost to **1-2 tool calls** without weakening the rule
that every included record must trace to the venue's own domain.

## Per-candidate loop (target 1-2 calls)

1. **One search, tuned query** (depth 2):
   `"<venue name>" <street address if known> San Francisco hours 2026`
   Extract from snippets ONLY:
   - the venue's official domain (look for "Business website" / sameAs / the
     venue's own TLD in the results; a claimed listing naming its website
     counts as a lead, not evidence),
   - claimed hours (venue-entered listing hours = the venue's own data; they
     justify `verified-with-gap`, never bare `verified`),
   - address + ZIP (cross-check, never trust a single old aggregator).
   A domain that now serves unrelated content = **dead domain → exclude**,
   record the reason; do not fetch it further.

2. **One fetch of the official domain** (chunkIndex 0 only; chunk 1 only if
   hours are not in chunk 0):
   - static text contains the hours → status `verified`, quote from the page.
   - site live, hours not machine-readable (widget/images/JS) →
     `verified-with-gap`, quote = page facts + claimed hours, flag the gap.
   - fetch blocked (HTTP 500/bot wall) but a snippet already carries verbatim
     text FROM the official domain (indexed this year) → `verified-with-gap`,
     quote the snippet, flag "direct fetch blocked at check time".
   - domain dead / unrelated content / 404 → **exclude** with reason.
   - no official domain anywhere → **exclude: no official site**.

3. **Never**:
   - cite yelp.com/tripadvisor.com/wanderlog.com/restaurantji.com/google.com
     or mirror domains (wheree/dimhour/checkle/thevendry) as `source.url`;
     they are leads only.
   - include a candidate whose qualifying-day close cannot be traced to the
     venue's own domain or its claimed listing.
   - re-check anything already in `candidates.jsonl` with status
     `excluded`/`verified` — the file is the source of truth.

## Batching rules

- 4 searches per turn (independent), then 2-4 fetches per turn.
- Try `https://www.x.com/` and `https://x.com/` in the same batch when the
  first failed — one of the two usually hits.
- Keep the exact source line verbatim in the record's `quote` field; paraphrase
  only in `method`/`flags`.

## Merge (one command)

Write passing records as JSONL (same schema as `data/venues.json` venues) and
run: `python3 scripts/apply_round.py scripts/roundN.jsonl`
It merges, bumps `meta.recordCount`, patches the validator's expected count,
and rewrites the 6 count strings in `index.html` + the README count lines.
Then: `python3 scripts/validate_data.py`, append the round section to
`VERIFICATION.md`, commit + push the arena branch.
