# SF Late Night

A clean, source-first GitHub Pages directory for late-night restaurants, bars, and places to hang out in San Francisco, starting from **21st Ave & Judah St, San Francisco, CA 94122**.

## What is included

- 96 San Francisco venue records (20 launch records, 50 added in the second verification pass, and 26 more merged from a parallel verification pass).
- Official venue links for manual review.
- Officially published address and weekly hours transcribed into a searchable table.
- Inclusion only when the published venue schedule ends after 11:00 PM on at least one Friday, Saturday, or Sunday. Midnight counts as later than 11 PM.
- Neighborhood clusters for Mission, Castro / Upper Market, North Beach, SoMa, Downtown / Union Square, Polk Gulch, Lower Nob Hill, Market / Duboce, and Divisadero / NoPa.
- Conservative public-transit and walking notes, official Muni route mappings, Saturday service windows, and a live transit route link from the requested starting point.
- A visible review queue for kitchen cutoffs, grouped hours, missing opening times, 21+ rules, transit gaps, and other operational details.
- Venue verification in [`VERIFICATION.md`](VERIFICATION.md) and transit verification in [`TRANSIT_VERIFICATION.md`](TRANSIT_VERIFICATION.md).

This is intentionally a **static, source-linked index**, not a fake live-search service or a claim that every San Francisco business is represented. The current master list is exactly 96 verified records; the site never invents hours or implies that a venue is open right now. Hours and transit service can change, so the official source, SFMTA alerts, and day-of route check are part of the product.

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

The guardrail checks that there are exactly 96 records, every record has a seven-day schedule, each official source is HTTPS and not a review directory, qualifying days have a late close, every row carries a neighborhood and mapped transit line, and every transit line has an official Saturday service window and source quote.

## GitHub Pages

The repository includes [`.github/workflows/pages.yml`](.github/workflows/pages.yml). After GitHub Pages is configured to use **GitHub Actions**, merging this branch into the repository's `main` branch deploys the static site automatically. The current repository environment only permits Pages deployments from `main`; the source branch is intentionally not used to bypass that protection.

## Source policy

1. Prefer the venue's own current website or official location/contact page.
2. Transcribe the source wording rather than filling gaps from memory or review sites.
3. Keep bar, kitchen, event, and private-event hours separate when the venue distinguishes them.
4. Never substitute a different branch for a verified address.
5. Flag conflicts or missing details instead of guessing.
6. Re-check the source, SFMTA alerts, and live transit service before a specific visit.
7. Treat route-level service windows as screening information; the first/last vehicle at a particular stop may differ.

**Venue and transit snapshot checked:** September 5, 2026 (America/Los_Angeles).
