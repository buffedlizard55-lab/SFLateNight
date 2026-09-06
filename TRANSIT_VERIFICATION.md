# Transit verification log

This file records the official SFMTA route pages used for the transit service snapshot in [`data/venues.json`](data/venues.json).

- **Current snapshot (live in the site data):** Sunday **September 6, 2026**, re-verified line-by-line from official SFMTA route pages on 2026-09-06. See the [Sunday service snapshot](#sunday-service-snapshot--2026-09-06-round-3-re-verification) section below.
- **Retained history:** the original Saturday **September 5, 2026** snapshot is kept below (its `service_id=2` schedule links no longer match `data/venues.json`, which now points at `service_id=3` Sunday service).

## Important limits

- These are **published route service windows and scheduled frequency summaries**, not live vehicle positions or a guarantee that a particular trip will run.
- Service windows are route-level summaries. The first and last vehicle at a specific stop can differ by direction, branch, short turn, and transfer.
- SFMTA alerts, temporary stop relocations, events, and service changes can override the regular schedule. Check the [SFMTA Muni alerts page](https://www.sfmta.com/getting-around/muni/muni-alerts) and the [official route page](https://www.sfmta.com/routes) before leaving.
- The site uses the official [511 Bay Area trip planner](https://511.org/) / live route link for the final transfer and walking plan from **21st Ave & Judah St, San Francisco, CA 94122**.

## Origin check

The closest practical rail boarding point for the requested origin is the N Judah corridor around **Judah St & 19th Ave**. The origin is not itself a transit stop, so a short walk and a live planner are required before any route claim is treated as final.

## Saturday service snapshot

### N Judah

- **Official route page:** [SFMTA N Judah](https://www.sfmta.com/routes/n-judah)
- **Saturday schedule page:** [N Bus Saturday schedule](https://www.sfmta.com/routes/schedule/NBUS?direction_id=0&service_id=2&date=20260905)
- **Published line:** “24 hours daily.”
- **Saturday frequency used in the site:** 12 minutes in morning, midday, and evening; 20 minutes late night; Owl 30 minutes.
- **Coverage note:** SFMTA says to use the N Bus between subway hours and Owl service.

### 5 Fulton

- **Official route page:** [SFMTA 5 Fulton](https://www.sfmta.com/routes/5-fulton)
- **Saturday schedule page:** [5 Fulton Saturday schedule](https://www.sfmta.com/routes/schedule/5?direction_id=0&service_id=2&date=20260905)
- **Published line:** “24 hours daily.”
- **Saturday frequency used in the site:** 7 minutes in morning and midday; 12 minutes evening; 20 minutes late night; Owl 30 minutes.
- **Coverage note:** SFMTA describes weekend 5 AM–midnight Ocean Beach–Downtown service and 5 Owl from midnight–5 AM. The 5R branch is separately noted by SFMTA for some weekday daytime segments.

### 14 Mission

- **Official route page:** [SFMTA 14 Mission](https://www.sfmta.com/routes/14-mission)
- **Saturday schedule page:** [14 Mission Saturday schedule](https://www.sfmta.com/routes/schedule/14?direction_id=1&service_id=2&date=20260905)
- **Published line:** “24 hours daily.”
- **Saturday frequency used in the site:** 8 minutes in morning and midday; 10 minutes evening; 15 minutes late night and Owl.
- **Coverage note:** The route page lists Owl service on the 14 schedule; the late-night path and stop spacing still need a live check.

### 22 Fillmore

- **Official route page:** [SFMTA 22 Fillmore](https://www.sfmta.com/routes/22-fillmore)
- **Saturday schedule page:** [22 Fillmore Saturday schedule](https://www.sfmta.com/routes/schedule/22?direction_id=0&service_id=2&date=20260905)
- **Published line:** “24 hours daily.”
- **Saturday frequency used in the site:** 10 minutes morning; 8 minutes midday and evening; 15 minutes late night; Owl 30 minutes.
- **Coverage note:** The official page lists the Mission, Castro / Upper Market, Marina, and SoMa neighborhoods and a live map; a specific venue trip still needs a stop-level check.

### 24 Divisadero

- **Official route page:** [SFMTA 24 Divisadero](https://www.sfmta.com/routes/24-divisadero)
- **Saturday schedule page:** [24 Divisadero Saturday schedule](https://www.sfmta.com/routes/schedule/24?direction_id=0&service_id=2&date=20260905)
- **Published line:** “24 hours daily.”
- **Saturday frequency used in the site:** 12 minutes in morning, midday, and evening; 20 minutes late night; Owl 30 minutes.
- **Coverage note:** The official stop list includes Castro St & 18th St and Divisadero St & McAllister St, which are used as conservative screening points for the Castro and Divisadero clusters.

### 30 Stockton

- **Official route page:** [SFMTA 30 Stockton](https://www.sfmta.com/routes/30-stockton)
- **Saturday schedule page:** [30 Stockton Saturday schedule](https://www.sfmta.com/routes/schedule/30?direction_id=0&service_id=2&date=20260905)
- **Published line:** “Weekdays 5 a.m. - 12 a.m.; Weekends 6 a.m. - 12 a.m.”
- **Saturday frequency used in the site:** Long route: 20 minutes morning; 15 minutes midday and evening; 20 minutes late night. SFMTA separately lists different short-route frequencies.
- **Coverage note:** SFMTA says the route changes at night and points riders to 91 Owl overnight. The site therefore does not treat 30 Stockton as a 24-hour return option.

### 33 Ashbury/18th Street

- **Official route page:** [SFMTA 33 Ashbury/18th Street](https://www.sfmta.com/routes/33-ashbury18th-street)
- **Saturday schedule page:** [33 Saturday schedule](https://www.sfmta.com/routes/schedule/33?direction_id=0&service_id=2&date=20260905)
- **Published line:** “5 a.m. - 10 p.m. daily.”
- **Saturday frequency used in the site:** 30 minutes morning; 20 minutes midday and evening; no late-night or Owl service listed.
- **Coverage note:** The line is shown for the ABV access screen because its official stop list includes 18th St & Guerrero and the Mission corridor. It is explicitly **not** a late-night return recommendation after 10 PM.

### 38 Geary

- **Official route page:** [SFMTA 38 Geary](https://www.sfmta.com/routes/38-geary)
- **Saturday schedule page:** [38 Geary Saturday schedule](https://www.sfmta.com/routes/schedule/38?direction_id=1&service_id=2&date=20260905)
- **Published line:** “24 hours daily.”
- **Saturday frequency used in the site:** The official page varies by segment: west of Geary & 32nd Ave is 20 minutes morning, midday, evening, and late night; east of that point is 15 minutes morning, 10 minutes midday and evening, and 15 minutes late night; Owl is 30 minutes.
- **Coverage note:** Direction, segment, and stop matter. The site uses 38 for the Powell, Polk, and downtown screening areas but does not promise a specific stop arrival.

### 49 Van Ness/Mission

- **Official route page:** [SFMTA 49 Van Ness/Mission](https://www.sfmta.com/routes/49-van-nessmission)
- **Saturday schedule page:** [49 Saturday schedule](https://www.sfmta.com/routes/schedule/49?direction_id=0&service_id=2&date=20260905)
- **Published line:** “5 a.m. - 12 a.m. daily.”
- **Saturday frequency used in the site:** 8 minutes morning, midday, and evening; 13 minutes late night.
- **Coverage note:** The official page points riders to 14 Mission and 90 Owl for overnight service. The site does not claim that 49 itself runs after midnight.

### T Third Street

- **Official route page:** [SFMTA T Third Street](https://www.sfmta.com/routes/t-third-street)
- **Saturday schedule page:** [T Saturday schedule](https://www.sfmta.com/routes/schedule/T?direction_id=0&service_id=2&date=20260905)
- **Published line:** “Weekdays 6 a.m. - 12 a.m.; Weekends 8 a.m. - 12 a.m.”
- **Saturday frequency used in the site:** 12 minutes morning, midday, and evening; 20 minutes late night; 91 Owl 30 minutes.
- **Coverage note:** SFMTA lists the T Bus for early mornings before the subway opens and 91 Owl for overnight coverage. The site uses T for the 3rd Street access screen and shows 91 separately.

### 91 3rd Street/19th Avenue Owl

- **Official route page:** [SFMTA 91 3rd Street/19th Avenue Owl](https://www.sfmta.com/routes/91-3rd-street19th-avenue-owl)
- **Saturday schedule page:** [91 Saturday schedule](https://www.sfmta.com/routes/schedule/91?direction_id=0&service_id=2&date=20260905)
- **Published line:** “12 a.m. - 5 a.m. nightly.”
- **Saturday frequency used in the site:** 30 minutes late night / Owl.
- **Coverage note:** The 91 page is the official overnight route linked from the T and 30 pages. Its actual path and stop direction should be checked against the destination and return leg.

### 7 Haight/Noriega (added in the second pass)

- **Official route page:** [SFMTA 7 Haight/Noriega](https://www.sfmta.com/routes/7-haightnoriega)
- **Saturday schedule page:** [7 Saturday schedule](https://www.sfmta.com/routes/schedule/7?direction_id=0&service_id=2&date=20260905)
- **Published line:** Selected-stop Saturday table shows outbound trips roughly every 12-20 minutes from 5:00 AM, with the final departure at 12:00 AM (Market & Van Ness 12:14 AM; Haight & Masonic 12:24 AM; Lincoln Way & 19th Ave 12:34 AM; Ortega & 48th 12:47 AM).
- **Saturday frequency used in the site:** every 12-20 minutes.
- **Coverage note:** Used for the Haight Street cluster (Toronado). The last midnight trip passes within a few blocks of the origin area (Lincoln Way & 19th Ave); nothing later appears on this schedule page.

### 12 Folsom/Pacific (added in the second pass)

- **Official route page:** [SFMTA 12 Folsom/Pacific](https://www.sfmta.com/routes/12-folsompacific)
- **Saturday schedule page:** [12 Saturday schedule](https://www.sfmta.com/routes/schedule/12?direction_id=0&service_id=2&date=20260905)
- **Published line:** Selected-stop Saturday table shows outbound service roughly every 10-20 minutes from 6:00 AM with the final trip at 10:00 PM (Pacific Ave & Powell St 10:12 PM; Folsom St & 11th St 10:33 PM; Folsom St & 24th St 10:40 PM).
- **Saturday frequency used in the site:** every 10-20 minutes.
- **Coverage note:** Used for Jackson Square/Chinatown edge, the Kearny Street corridor, and the Folsom & 11th Street club cluster. It ends at 10:00 PM — late-night SoMa returns must use another line.

### 19 Polk (added in the second pass)

- **Official route page:** [SFMTA 19 Polk](https://www.sfmta.com/routes/19-polk)
- **Saturday schedule page:** [19 Saturday schedule](https://www.sfmta.com/routes/schedule/19?direction_id=0&service_id=2&date=20260905)
- **Published line:** Selected-stop Saturday table shows outbound trips roughly every 20 minutes from 5:05 AM with the final trip at 10:00 PM (Polk & Sacramento 10:08 PM; Polk & Sutter 10:11 PM; 8th & Mission 10:21 PM).
- **Saturday frequency used in the site:** every 20 minutes.
- **Coverage note:** Used for the Polk Street record (Bob's Donuts) and as a secondary walk option for Geary/Turk Street Tenderloin records. Ends at 10:00 PM outbound.

### 43 Masonic (added in the second pass)

- **Official route page:** [SFMTA 43 Masonic](https://www.sfmta.com/routes/43-masonic)
- **Saturday schedule page:** [43 Saturday schedule](https://www.sfmta.com/routes/schedule/43?direction_id=0&service_id=2&date=20260905)
- **Published line:** Selected-stop Saturday table shows outbound trips roughly every 20 minutes from 5:00 AM with the final trip at 11:50 PM (Presidio Ave & California St 12:13 AM; Masonic Ave & Haight St 12:22 AM; 9th Ave & Judah St 12:27 AM; Munich St & Geneva 12:50 AM).
- **Saturday frequency used in the site:** every 20 minutes.
- **Coverage note:** Used for the Presidio (Presidio Bowl) and as a secondary line for Haight/Inner Sunset records; its 9th Ave & Judah stop is close to the origin area's N Judah corridor.

### Lines checked but not added (second pass)

- **41 Union:** SFMTA's schedule page returns "Content Not Found" as of this snapshot, so the Columbus Avenue corridor is served in this directory by the 30 Stockton and 12 Folsom/Pacific instead. No 41-based access text is used.
- **2 Sutter:** the current 2 runs Steuart St to The Richmond via Sutter Street and Presidio Ave & California St. It was verified but not used by any record; Clement and Geary records use the 38 Geary corridor with a short walk.

## Re-check policy

The venue hours and this transit snapshot are separate claims. A venue can remain open while a regular line is disrupted, short-turned, or replaced. Before a specific Friday, Saturday, or Sunday trip, open the official venue source, the official SFMTA route page, the [Muni alerts page](https://www.sfmta.com/getting-around/muni/muni-alerts), and the live planner.

---

## September 5, 2026 expansion pass — additional lines

Each line below was read from its official SFMTA route page on 2026-09-05 (a Saturday). Frequencies quoted are the weekend rows.

### 1 California (added by the parallel pass)

- **Official route page:** [1 California](https://www.sfmta.com/routes/1-california)
- **Saturday schedule page:** [1 Saturday schedule](https://www.sfmta.com/routes/schedule/1?direction_id=0&service_id=2&date=20260905)
- **Published line:** “SFMTA lists 1 California as "5 a.m. - 12 a.m. daily". Its weekend rows list 10 minutes morning, midday, and evening and 15 minutes late night, with no Owl service.”
- **Today's window:** 5:00 AM–12:00 AM daily
- **Saturday frequency used in the site:** Saturday: 10 min morning, midday, and evening west and east of Presidio Ave; 15 min late night. No Owl listed.
- **Coverage note:** No Owl service is listed on the route page; use the 38 Geary or 90 Owl after midnight.

### 6 Hayes/Parnassus (added by the parallel pass)

- **Official route page:** [6 Hayes/Parnassus](https://www.sfmta.com/routes/6-hayesparnassus)
- **Saturday schedule page:** [6 Saturday schedule](https://www.sfmta.com/routes/schedule/6?direction_id=0&service_id=2&date=20260905)
- **Published line:** “SFMTA lists 6 Hayes/Parnassus as "Weekdays 5 a.m. - 12 a.m.; Weekends 5 a.m. - 12 a.m." Its weekend row lists 20 minutes across morning, midday, evening, and late night with no Owl.”
- **Today's window:** 5:00 AM–12:00 AM daily
- **Saturday frequency used in the site:** Saturday: 20 min morning, midday, evening, and late night. No Owl listed.
- **Coverage note:** No Owl service is listed; SFMTA shows service ending at midnight on weekends.



## Sunday service snapshot — 2026-09-06 (Round 3 re-verification)

All 20 lines below were re-checked on **Sunday, September 6, 2026** (America/Los_Angeles) from the official SFMTA route page for each line. Service discovery notes:

- The SFMTA schedule pages' service switcher shows **service_id=3 = Sunday Service**, service_id=2 = Saturday, M11 = school day; the `date=` parameter does not auto-select the service, so the schedule links in `data/venues.json` now use `service_id=3&date=20260906`.
- The schedule page lists **Labor Day 2026-09-07 under the same Sunday service ID**, so tomorrow's service matches today's snapshot.
- The schedule tables paginate client-side (only the first column is in the static HTML), so first/last trips at a specific stop still require the live planner; the route-page service window and frequency rows (used here) are fully static.

### N Judah

- **Official route page:** [SFMTA N Judah](https://www.sfmta.com/routes/n-judah)
- **Sunday schedule page:** [N Bus Sunday schedule](https://www.sfmta.com/routes/schedule/NBUS?direction_id=0&service_id=3&date=20260906)
- **Published line:** "24 hours daily."
- **Sunday frequency used in the site:** 12 minutes in morning, midday, and evening; 20 minutes late night; Owl 30 minutes.
- **Coverage note:** SFMTA says to use the N Bus between subway hours and Owl service.

### 5 Fulton

- **Official route page:** [SFMTA 5 Fulton](https://www.sfmta.com/routes/5-fulton)
- **Sunday schedule page:** [5 Fulton Sunday schedule](https://www.sfmta.com/routes/schedule/5?direction_id=0&service_id=3&date=20260906)
- **Published line:** "24 hours daily."
- **Sunday frequency used in the site:** 7 minutes in morning and midday; 12 minutes in the evening; 20 minutes late night; Owl 30 minutes (Ocean Beach to 4th & Market).
- **Coverage note:** The 5R Fulton Rapid supplement applies only on weekdays 7 a.m.–7 p.m., so it does not affect Sunday.

### 14 Mission

- **Official route page:** [SFMTA 14 Mission](https://www.sfmta.com/routes/14-mission)
- **Sunday schedule page:** [14 Mission Sunday schedule](https://www.sfmta.com/routes/schedule/14?direction_id=0&service_id=3&date=20260906)
- **Published line:** "24 hours daily."
- **Sunday frequency used in the site:** 8 minutes in morning and midday; 10 minutes in the evening; 15 minutes late night and Owl.
- **Coverage note:** Runs 24 hours on Sunday with 15-minute late-night and Owl service.

### 22 Fillmore

- **Official route page:** [SFMTA 22 Fillmore](https://www.sfmta.com/routes/22-fillmore)
- **Sunday schedule page:** [22 Fillmore Sunday schedule](https://www.sfmta.com/routes/schedule/22?direction_id=0&service_id=3&date=20260906)
- **Published line:** "24 hours daily."
- **Sunday frequency used in the site:** 10 minutes morning; 8 minutes midday and evening; 15 minutes late night; Owl 30 minutes.
- **Coverage note:** The route page lists Muni service changes effective Saturday, August 29, 2026 — check the alerts page before riding.

### 24 Divisadero

- **Official route page:** [SFMTA 24 Divisadero](https://www.sfmta.com/routes/24-divisadero)
- **Sunday schedule page:** [24 Divisadero Sunday schedule](https://www.sfmta.com/routes/schedule/24?direction_id=0&service_id=3&date=20260906)
- **Published line:** "24 hours daily."
- **Sunday frequency used in the site:** 12 minutes in morning, midday, and evening; 20 minutes late night; Owl 30 minutes.
- **Coverage note:** Runs 24 hours; Owl every 30 minutes after regular late-night service.

### 30 Stockton

- **Official route page:** [SFMTA 30 Stockton](https://www.sfmta.com/routes/30-stockton)
- **Sunday schedule page:** [30 Stockton Sunday schedule](https://www.sfmta.com/routes/schedule/30?direction_id=0&service_id=3&date=20260906)
- **Published line:** "Weekdays 5 a.m. - 12 a.m.; Weekends 6 a.m. - 12 a.m." — i.e., **6 a.m. to 12 a.m. on Sunday**.
- **Sunday frequency used in the site:** long route 20 min morning, 15 min midday and evening, 20 min late night; short route 12 min morning, 8 min midday and evening, 20 min late night; Owl: see 91 Owl.
- **Coverage note:** After 8 p.m. the 30 terminates at Divisadero & Chestnut; late-night riders transfer to the 91 Owl or other 24-hour lines.

### 33 Ashbury/18th Street

- **Official route page:** [SFMTA 33 Ashbury/18th Street](https://www.sfmta.com/routes/33-ashbury18th-street)
- **Sunday schedule page:** [33 Sunday schedule](https://www.sfmta.com/routes/schedule/33?direction_id=0&service_id=3&date=20260906)
- **Published line:** "5 a.m. - 10 p.m. daily."
- **Sunday frequency used in the site:** 30 minutes in the morning; 20 minutes in midday and evening; no late-night or Owl service.
- **Coverage note:** Sunday service ends around 10 p.m.; after that use 38 Geary or other 24-hour lines.

### 38 Geary

- **Official route page:** [SFMTA 38 Geary](https://www.sfmta.com/routes/38-geary)
- **Sunday schedule page:** [38 Geary Sunday schedule](https://www.sfmta.com/routes/schedule/38?direction_id=0&service_id=3&date=20260906)
- **Published line:** "24 hours daily."
- **Sunday frequency used in the site:** east of 32nd Ave 15 min morning, 10 min midday and evening, 15 min late night; west of 32nd Ave 20 minutes in all periods; Owl 30 minutes.
- **Coverage note:** Runs 24 hours in both directions; Owl every 30 minutes.

### 49 Van Ness/Mission

- **Official route page:** [SFMTA 49 Van Ness/Mission](https://www.sfmta.com/routes/49-van-nessmission)
- **Sunday schedule page:** [49 Sunday schedule](https://www.sfmta.com/routes/schedule/49?direction_id=0&service_id=3&date=20260906)
- **Published line:** "5 a.m. - 12 a.m. daily."
- **Sunday frequency used in the site:** 8 minutes in morning, midday, and evening; 13 minutes late night; Owl: see 14 Mission and 90 Owl.
- **Coverage note:** The 49 stops at 12 a.m. on Sunday; after that use 14 Mission or 90 Owl on the same corridors.

### T Third Street

- **Official route page:** [SFMTA T Third Street](https://www.sfmta.com/routes/t-third-street)
- **Sunday schedule page:** [T Sunday schedule](https://www.sfmta.com/routes/schedule/T?direction_id=0&service_id=3&date=20260906)
- **Published line:** "Weekdays 6 a.m. - 12 a.m.; Weekends 8 a.m. - 12 a.m." — i.e., **8 a.m. to 12 a.m. on Sunday**.
- **Sunday frequency used in the site:** 12 minutes in morning, midday, and evening; 20 minutes late night; Owl: see 91 Owl.
- **Coverage note:** SFMTA points riders to the T Bus between subway hours and Owl service; after 12 a.m. the 91 Owl covers the same corridor.

### 91 3rd Street/19th Avenue Owl

- **Official route page:** [SFMTA 91 Owl](https://www.sfmta.com/routes/91-3rd-street19th-avenue-owl)
- **Sunday schedule page:** [91 Sunday schedule](https://www.sfmta.com/routes/schedule/91?direction_id=0&service_id=3&date=20260906)
- **Published line:** "12 a.m. - 5 a.m. nightly."
- **Sunday frequency used in the site:** 30 minutes late night and Owl.
- **Coverage note:** Owl-only line; runs 12 a.m.–5 a.m. every night, including Sunday.

### 7 Haight/Noriega

- **Official route page:** [SFMTA 7 Haight/Noriega](https://www.sfmta.com/routes/7-haightnoriega)
- **Sunday schedule page:** [7 Sunday schedule](https://www.sfmta.com/routes/schedule/7?direction_id=0&service_id=3&date=20260906)
- **Published line:** "5 a.m. - 12 a.m. daily."
- **Sunday frequency used in the site:** 15 minutes in the morning; 12 minutes in midday and evening; 25 minutes late night; no Owl.
- **Coverage note:** Stops at 12 a.m. on Sunday; after that use N Judah or other 24-hour lines for the Haight.

### 12 Folsom/Pacific

- **Official route page:** [SFMTA 12 Folsom/Pacific](https://www.sfmta.com/routes/12-folsompacific)
- **Sunday schedule page:** [12 Sunday schedule](https://www.sfmta.com/routes/schedule/12?direction_id=0&service_id=3&date=20260906)
- **Published line:** "6 a.m. - 10 p.m. daily."
- **Sunday frequency used in the site:** north of Main & Folsom 20 min morning, 10 min midday and evening; south of Main & Folsom 20 minutes in all periods; no Owl.
- **Coverage note:** Stops at 10 p.m. on Sunday; after that use 14 Mission, 90/91 Owl, or T-line corridors.

### 19 Polk

- **Official route page:** [SFMTA 19 Polk](https://www.sfmta.com/routes/19-polk)
- **Sunday schedule page:** [19 Sunday schedule](https://www.sfmta.com/routes/schedule/19?direction_id=0&service_id=3&date=20260906)
- **Published line:** "5 a.m. - 10 p.m. daily."
- **Sunday frequency used in the site:** 20 minutes in morning, midday, and evening; no late-night or Owl service.
- **Coverage note:** Stops at 10 p.m. on Sunday; after that use 14 Mission, 90 Owl, or 91 Owl on nearby corridors.

### 43 Masonic

- **Official route page:** [SFMTA 43 Masonic](https://www.sfmta.com/routes/43-masonic)
- **Sunday schedule page:** [43 Sunday schedule](https://www.sfmta.com/routes/schedule/43?direction_id=0&service_id=3&date=20260906)
- **Published line:** "5 a.m. - 12 a.m. daily."
- **Sunday frequency used in the site:** 20 minutes in morning, midday, and evening; 25 minutes late night; no Owl.
- **Coverage note:** Stops at 12 a.m. on Sunday; after that use 38 Geary or other 24-hour lines for the Richmond.

### 1 California

- **Official route page:** [SFMTA 1 California](https://www.sfmta.com/routes/1-california)
- **Sunday schedule page:** [1 Sunday schedule](https://www.sfmta.com/routes/schedule/1?direction_id=0&service_id=3&date=20260906)
- **Published line:** "5 a.m. - 12 a.m. daily."
- **Sunday frequency used in the site:** 10 minutes in morning, midday, and evening; 15 minutes late night (both sides of Presidio Avenue); no Owl.
- **Coverage note:** Stops at 12 a.m. on Sunday; after that use 38 Geary or 5 Fulton in the Richmond.

### 6 Hayes/Parnassus

- **Official route page:** [SFMTA 6 Hayes/Parnassus](https://www.sfmta.com/routes/6-hayesparnassus)
- **Sunday schedule page:** [6 Sunday schedule](https://www.sfmta.com/routes/schedule/6?direction_id=0&service_id=3&date=20260906)
- **Published line:** "Weekdays 5 a.m. - 12 a.m.; Weekends 5 a.m. - 12 a.m." — i.e., **5 a.m. to 12 a.m. on Sunday**.
- **Sunday frequency used in the site:** 20 minutes in morning, midday, and evening; 20 minutes late night; no Owl.
- **Coverage note:** Stops at 12 a.m. on Sunday; after that use 22 Fillmore, 7 Haight, or N Judah in Hayes Valley.

### 8 Bayshore

- **Official route page:** [SFMTA 8 Bayshore](https://www.sfmta.com/routes/8-bayshore)
- **Sunday schedule page:** [8 Sunday schedule](https://www.sfmta.com/routes/schedule/8?direction_id=0&service_id=3&date=20260906)
- **Published line:** "5 a.m. - 12 a.m. daily."
- **Sunday frequency used in the site:** 10 minutes in the morning; 7 minutes in midday; 8 minutes in the evening; 15 minutes late night; no Owl.
- **Coverage note:** Stops at 12 a.m. on Sunday; the weekday 8AX/8BX express gaps do not apply on Sunday.

### 45 Union/Stockton

- **Official route page:** [SFMTA 45 Union/Stockton](https://www.sfmta.com/routes/45-unionstockton)
- **Sunday schedule page:** [45 Sunday schedule](https://www.sfmta.com/routes/schedule/45?direction_id=0&service_id=3&date=20260906)
- **Published line:** "5 a.m. - 10 p.m. daily."
- **Sunday frequency used in the site:** 15 minutes in morning, midday, and evening; no late-night or Owl service.
- **Coverage note:** Stops at 10 p.m. on Sunday; after that use N Judah or other 24-hour lines for the Marina.

### 90 San Bruno Owl

- **Official route page:** [SFMTA 90 San Bruno Owl](https://www.sfmta.com/routes/90-san-bruno-owl)
- **Sunday schedule page:** [90 Sunday schedule](https://www.sfmta.com/routes/schedule/90?direction_id=0&service_id=3&date=20260906)
- **Published line:** "12 a.m. - 5 a.m. nightly."
- **Sunday frequency used in the site:** 30 minutes late night and Owl.
- **Coverage note:** Owl-only line; runs 12 a.m.–5 a.m. every night, including Sunday.
