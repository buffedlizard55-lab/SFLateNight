# SF Late Night

A clean, source-first GitHub Pages directory for late-night restaurants, bars, and places to hang out in San Francisco, starting from **21st Ave & Judah St, San Francisco, CA 94122**.

## What is included

- 20 new San Francisco venue records.
- Official venue links for manual review.
- Officially published address and weekly hours transcribed into a searchable table.
- Inclusion only when the published venue schedule ends after 11:00 PM on at least one Friday, Saturday, or Sunday. Midnight counts as later than 11 PM.
- Conservative public-transit and walking notes, plus a live transit route link from the requested starting point.
- A visible review queue for kitchen cutoffs, grouped hours, missing opening times, 21+ rules, and other operational details.
- A verification log in [`VERIFICATION.md`](VERIFICATION.md).

This is intentionally a **static, source-linked index**, not a fake live-search service. The site never invents hours or implies that a venue is open right now. Hours can change, so the official source and day-of route check are part of the product.

## Run locally

Any static server works. For example:

```bash
python3 -m http.server 8000
```

Then open <http://localhost:8000>.

## Validate the data

```bash
python3 scripts/validate_data.py
```

The guardrail checks that there are exactly 20 records, every record has a seven-day schedule, each official source is HTTPS and not a review directory, qualifying days have a late close, and every row carries an explicit operational note.

## GitHub Pages

The repository includes [`.github/workflows/pages.yml`](.github/workflows/pages.yml). After GitHub Pages is configured to use **GitHub Actions**, merging this branch into the repository's `main` branch deploys the static site automatically. The current repository environment only permits Pages deployments from `main`; the source branch is intentionally not used to bypass that protection.

## Source policy

1. Prefer the venue's own current website or official location/contact page.
2. Transcribe the source wording rather than filling gaps from memory or review sites.
3. Keep bar, kitchen, event, and private-event hours separate when the venue distinguishes them.
4. Never substitute a different branch for a verified address.
5. Flag conflicts or missing details instead of guessing.
6. Re-check the source and live transit service before a specific visit.

**Snapshot checked:** September 5, 2026 (UTC).
