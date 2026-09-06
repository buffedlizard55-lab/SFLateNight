# SF Late Night

A clean, source-first GitHub Pages directory for late-night restaurants, bars, and places to hang out in San Francisco, starting from **21st Ave & Judah St, San Francisco, CA 94122**.

## What is included

- 70 San Francisco venue records: the original 20 plus 50 added on September 5, 2026.
- Official venue links for manual review.
- Officially published address and weekly hours transcribed into a searchable table.
- Inclusion only when the published venue schedule ends after 11:00 PM on at least one Friday, Saturday, or Sunday. Midnight counts as later than 11 PM.
- 21 neighborhood clusters ordered roughly west to east from the origin: Inner Sunset, Inner Richmond, Upper Haight, Lower Haight, Divisadero / NoPa, Hayes Valley, Fillmore / Japantown, Marina / Cow Hollow, Russian Hill, Polk Gulch, Nob Hill, Lower Nob Hill, Downtown / Union Square, Financial District, North Beach, Fisherman’s Wharf, Market / Duboce, Castro / Upper Market, Mission, SoMa, and Potrero Hill.
- Conservative public-transit and walking notes, official Muni route mappings for 17 lines (including the N Owl, 44 O’Shaughnessy, 1 California, 7 Haight/Noriega, 6 Hayes/Parnassus, and 28 19th Avenue), Saturday service windows, and a live transit route link from the requested starting point.
- A visible review queue for kitchen cutoffs, grouped hours, missing opening times, 21+ rules, transit gaps, and other operational details.
- Venue verification in [`VERIFICATION.md`](VERIFICATION.md) and transit verification in [`TRANSIT_VERIFICATION.md`](TRANSIT_VERIFICATION.md).

This is intentionally a **static, source-linked index**, not a fake live-search service or a claim that every San Francisco business is represented. The current master list is exactly 70 verified records (62 clean official matches and 8 with a documented source gap); the site never invents hours or implies that a venue is open right now. Hours and transit service can change, so the official source, SFMTA alerts, and day-of route check are part of the product.

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

The guardrail checks that there are exactly 70 records, every record has a seven-day schedule, each official source is HTTPS and not a review directory, qualifying days have a late close, every row carries a neighborhood and mapped transit line, and every transit line has an official Saturday service window and source quote.

## GitHub Pages

The repository includes [`.github/workflows/pages.yml`](.github/workflows/pages.yml). After GitHub Pages is configured to use **GitHub Actions**, merging this branch into the repository's `main` branch deploys the static site automatically. The current repository environment only permits Pages deployments from `main`; the source branch is intentionally not used to bypass that protection.

## September 5, 2026 expansion (records 21–70)

The 50 added records follow the same rules as the first 20. A few things worth knowing when reviewing them:

- Roughly 200 candidate venues were checked; only venues whose **own** site (or the operator’s official group site) publishes an address and a closing time later than 11 PM on Friday, Saturday, or Sunday were kept. The rejected candidates and the reason for each rejection are listed at the top of the new section in [`VERIFICATION.md`](VERIFICATION.md).
- Eight records are marked **Review gap** rather than clean: Toronado (hours read from the indexed copy of the official contact page), The Page and Comstock Saloon (closing time only), Fly Bar (no Friday opening time), Brazen Head (address from the official site listing rather than page text), Bob’s Donuts (24-hour claim from structured data only), and Hole in the Wall Saloon (official domain redirects to an oddly named host).
- Several records qualify only because a **midnight** close counts as later than 11 PM (Woods Lowside, Woods Polk Station, Super Duper Fillmore, Tommy’s Joynt, Buena Vista, Hotel Utah, and the Sunday columns of several bars). Each of those rows says so in its flags.
- Transit mapping now includes the **N Owl**, which stops at Judah St & 22nd Ave one block from the origin, so every cluster has an overnight option or an explicit note that the last bus leaves around the same time the venue closes (Fisherman’s Wharf, North Beach, Nob Hill, Russian Hill).
- Lines that SFMTA lists as ending by 10 PM (12 Folsom, 19 Polk, 27 Bryant, 45 Union/Stockton, 2 Sutter) or as suspended (47 Van Ness) are never used for a late return leg; see [`TRANSIT_VERIFICATION.md`](TRANSIT_VERIFICATION.md).

## Source policy

1. Prefer the venue's own current website or official location/contact page.
2. Transcribe the source wording rather than filling gaps from memory or review sites.
3. Keep bar, kitchen, event, and private-event hours separate when the venue distinguishes them.
4. Never substitute a different branch for a verified address.
5. Flag conflicts or missing details instead of guessing.
6. Re-check the source, SFMTA alerts, and live transit service before a specific visit.
7. Treat route-level service windows as screening information; the first/last vehicle at a particular stop may differ.

**Venue and transit snapshot checked:** September 5, 2026 (America/Los_Angeles).
