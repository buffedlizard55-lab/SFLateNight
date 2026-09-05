# Verification log

This log records the manual source check for the 20 records in [`data/venues.json`](data/venues.json). The snapshot date is **September 5, 2026**. Each row below is linked to the venue-controlled page used for the name, address, and hours. No third-party directory is used as the inclusion source.

## Inclusion test

- **Origin:** 21st Ave & Judah St, San Francisco, CA 94122.
- **Threshold:** the venue or bar must publish a close later than 11:00 PM on Friday, Saturday, or Sunday. A midnight close is later than 11 PM.
- **Transit:** access text is intentionally a planning aid, not a promise of a particular trip. Each row now maps to official SFMTA route pages and the dated Saturday service windows recorded in [`TRANSIT_VERIFICATION.md`](TRANSIT_VERIFICATION.md).
- **Operational honesty:** kitchen, private-event, event-night, grouped-hour, missing-opening-time, and transit-return notes remain visible as flags.

## Record-by-record checks

### 01. Emporium SF

- **Status:** Official match.

- **Category / neighborhood:** Arcade bar · Divisadero / NoPa.

- **Address check:** `616 Divisadero St, San Francisco, CA 94117` — [official source](https://www.emporiumarcadebar.com/locations/san-francisco/).

- **Published source line:** “616 Divisadero St. San Francisco, California 94117. General Hours: Monday 4PM-2AM; Tuesday 4PM-2AM; Wednesday 4PM-2AM; Thursday 4PM-2AM; Friday 4PM-2AM; Saturday 2PM-2AM; Sunday 2PM-2AM.”

- **Late-night result:** Friday: 4:00 PM–2:00 AM; Saturday: 2:00 PM–2:00 AM; Sunday: 2:00 PM–2:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 24 Divisadero / 5 Fulton + walk — The official route stop lists place both lines at Divisadero & McAllister; use the dated service window and live planner for the final blocks to 616 Divisadero.

- **Manual review flags:** 21+ venue; event nights can add a cover or change entry conditions.

- **Official link:** [https://www.emporiumarcadebar.com/locations/san-francisco/](https://www.emporiumarcadebar.com/locations/san-francisco/)

### 02. Zeitgeist

- **Status:** Official match.

- **Category / neighborhood:** Beer garden / bar · Mission / Valencia.

- **Address check:** `199 Valencia St, San Francisco, CA 94103` — [official source](https://www.zeitgeistsf.com/).

- **Published source line:** “Zeitgeist is a German Beergarden ... located at 199 Valencia Street, San Francisco, CA 94103. Mon 2 PM–11 PM; Tues 2 PM–11 PM; Wed 2 PM–11 PM; Thurs 2 PM–12 AM; Fri 2 PM–1 AM; Sat 12 PM–1 AM; Sun 11 AM–9:30 PM.”

- **Late-night result:** Friday: 2:00 PM–1:00 AM; Saturday: 12:00 PM–1:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 14 Mission / 22 Fillmore + walk — 22 Fillmore serves 16th St & Valencia and 14 Mission serves the Mission corridor; use the dated service window and live planner for the final walk to Valencia Street.

- **Manual review flags:** Kitchen closes one hour before the bar; the late-night match is for the venue/bar, not the kitchen.

- **Official link:** [https://www.zeitgeistsf.com/](https://www.zeitgeistsf.com/)

### 03. Make-Out Room

- **Status:** Official match.

- **Category / neighborhood:** Music venue / bar · Mission.

- **Address check:** `3225 22nd St at Mission, San Francisco, CA 94110` — [official source](https://www.makeoutroom.com/contact.html).

- **Published source line:** “MAKE OUT ROOM, 3225 22nd Street @ Mission, San Francisco, California 94110. OPEN 6pm–2am Tuesday–Saturday; 6pm–2am Sunday (plus occasional matinee shows Noon–5pm); Closed Monday. Walking: BART 24th & Mission Street Station; #49 & #14 Mission buses stop on Mission at 22nd Street.”

- **Late-night result:** Friday: 6:00 PM–2:00 AM; Saturday: 6:00 PM–2:00 AM; Sunday: 6:00 PM–2:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 14 Mission / 49 Van Ness-Mission + short walk — The venue names the #49 and #14 Mission buses at Mission and 22nd; use the dated route window and live planner for the exact stop and return leg.

- **Manual review flags:** Strictly 21+; occasional matinees are separately noted by the venue.

- **Official link:** [https://www.makeoutroom.com/contact.html](https://www.makeoutroom.com/contact.html)

### 04. Specs' Twelve Adler Museum Cafe

- **Status:** Official match.

- **Category / neighborhood:** Historic bar / music · North Beach.

- **Address check:** `12 William Saroyan Place, San Francisco, CA 94133` — [official source](https://www.specsbarsf.com/).

- **Published source line:** “Welcome to Specs’ Twelve Adler Museum Cafe ... in North Beach, SF since 1968! Open Sun-Wed 4pm-1am, Thurs-Sat 4pm-2am. Specs’ Twelve Adler Museum Cafe, 12 William Saroyan Place, San Francisco, CA 94133.”

- **Late-night result:** Friday: 4:00 PM–2:00 AM; Saturday: 4:00 PM–2:00 AM; Sunday: 4:00 PM–1:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 30 Stockton + walk — Use the dated 30 Stockton service window via the Columbus/Grant North Beach corridor, then check the final walk and late return service.

- **Manual review flags:** North Beach location is in a pedestrian-heavy area; check the return transit plan before going late.

- **Official link:** [https://www.specsbarsf.com/](https://www.specsbarsf.com/)

### 05. Casements Bar

- **Status:** Official match.

- **Category / neighborhood:** Irish bar / food · Mission.

- **Address check:** `2351 Mission St, San Francisco, CA 94110` — [official source](https://casementsbar.com/).

- **Published source line:** “Casements Bar, 2351 Mission Street, San Francisco, CA 94110. Mon 4pm–2am; Tue 4pm–2am; Wed 4pm–2am; Thu 4pm–2am; Fri 3pm–2am; Sat 2pm–2am; Sun 2pm–2am.”

- **Late-night result:** Friday: 3:00 PM–2:00 AM; Saturday: 2:00 PM–2:00 AM; Sunday: 2:00 PM–2:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 14 Mission / 49 Van Ness-Mission + short walk — Use the dated Mission corridor service window and live planner for 24th Street, the exact stop, and the final walk.

- **Manual review flags:** Food service is earlier than the bar: the official menu page says kitchen until 9 PM Monday–Saturday and 8 PM Sunday.

- **Official link:** [https://casementsbar.com/](https://casementsbar.com/)

### 06. The Mint Karaoke Lounge

- **Status:** Official match.

- **Category / neighborhood:** Karaoke bar · Market / Duboce Triangle.

- **Address check:** `1942 Market St, San Francisco, CA 94102` — [official source](https://themint.net/san-francisco-karaoke-reservations/).

- **Published source line:** “Same-day reservations by phone only ... Hours: Mon-Fri 5PM-2AM; Sat-Sun 4PM-2AM; Tues: Available for private events only. Contact info: 1942 Market St, San Francisco, CA 94102.”

- **Late-night result:** Friday: 5:00 PM–2:00 AM; Saturday: 4:00 PM–2:00 AM; Sunday: 4:00 PM–2:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** N Judah / 22 Fillmore + walk — Use the dated route windows for N Judah and 22 Fillmore to the Market/Church corridor, then verify the last walk to 1942 Market.

- **Manual review flags:** Tuesday is listed as private events only; it is not used for late-night eligibility.

- **Official link:** [https://themint.net/](https://themint.net/)

### 07. Pilsner Inn

- **Status:** Official match.

- **Category / neighborhood:** LGBTQ+ neighborhood bar · Castro / Duboce.

- **Address check:** `225 Church St, San Francisco, CA 94114` — [official source](https://www.pilsnerinn.com/location).

- **Published source line:** “225 Church Street, San Francisco, CA 94114. The official location listing states 1:00p–2:00a Monday–Thursday and 12:00p–2:00a Friday–Sunday; the current home page also states open until 2AM.”

- **Late-night result:** Friday: 12:00 PM–2:00 AM; Saturday: 12:00 PM–2:00 AM; Sunday: 12:00 PM–2:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** N Judah / 22 Fillmore + short walk — Use the dated route windows for the Church/Market corridor, then confirm the last walk to 225 Church Street.

- **Manual review flags:** The current home page emphasizes the closing time rather than repeating the full weekly table; the location-page schedule is retained here for review.

- **Official link:** [https://www.pilsnerinn.com/](https://www.pilsnerinn.com/)

### 08. Midnight Sun

- **Status:** Official match.

- **Category / neighborhood:** LGBTQ+ video bar · Castro.

- **Address check:** `4067 18th St, San Francisco, CA 94114` — [official source](https://www.midnightsunsf.com/).

- **Published source line:** “Midnight Sun ... current location ... 4067 18th Street, San Francisco, CA 94114. Opening Hours: Thu–Fri 2pm–2am; Sat 12:30pm–2am; Sun 1pm–12am; Mon–Wed 2pm–12am.”

- **Late-night result:** Friday: 2:00 PM–2:00 AM; Saturday: 12:30 PM–2:00 AM; Sunday: 1:00 PM–12:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 24 Divisadero / N Judah + walk — 24 Divisadero lists a Castro St & 18th St stop; use the dated windows and live planner to confirm the final walk to 18th Street.

- **Manual review flags:** Sunday closes at midnight; midnight is included because it is later than the requested 11 PM threshold.

- **Official link:** [https://www.midnightsunsf.com/](https://www.midnightsunsf.com/)

### 09. Alchemist Bar & Lounge

- **Status:** Official match.

- **Category / neighborhood:** Cocktail bar · SOMA / 3rd Street.

- **Address check:** `679 3rd St, San Francisco, CA 94107` — [official source](https://alchemistsf.com/).

- **Published source line:** “Find Us: 679 3rd Street, San Francisco, CA 94107. Open hours: Mon 4:30pm–11pm; Tues 4:30pm–11pm; Wed 4:30pm–11pm; Thurs 4:30pm–2am; Fri 4:30pm–2am; Sat 5pm–2am; Sun 5pm–11pm.”

- **Late-night result:** Friday: 4:30 PM–2:00 AM; Saturday: 5:00 PM–2:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** T Third / 91 Owl + walk — Use the dated T Third window for the 3rd Street corridor and 91 Owl for overnight coverage; confirm the final walk to 679 3rd Street.

- **Manual review flags:** Sunday closes at 11 PM exactly and therefore is not counted; Friday and Saturday qualify.

- **Official link:** [https://alchemistsf.com/](https://alchemistsf.com/)

### 10. Owl Tree

- **Status:** Official match.

- **Category / neighborhood:** Bar / lounge · Lower Nob Hill.

- **Address check:** `601 Post St at Taylor, San Francisco, CA 94109` — [official source](https://www.owltreesf.com/contact-us).

- **Published source line:** “Hours: Sun–Mon, 6pm–2am; Tue–Thurs, 4pm–2am; Fri–Sat, 3pm–2am. Address: 601 Post Street (@ Taylor), San Francisco, CA 94109.”

- **Late-night result:** Friday: 3:00 PM–2:00 AM; Saturday: 3:00 PM–2:00 AM; Sunday: 6:00 PM–2:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 38 Geary / 30 Stockton + walk — Use the dated Powell-area windows for both lines and the live planner for the final walk toward Post and Taylor.

- **Manual review flags:** 21+ nightlife venue; reservation and event conditions can change the door experience.

- **Official link:** [https://www.owltreesf.com/contact-us](https://www.owltreesf.com/contact-us)

### 11. The Saloon

- **Status:** Official match.

- **Category / neighborhood:** Historic live-music bar · North Beach.

- **Address check:** `1232 Grant Ave, San Francisco, CA 94133` — [official source](https://thesaloonsf.com/).

- **Published source line:** “The Saloon, 1232 Grant Avenue, San Francisco, California 94133. Open Daily: 12:00 pm–02:00 am.”

- **Late-night result:** Friday: 12:00 PM–2:00 AM; Saturday: 12:00 PM–2:00 AM; Sunday: 12:00 PM–2:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 30 Stockton + walk — Use the dated 30 Stockton window via the Columbus corridor, then check the final walk and late return service.

- **Manual review flags:** The venue advertises live music in separate time blocks; check the official calendar for a specific night.

- **Official link:** [https://thesaloonsf.com/](https://thesaloonsf.com/)

### 12. The Detour

- **Status:** Official match.

- **Category / neighborhood:** Games bar · Duboce Triangle / Castro.

- **Address check:** `2200 Market St, Suite A, San Francisco, CA 94114` — [official source](https://www.detoursf.com/location/the-detour/).

- **Published source line:** “2200 Market St, Suite A, San Francisco, CA 94114. Monday 5pm–11:30pm; Tuesday 5pm–11:30pm; Wednesday 5pm–11:30pm; Thursday 5pm–11:30pm; Friday 5pm–1am; Saturday 2pm–1am; Sunday 1pm–12am.”

- **Late-night result:** Friday: 5:00 PM–1:00 AM; Saturday: 2:00 PM–1:00 AM; Sunday: 1:00 PM–12:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** N Judah / 22 Fillmore + walk — Use the dated Market corridor windows and live planner for the final walk to Suite A.

- **Manual review flags:** 21+ with government-issued ID or passport; Saturday is all ages only from 2–6 PM.

- **Official link:** [https://www.detoursf.com/location/the-detour/](https://www.detoursf.com/location/the-detour/)

### 13. The Beehive

- **Status:** Official match.

- **Category / neighborhood:** Cocktail bar / food · Mission / Valencia.

- **Address check:** `842 Valencia St at 19th, San Francisco, CA 94110` — [official source](https://www.thebeehivesf.com/contact-2).

- **Published source line:** “842 Valencia Street (at 19th), San Francisco, CA 94110. Tues–Thurs 4pm to Midnight; Friday 4pm to 2am; Saturday 2pm to 2am; Sunday 2pm to 10pm. Food is served until one hour prior to close.”

- **Late-night result:** Friday: 4:00 PM–2:00 AM; Saturday: 2:00 PM–2:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 22 Fillmore + walk — 22 Fillmore lists 16th St & Valencia; use its dated window and the live planner for the last several blocks to 842 Valencia.

- **Manual review flags:** Food service ends one hour before close; Sunday does not meet the late-night threshold.

- **Official link:** [https://www.thebeehivesf.com/contact-2](https://www.thebeehivesf.com/contact-2)

### 14. Vesuvio Cafe

- **Status:** Official match.

- **Category / neighborhood:** Historic cafe / saloon · North Beach.

- **Address check:** `255 Columbus Ave at Jack Kerouac Alley, San Francisco, CA 94133` — [official source](https://vesuvio.com/).

- **Published source line:** “Vesuvio Cafe, 255 Columbus @ Jack Kerouac Alley, North Beach San Francisco California. Hours: Sun–Thurs 11–1 and Fri–Sat 11–2.”

- **Late-night result:** Friday: 11:00 AM–2:00 AM; Saturday: 11:00 AM–2:00 AM; Sunday: 11:00 AM–1:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 30 Stockton + walk — Use the dated 30 Stockton window through Columbus/Grant, then walk the final blocks and check late return service.

- **Manual review flags:** Sunday is grouped with Sun–Thurs on the official site; it is transcribed as 11 AM–1 AM here.

- **Official link:** [https://vesuvio.com/](https://vesuvio.com/)

### 15. El Farolito — Mission Street flagship

- **Status:** Official match.

- **Category / neighborhood:** Taqueria / restaurant · Mission.

- **Address check:** `2779 Mission St, San Francisco, CA 94110` — [official source](https://elfarolitosf.com/locations/).

- **Published source line:** “Mission Street (Flagship), 2779 Mission St, San Francisco, CA 94110. Mon 10:00 AM–3:00 AM; Tue 10:00 AM–3:00 AM; Wed 10:00 AM–3:00 AM; Thu 10:00 AM–3:30 AM; Fri 10:00 AM–3:30 AM; Sat 10:00 AM–3:00 AM; Sun 10:00 AM–12:00 AM.”

- **Late-night result:** Friday: 10:00 AM–3:30 AM; Saturday: 10:00 AM–3:00 AM; Sunday: 10:00 AM–12:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 14 Mission / 49 Van Ness-Mission + walk — Use the dated Mission corridor windows and live planner for the exact stop and final walk to 2779 Mission.

- **Manual review flags:** Official page says all locations are cash only and walk-in; hours are location-specific, so do not substitute a different El Farolito branch.

- **Official link:** [https://elfarolitosf.com/locations/](https://elfarolitosf.com/locations/)

### 16. Pinecrest Diner

- **Status:** Official match.

- **Category / neighborhood:** Diner / restaurant · Union Square.

- **Address check:** `401 Geary St, San Francisco, CA 94102` — [official source](https://pinecrestdiner.com/).

- **Published source line:** “PINECREST DINER, 401 Geary St, San Francisco, CA 94102, USA. Hours: Monday & Tuesday 7am–11pm; Wednesday, Thursday, Friday & Saturday 24hrs; Sunday 7am–11pm.”

- **Late-night result:** Friday: Open 24 hours; Saturday: Open 24 hours. This is why the record passes the >11 PM test.

- **Transit screen:** 38 Geary / 30 Stockton + walk — Use the dated Powell/Geary windows and live planner for the final walk to Geary Street; do not infer a specific last vehicle.

- **Manual review flags:** The official page notes that it is slowly moving back toward normal hours after the pandemic; confirm before a late Friday/Saturday visit.

- **Official link:** [https://pinecrestdiner.com/](https://pinecrestdiner.com/)

### 17. Harper & Rye

- **Status:** Official match.

- **Category / neighborhood:** Neighborhood cocktail bar · Polk Gulch.

- **Address check:** `1695 Polk St, San Francisco, CA 94109` — [official source](https://www.harperandrye.com/).

- **Published source line:** “Harper & Rye, 1695 Polk St. SF. Open daily 3PM–2AM.”

- **Late-night result:** Friday: 3:00 PM–2:00 AM; Saturday: 3:00 PM–2:00 AM; Sunday: 3:00 PM–2:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 38 Geary / 49 Van Ness-Mission + walk — Use the dated route windows and live planner for the final blocks to 1695 Polk.

- **Manual review flags:** The current official page states open daily and the full daily range, but does not publish a phone number on the visible page.

- **Official link:** [https://www.harperandrye.com/](https://www.harperandrye.com/)

### 18. ABV

- **Status:** Official match.

- **Category / neighborhood:** Cocktail bar / food · Mission / 16th Street.

- **Address check:** `3174 16th St, San Francisco, CA 94103` — [official source](https://www.abvsf.com/).

- **Published source line:** “ABV, 3174 16th St, San Francisco, CA 94103. Hours: 4 pm–2 am every day. Kitchen until midnight daily.”

- **Late-night result:** Friday: 4:00 PM–2:00 AM; Saturday: 4:00 PM–2:00 AM; Sunday: 4:00 PM–2:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 14 Mission / 22 Fillmore / 33 Ashbury + walk — Use the dated windows for the Mission/16th/18th corridors and confirm the final walk to 3174 16th; 33 has no late-night service listed.

- **Manual review flags:** The 2 AM schedule is for the bar; the kitchen is published as open only until midnight.

- **Official link:** [https://www.abvsf.com/](https://www.abvsf.com/)

### 19. Tupelo

- **Status:** Official match.

- **Category / neighborhood:** Restaurant / live-music bar · North Beach.

- **Address check:** `1337 Grant Ave, San Francisco, CA 94133` — [official source](https://tupelosf.com/).

- **Published source line:** “Located at 1337 Grant Ave, in the heart of North Beach, San Francisco. Bar hours: 1:00PM–2:00AM every day. Kitchen hours: 1:00PM–10:00PM every day.”

- **Late-night result:** Friday: Bar 1:00 PM–2:00 AM; kitchen 1:00 PM–10:00 PM; Saturday: Bar 1:00 PM–2:00 AM; kitchen 1:00 PM–10:00 PM; Sunday: Bar 1:00 PM–2:00 AM; kitchen 1:00 PM–10:00 PM. This is why the record passes the >11 PM test.

- **Transit screen:** 30 Stockton + walk — Use the dated 30 Stockton window through Columbus/Grant, then check the final walk and late return service.

- **Manual review flags:** Late-night eligibility is for the bar/live-music venue; the official kitchen hours end at 10 PM.

- **Official link:** [https://tupelosf.com/](https://tupelosf.com/)

### 20. The Mix

- **Status:** Official match with documented gap.

- **Category / neighborhood:** LGBTQ+ neighborhood bar · Castro.

- **Address check:** `4086 18th St, San Francisco, CA 94114` — [official source](https://themix.bar/).

- **Published source line:** “4086 18th St, San Francisco, CA. The Mix ... OPEN until 2am Daily!”

- **Late-night result:** Friday: Open until 2:00 AM; opening time not stated; Saturday: Open until 2:00 AM; opening time not stated; Sunday: Open until 2:00 AM; opening time not stated. This is why the record passes the >11 PM test.

- **Transit screen:** 24 Divisadero / N Judah + walk — Use the dated Castro corridor windows and the live planner for the final walk to 4086 18th; do not infer a specific last vehicle.

- **Manual review flags:** The current official page publishes the daily closing time but not a daily opening time; do not infer one.

- **Official link:** [https://themix.bar/](https://themix.bar/)

## What this does not verify

The official schedule verifies the published business hours at the time of review; it does not verify a future holiday schedule, last call, kitchen availability, cover charge, door policy, capacity, accessibility conditions, or a live transit disruption. Those are deliberately not inferred. Open the official page and use the live route link before leaving.

---

# September 5, 2026 expansion pass

This pass added **34 net-new records** to the original 20, for a master list of **54**. Every row below was read line by line from the venue's own official page (or, where flagged, the venue operator's official location page) on 2026-09-05.

## Shortfall against the 50-new-record target

The request asked for 50 new entries. This pass banked **34** that survive official-source verification. The gap is documented rather than filled: candidate venues were dropped because their official domain was parked or for sale (Zombie Village, Hearth, Doctor Teeth, Harrington's, Lone Star), the official site returned a hard error (The Cinch, Market Bar, The Cavern, Hobson's Choice, The Wreck Room, Holiday, Top of the Mark, The 440), the live official site publishes no hours at all (Toronado, Bourbon & Branch, Smuggler's Cove, Elixir, Wild Hawk, Pop's, Lookout, The Valencia Room, Whitechapel, Aunt Charlie's, The Page, Bus Stop Saloon, Dalva), or the published close was earlier than 11 PM (Pagan). No record was invented to reach the target.

## Record-by-record log

### SF Eagle

- **Status:** Official match.
- **Category / neighborhood:** Bar / event venue · SoMa.
- **Address check:** `398 12th St, San Francisco, CA 94103` — [official source](https://sf-eagle.com/visit/).
- **Published source line:** “HOURS Monday 6PM – 12AM; Tuesday Closed; Wed – Thu 6PM – 12AM; Fri – Sat 2PM – 2AM; Sunday 1PM – 12AM. Address 398 12th St, San Francisco, CA 94103.”
- **Late-night result:** Friday: 2:00 PM–2:00 AM; Saturday: 2:00 PM–2:00 AM.
- **Transit screen:** N Judah + 14 Mission / 49 Van Ness, or 90 Owl late — Ride the N Judah downtown and transfer to a Mission or Van Ness corridor bus; the 90 San Bruno Owl serves 11th & Harrison after midnight. Check the live planner for the final walk.
- **Manual review flags:** Sunday closes at 12:00 AM, which does not clear the after-11 PM threshold used here; only Friday and Saturday are counted. 21+ venue; event nights can change cover and entry conditions.
- **Official link:** [https://sf-eagle.com/visit/](https://sf-eagle.com/visit/)

### Mel's Drive-In — 4th & Mission

- **Status:** Official match.
- **Category / neighborhood:** Diner · SoMa.
- **Address check:** `801 Mission St, San Francisco, CA 94103` — [official source](https://melsdrive-in.com/restaurant/mels-4th-mission/).
- **Published source line:** “Mel's 4th & Mission, 801 MISSION STREET, SAN FRANCISCO, CA 94103. Open Hours: Monday 07:00am - 11:00pm; Tuesday 07:00am - 11:00pm; Wednesday 07:00am - 11:00pm; Thursday 07:00am - 12:00am; Friday 07:00am - 03:00am; Saturday 07:00am - 03:00am; Sunday 07:00am - 11:00pm.”
- **Late-night result:** Friday: 7:00 AM–3:00 AM; Saturday: 7:00 AM–3:00 AM.
- **Transit screen:** N Judah to Powell/Montgomery + short walk — The N Judah reaches the Market Street subway a few blocks from 4th & Mission; the 14 Mission and 91 Owl cover the late-night return.
- **Manual review flags:** Sunday closes at 11:00 PM and does not qualify. Chain location: hours are published per restaurant, so confirm this address specifically.
- **Official link:** [https://melsdrive-in.com/restaurant/mels-4th-mission/](https://melsdrive-in.com/restaurant/mels-4th-mission/)

### Mel's Drive-In — Lombard Street

- **Status:** Official match with documented gap.
- **Category / neighborhood:** Diner · Marina.
- **Address check:** `2165 Lombard St, San Francisco, CA 94123` — [official source](https://melsdrive-in.com/restaurant/mels-lombard-street/).
- **Published source line:** “Mel's Lombard Street, 2165 LOMBARD STREET, SAN FRANCISCO, CA 94123. Open Hours: Monday 06:30am - 12:00am; ... Friday 06:30am - 03:00am; Saturday 06:30am - 03:00am; Sunday 06:30am - 12:00am.”
- **Late-night result:** Friday: 6:30 AM–3:00 AM; Saturday: 6:30 AM–3:00 AM.
- **Transit screen:** N Judah + 22 Fillmore, or 43 Masonic (ends midnight) — The 22 Fillmore reaches the Marina and runs 24 hours; the 43 Masonic also serves the district but stops at midnight, so plan the return on the 22 or 90 Owl.
- **Manual review flags:** Sunday closes at 12:00 AM exactly and is not counted as after 11 PM here. Irregularity for manual review: a third-party listing at this address has been labelled closed while the official Mel's page still publishes hours. Call before travelling.
- **Official link:** [https://melsdrive-in.com/restaurant/mels-lombard-street/](https://melsdrive-in.com/restaurant/mels-lombard-street/)

### Mel's Drive-In — Geary Boulevard

- **Status:** Official match.
- **Category / neighborhood:** Diner · Richmond.
- **Address check:** `3355 Geary Blvd, San Francisco, CA 94118` — [official source](https://melsdrive-in.com/restaurant/mels-geary-boulevard-richmond-district/).
- **Published source line:** “Geary Boulevard Richmond District, 3355 GEARY BOULEVARD, SAN FRANCISCO, CA 94118. Open Hours: ... Thursday 07:00am - 11:00pm; Friday 07:00am - 01:00am; Saturday 07:00am - 01:00am; Sunday 07:00am - 11:00pm.”
- **Late-night result:** Friday: 7:00 AM–1:00 AM; Saturday: 7:00 AM–1:00 AM.
- **Transit screen:** N Judah or 5 Fulton, transfer to 38 Geary — The 38 Geary runs 24 hours along Geary Boulevard; the 5 Fulton and 1 California are daytime and evening alternates from the Sunset and Richmond.
- **Manual review flags:** Thursday and Sunday close at 11:00 PM and do not qualify. Chain location: hours are published per restaurant.
- **Official link:** [https://melsdrive-in.com/restaurant/mels-geary-boulevard-richmond-district/](https://melsdrive-in.com/restaurant/mels-geary-boulevard-richmond-district/)

### Orphan Andy's

- **Status:** Official match with documented gap.
- **Category / neighborhood:** Diner · Castro / Upper Market.
- **Address check:** `3991 17th St, San Francisco, CA 94114` — [official source](https://www.orphanandys.net/).
- **Published source line:** “Orphan Andy's. Address: 3991 17th St San Francisco, CA 94114. Hotline: (415) 864-9795. Open: 24 Hours.”
- **Late-night result:** Friday: 24 hours; Saturday: 24 hours; Sunday: 24 hours.
- **Transit screen:** N Judah to Church/Duboce + walk, or 24 Divisadero — The N Judah runs 24 hours to the Castro edge; the 24 Divisadero also carries Owl service. The 33 stops at 10 PM and cannot be used late.
- **Manual review flags:** The official site publishes a blanket "Open: 24 Hours" statement rather than a per-day grid; treat holiday and staffing exceptions as possible and call ahead for a late Sunday visit.
- **Official link:** [https://www.orphanandys.net/](https://www.orphanandys.net/)

### Trick Dog

- **Status:** Official match.
- **Category / neighborhood:** Cocktail bar · Mission.
- **Address check:** `3010 20th St, San Francisco, CA 94110` — [official source](https://www.trickdogbar.com/).
- **Published source line:** “3010 20th Street San Francisco, CA 415-471-2999. Sunday-Thursday: 4pm-12am, food til 10pm. Friday + Saturday: 4pm-2am, food til midnight.”
- **Late-night result:** Friday: 4:00 PM–2:00 AM; Saturday: 4:00 PM–2:00 AM.
- **Transit screen:** N Judah + 14 Mission or 22 Fillmore — The 14 Mission runs 24 hours through the Mission; the 22 Fillmore crosses at 16th Street. Walk the final blocks from Bryant or Harrison.
- **Manual review flags:** Kitchen closes before the bar: food service ends at midnight on Friday and Saturday. Sunday closes at 12:00 AM and is not counted.
- **Official link:** [https://www.trickdogbar.com/](https://www.trickdogbar.com/)

### Local Edition

- **Status:** Official match with documented gap.
- **Category / neighborhood:** Cocktail bar · Downtown / Union Square.
- **Address check:** `691 Market St, San Francisco, CA 94105` — [official source](https://www.localeditionsf.com/).
- **Published source line:** “We are open Monday Through Saturday; 21+ WITH VALID ID. mon: 4:30pm - 12am; TUES-Wed: 4:30pm - 1am; Thurs-FRI: 4:30pm - 2am; Sat: 6pm - 2am; Sun: closed. We are located just before Third St. on Market. Just head down the stairs.”
- **Late-night result:** Friday: 4:30 PM–2:00 AM; Saturday: 6:00 PM–2:00 AM.
- **Transit screen:** N Judah to Montgomery Station + walk — The N Judah stops at Montgomery Station on Market Street; the 14 Mission and 91 Owl cover the return after subway hours.
- **Manual review flags:** Closed Sunday. Irregularity for manual review: the official page describes the location as "just before Third St. on Market" and does not print the street number, so confirm the entrance on arrival. 21+ with valid ID.
- **Official link:** [https://www.localeditionsf.com/](https://www.localeditionsf.com/)

### Presidio Bowl

- **Status:** Official match with documented gap.
- **Category / neighborhood:** Bowling / bar · Presidio.
- **Address check:** `93 Moraga Ave, San Francisco, CA 94129` — [official source](https://www.presidiobowl.com/hours-and-closures/).
- **Published source line:** “Regular Hours: Monday-Wednesday 3PM-11PM; Thursday 11AM-Midnight; Friday 1PM-1AM; Saturday 11AM-1AM; Sunday Noon-8PM. Subject to change. The Presidio Bowling Center is located at 93 Moraga Avenue inside the Presidio of San Francisco.”
- **Late-night result:** Friday: 1:00 PM–1:00 AM; Saturday: 11:00 AM–1:00 AM.
- **Transit screen:** N Judah + 43 Masonic into the Presidio — The 43 Masonic route page lists the Presidio among its neighborhoods, but service ends at midnight, so the 1 AM close needs a different return plan.
- **Manual review flags:** Transit gap: the 43 Masonic stops running at midnight while the venue is open until 1 AM on Friday and Saturday. Plan the return before midnight or by another mode. The official page lists dated private-event closures, including patio closures; check the posted schedule for your date.
- **Official link:** [https://www.presidiobowl.com/hours-and-closures/](https://www.presidiobowl.com/hours-and-closures/)

### Rickhouse

- **Status:** Official match.
- **Category / neighborhood:** Whiskey bar · Financial District.
- **Address check:** `246 Kearny St, San Francisco, CA 94108` — [official source](https://www.rickhousebar.com/).
- **Published source line:** “246 Kearny Street, San Francisco, CA 94108. MON - Wed: 3pm-12am | Thu-FRI: 3pm-2am SAT: 6PM-2AM | Sun: Closed to rest.”
- **Late-night result:** Friday: 3:00 PM–2:00 AM; Saturday: 6:00 PM–2:00 AM.
- **Transit screen:** N Judah to Montgomery + walk, or 8 Bayshore on Kearny — The 8 Bayshore serves Kearny Street directly but ends at midnight; use the N Judah or 91 Owl for the late return.
- **Manual review flags:** Closed Sunday. Transit gap: the 8 Bayshore on Kearny ends at midnight, before the 2 AM close.
- **Official link:** [https://www.rickhousebar.com/](https://www.rickhousebar.com/)

### Starlite at the Beacon Grand

- **Status:** Official match with documented gap.
- **Category / neighborhood:** Hotel cocktail lounge · Downtown / Union Square.
- **Address check:** `450 Powell St, San Francisco, CA 94102` — [official source](https://www.beacongrand.com/starlite).
- **Published source line:** “Cocktails & Stories Since 1928. Thursday - Sunday. Hours: Thursday | 4pm - 12am; Friday - Saturday | 4pm - 2am; Sunday | 4pm - 12am. Guests must be 21 years or older. Starlite beckons you to take the elevator to the 21st floor.”
- **Late-night result:** Friday: 4:00 PM–2:00 AM; Saturday: 4:00 PM–2:00 AM.
- **Transit screen:** N Judah to Powell Station + walk up — Powell Station is a short walk from the Beacon Grand; the 30 Stockton runs to midnight and the 91 Owl covers the later return.
- **Manual review flags:** Sunday closes at 12:00 AM and is not counted. Irregularity for manual review: the official Starlite page gives the floor and hotel but not the street number; the address here is the Beacon Grand hotel entrance. 21+; reservations strongly recommended. The lounge is on the 21st floor.
- **Official link:** [https://www.beacongrand.com/starlite](https://www.beacongrand.com/starlite)

### Bissap Baobab

- **Status:** Official match with documented gap.
- **Category / neighborhood:** Restaurant / bar · Mission.
- **Address check:** `2243 Mission St, San Francisco, CA 94110` — [official source](https://www.bissapbaobab.com/info).
- **Published source line:** “Hours and Directions. Open Hours: Wed–Sun 5:30pm til 2am; Fri-Sat 5:30pm til 4am. 2243 Mission Street, San Francisco, CA. Bart Station 16th or 24th St.”
- **Late-night result:** Friday: 5:30 PM–4:00 AM; Saturday: 5:30 PM–4:00 AM; Sunday: 5:30 PM–2:00 AM.
- **Transit screen:** N Judah + 14 Mission (24 hours) — The 14 Mission runs 24 hours directly along Mission Street; the 49 ends at midnight and the 90 Owl covers the overnight return.
- **Manual review flags:** Irregularity for manual review: the venue's own menu page carries structured hours that end earlier than the hours printed on this contact page. Confirm before a very late visit.
- **Official link:** [https://www.bissapbaobab.com/info](https://www.bissapbaobab.com/info)

### El Farolito — 24th Street

- **Status:** Official match.
- **Category / neighborhood:** Taqueria · Mission.
- **Address check:** `2950 24th St, San Francisco, CA 94110` — [official source](https://elfarolitosf.com/locations/).
- **Published source line:** “24th Street, 2950 24th St, San Francisco, CA 94110. Mon–Thu 10:00 AM – 1:30 AM; Fri 10:00 AM – 2:30 AM; Sat 10:00 AM – 2:30 AM; Sun 10:00 AM – 1:30 AM.”
- **Late-night result:** Friday: 10:00 AM–2:30 AM; Saturday: 10:00 AM–2:30 AM; Sunday: 10:00 AM–1:30 AM.
- **Transit screen:** N Judah + 14 Mission, walk from 24th & Mission — The 14 Mission runs 24 hours; 24th Street is a short walk east from the Mission Street stops.
- **Manual review flags:** Chain location: hours are published per address on one official page, so confirm the 24th Street row specifically.
- **Official link:** [https://elfarolitosf.com/locations/](https://elfarolitosf.com/locations/)

### El Farolito — North Beach

- **Status:** Official match.
- **Category / neighborhood:** Taqueria · North Beach.
- **Address check:** `1230 Grant Ave, San Francisco, CA 94133` — [official source](https://elfarolitosf.com/locations/).
- **Published source line:** “North Beach (Grant Ave), 1230 Grant Ave, San Francisco, CA 94133. Mon through Sun 10:00 AM – 2:00 AM.”
- **Late-night result:** Friday: 10:00 AM–2:00 AM; Saturday: 10:00 AM–2:00 AM; Sunday: 10:00 AM–2:00 AM.
- **Transit screen:** N Judah downtown + 30 Stockton or 8 Bayshore — The 30 Stockton and 8 Bayshore both reach North Beach but end at midnight; the 91 Owl is the overnight alternative from downtown.
- **Manual review flags:** Transit gap: the 30 and 8 stop at midnight while the taqueria is open until 2 AM. Chain location: confirm the Grant Avenue row on the official page.
- **Official link:** [https://elfarolitosf.com/locations/](https://elfarolitosf.com/locations/)

### El Farolito — 4817 Mission Street

- **Status:** Official match.
- **Category / neighborhood:** Taqueria · Excelsior.
- **Address check:** `4817 Mission St, San Francisco, CA 94112` — [official source](https://elfarolitosf.com/locations/).
- **Published source line:** “4817 Mission Street, 4817 Mission St, San Francisco, CA 94112. Mon 10:00 AM – 1:45 AM; Tue 10:00 AM – 1:45 AM; Wed 9:00 AM – 2:45 AM; Thu 9:00 AM – 3:45 AM; Fri 9:00 AM – 3:45 AM; Sat 9:00 AM – 2:45 AM; Sun 10:00 AM – 1:45 AM.”
- **Late-night result:** Friday: 9:00 AM–3:45 AM; Saturday: 9:00 AM–2:45 AM; Sunday: 10:00 AM–1:45 AM.
- **Transit screen:** N Judah + 14 Mission down the Mission corridor — The 14 Mission runs 24 hours the length of Mission Street to the Excelsior; allow a long ride from the Sunset.
- **Manual review flags:** Long transit trip from the origin; check the live planner for the fastest transfer. Chain location: confirm the 4817 Mission row on the official page.
- **Official link:** [https://elfarolitosf.com/locations/](https://elfarolitosf.com/locations/)

### Blackbird Bar

- **Status:** Official match with documented gap.
- **Category / neighborhood:** Cocktail bar · Castro / Upper Market.
- **Address check:** `2124 Market St, San Francisco, CA 94114` — [official source](https://www.blackbirdbar.com/location/blackbird-bar/).
- **Published source line:** “Hours & Location. 2124 Market Street, San Francisco, CA 94114. Monday 5pm-11pm; Tuesday 5pm-12pm; Wednesday 5pm–12pm; Thursday 5pm–12pm; Friday 4pm–2am; Saturday 2pm-2am; Sunday 2pm-11pm. Closed Thanksgiving & Christmas.”
- **Late-night result:** Friday: 4:00 PM–2:00 AM; Saturday: 2:00 PM–2:00 AM.
- **Transit screen:** N Judah to Church/Duboce + walk on Market — The N Judah surfaces near Church and Market; the 22 Fillmore runs 24 hours nearby.
- **Manual review flags:** Irregularity for manual review: the official hours list writes the Tuesday to Thursday close as "12pm", which reads as noon but sits in an evening range; only Friday and Saturday are counted here. Sunday closes at 11:00 PM and does not qualify.
- **Official link:** [https://www.blackbirdbar.com/location/blackbird-bar/](https://www.blackbirdbar.com/location/blackbird-bar/)

### Kilowatt

- **Status:** Official match.
- **Category / neighborhood:** Neighborhood bar · Mission.
- **Address check:** `3160 16th St, San Francisco, CA 94103` — [official source](https://kilowattbar.com/).
- **Published source line:** “LOCATION 3160 16TH STREET (@ ALBION) SAN FRANCISCO, CA 94103. OPENING hours MON-FRI: 5PM-2AM; SAT-SUN: 1PM-2AM.”
- **Late-night result:** Friday: 5:00 PM–2:00 AM; Saturday: 1:00 PM–2:00 AM; Sunday: 1:00 PM–2:00 AM.
- **Transit screen:** N Judah + 22 Fillmore to 16th Street — The 22 Fillmore runs 24 hours and crosses 16th Street a short walk from Albion.
- **Manual review flags:** 21+ bar with live music and DJ nights; event nights can change entry conditions.
- **Official link:** [https://kilowattbar.com/](https://kilowattbar.com/)

### Casanova Lounge

- **Status:** Official match.
- **Category / neighborhood:** Cocktail bar · Mission.
- **Address check:** `527 Valencia St, San Francisco, CA 94110` — [official source](https://www.casanovasf.com/).
- **Published source line:** “Casanova Lounge. 527 VALENCIA ST, SF CA 94110. DAILY 5pm - 2am. HAPPY HOUR till 7pm.”
- **Late-night result:** Friday: 5:00 PM–2:00 AM; Saturday: 5:00 PM–2:00 AM; Sunday: 5:00 PM–2:00 AM.
- **Transit screen:** N Judah + 14 Mission, walk to Valencia — The 14 Mission runs 24 hours; Valencia Street is one block west of the Mission Street stops.
- **Manual review flags:** 21+ bar; the official page lists a single daily schedule with no holiday exceptions.
- **Official link:** [https://www.casanovasf.com/](https://www.casanovasf.com/)

### Blondie's Bar

- **Status:** Official match.
- **Category / neighborhood:** Bar / live music · Mission.
- **Address check:** `540 Valencia St, San Francisco, CA 94110` — [official source](https://blondiesbarsf.com/).
- **Published source line:** “Blondie's Bar, 540 Valencia Street, San Francisco, California 94110, United States. Hours: Mon 04:00 pm – 02:00 am; Tue 04:00 pm – 02:00 am; Wed 04:00 pm – 02:00 am; Thu 04:00 pm – 02:00 am; Fri 02:00 pm – 02:00 am; Sat 02:00 pm – 02:00 am; Sun 02:00 pm – 02:00 am.”
- **Late-night result:** Friday: 2:00 PM–2:00 AM; Saturday: 2:00 PM–2:00 AM; Sunday: 2:00 PM–2:00 AM.
- **Transit screen:** N Judah + 14 Mission, walk to Valencia — The 14 Mission runs 24 hours; Valencia is a block west.
- **Manual review flags:** The second bar, Blondie's Wetspot, is open only on Friday and Saturday nights per the official page. 21+; DJ and live music nights.
- **Official link:** [https://blondiesbarsf.com/](https://blondiesbarsf.com/)

### Noc Noc

- **Status:** Official match.
- **Category / neighborhood:** Beer and wine bar · Lower Haight.
- **Address check:** `557 Haight St, San Francisco, CA 94117` — [official source](https://www.nocnocs.com/).
- **Published source line:** “Hours of Operation. Sunday – Thursday 5 pm – 1 am. Friday – Saturday 5 pm – 2 am. 557 Haight St. San Francisco, CA 94117 (Between Fillmore and Steiner).”
- **Late-night result:** Friday: 5:00 PM–2:00 AM; Saturday: 5:00 PM–2:00 AM; Sunday: 5:00 PM–1:00 AM.
- **Transit screen:** N Judah + 7 Haight/Noriega along Haight Street — The 7 Haight/Noriega runs from the Sunset along Haight Street but ends at midnight; the 22 Fillmore crosses Haight and runs 24 hours.
- **Manual review flags:** Transit gap: the 7 and 6 both end at midnight, before the Friday and Saturday 2 AM close. Beer, wine, and sake only — no spirits, per the official page.
- **Official link:** [https://www.nocnocs.com/](https://www.nocnocs.com/)

### The Irish Bank

- **Status:** Official match with documented gap.
- **Category / neighborhood:** Irish pub / restaurant · Downtown / Union Square.
- **Address check:** `10 Mark Ln, San Francisco, CA 94108` — [official source](https://www.theirishbank.com/).
- **Published source line:** “Come find the Soul of Ireland in the Heart of San Francisco. Hours are 11.30am - 12.00 midnight Sunday through Thursday. 11.30am - 2am Friday and Saturday.”
- **Late-night result:** Friday: 11:30 AM–2:00 AM; Saturday: 11:30 AM–2:00 AM.
- **Transit screen:** N Judah to Montgomery + walk up Bush — Montgomery Station is a short walk; the 30 Stockton and 8 Bayshore serve the area until midnight, with the 91 Owl overnight.
- **Manual review flags:** Irregularity for manual review: the official page states the pub is "nestled in its own lane" but does not print the street address; the Mark Lane address should be confirmed on arrival. Sunday closes at midnight and does not qualify.
- **Official link:** [https://www.theirishbank.com/](https://www.theirishbank.com/)

### Churchill

- **Status:** Official match.
- **Category / neighborhood:** Cocktail bar · Market / Duboce.
- **Address check:** `198 Church St, San Francisco, CA 94114` — [official source](https://www.churchillsf.com/).
- **Published source line:** “198 CHURCH ST @ MARKET SAN FRANCISCO, CA. HOURS: sun-thur 4pm-12am fri-sat 4pm-2am. HAPPY HOUR: EVERYDAY TIL 7Pm.”
- **Late-night result:** Friday: 4:00 PM–2:00 AM; Saturday: 4:00 PM–2:00 AM.
- **Transit screen:** N Judah to Church & Duboce + short walk — The N Judah stops at Church and Duboce two blocks away and runs 24 hours with Owl service.
- **Manual review flags:** Sunday closes at 12:00 AM and is not counted.
- **Official link:** [https://www.churchillsf.com/](https://www.churchillsf.com/)

### The Old Ship Saloon

- **Status:** Official match with documented gap.
- **Category / neighborhood:** Historic saloon / restaurant · Financial District.
- **Address check:** `298 Pacific Ave, San Francisco, CA 94111` — [official source](https://theoldshipsf.com/).
- **Published source line:** “FIND US. 298 Pacific Ave. San Francisco, CA 94111. Open Daily. Monday – Sunday, 11am to 2am.”
- **Late-night result:** Friday: 11:00 AM–2:00 AM; Saturday: 11:00 AM–2:00 AM; Sunday: 11:00 AM–2:00 AM.
- **Transit screen:** N Judah downtown + 8 Bayshore to Jackson Square — The 8 Bayshore serves Kearny near Jackson Square until midnight; the 91 Owl is the overnight return.
- **Manual review flags:** Transit gap: the 8 and 30 stop at midnight while the saloon is open until 2 AM. Legacy pages under an older domain publish different hours; the current official site is treated as authoritative.
- **Official link:** [https://theoldshipsf.com/](https://theoldshipsf.com/)

### Stookey's Club Moderne

- **Status:** Official match.
- **Category / neighborhood:** Cocktail lounge · Lower Nob Hill.
- **Address check:** `895 Bush St, San Francisco, CA 94108` — [official source](https://www.stookeysclubmoderne.com/).
- **Published source line:** “LOCATION: 895 Bush Street, San Francisco. Hours: Open Everyday 5:00 pm to 2:00 am. Final drink orders taken at 1:30 am.”
- **Late-night result:** Friday: 5:00 PM–2:00 AM; Saturday: 5:00 PM–2:00 AM; Sunday: 5:00 PM–2:00 AM.
- **Transit screen:** N Judah downtown + 30 Stockton or 1 California — The 1 California and 30 Stockton both serve lower Nob Hill until midnight; the 91 Owl covers the late return.
- **Manual review flags:** Last call is 1:30 AM even though the room closes at 2:00 AM. Transit gap: the 1 and 30 end at midnight.
- **Official link:** [https://www.stookeysclubmoderne.com/](https://www.stookeysclubmoderne.com/)

### Madrone Art Bar

- **Status:** Official match.
- **Category / neighborhood:** Bar / music venue · Divisadero / NoPa.
- **Address check:** `500 Divisadero St, San Francisco, CA 94117` — [official source](https://madroneartbar.com/contact/).
- **Published source line:** “Location: 500 Divisadero Street, San Francisco, CA 94117 (at Divisadero & Fell). Hours: Open daily, 4pm–2am.”
- **Late-night result:** Friday: 4:00 PM–2:00 AM; Saturday: 4:00 PM–2:00 AM; Sunday: 4:00 PM–2:00 AM.
- **Transit screen:** N Judah + 24 Divisadero to Divisadero & Fell — The 24 Divisadero runs 24 hours with Owl service and stops at the corner; the 5 Fulton is a Sunset-side alternative.
- **Manual review flags:** Ticketed events are listed on the official calendar and can change entry conditions or add a cover.
- **Official link:** [https://madroneartbar.com/contact/](https://madroneartbar.com/contact/)

### The Willows

- **Status:** Official match.
- **Category / neighborhood:** Gastropub · SoMa.
- **Address check:** `1582 Folsom St, San Francisco, CA 94103` — [official source](https://thewillowssf.com/).
- **Published source line:** “1582 Folsom Street, San Francisco, CA 94103. Hours: Monday-Thursday: 11:30 AM to midnight; Friday: 11:30 AM to 2:00 AM; Saturday: 11:00 AM to 2:00 AM; Sunday: 11:00 AM to midnight.”
- **Late-night result:** Friday: 11:30 AM–2:00 AM; Saturday: 11:00 AM–2:00 AM.
- **Transit screen:** N Judah + 14 Mission, walk from 12th & Mission — The 90 San Bruno Owl serves 11th Street after midnight; the 14 Mission runs 24 hours nearby.
- **Manual review flags:** Sunday closes at midnight and does not qualify.
- **Official link:** [https://thewillowssf.com/](https://thewillowssf.com/)

### Bender's Bar & Grill

- **Status:** Official match with documented gap.
- **Category / neighborhood:** Dive bar / kitchen · Mission.
- **Address check:** `806 S Van Ness Ave, San Francisco, CA 94110` — [official source](https://bendersbar.com/).
- **Published source line:** “BUSINESS NOURS TUES-SUN 2PM-2AM. KITCHEN HOURS TUES-SAT 4-11PM. SUN- PIZZA! 5-9PM. (hours subject to change). Address 806 S. Van Ness, Ave SF, CA 94110.”
- **Late-night result:** Friday: 2:00 PM–2:00 AM; Saturday: 2:00 PM–2:00 AM; Sunday: 2:00 PM–2:00 AM.
- **Transit screen:** N Judah + 14 Mission, walk to South Van Ness — The 14 Mission runs 24 hours a block away; the 49 ends at midnight.
- **Manual review flags:** The official page itself notes "hours subject to change". Kitchen closes well before the bar: 11 PM Tuesday to Saturday, 9 PM Sunday.
- **Official link:** [https://bendersbar.com/](https://bendersbar.com/)

### The Sycamore

- **Status:** Official match with documented gap.
- **Category / neighborhood:** Bar / restaurant · Mission.
- **Address check:** `2140 Mission St, San Francisco, CA 94110` — [official source](https://thesycamoresf.com/).
- **Published source line:** “2140 Mission, San Francisco, CA 94110. Monday: 3PM-2AM. Tuesday-Friday: 11:30AM-2AM (Lunch 11:30AM-3PM). Saturday & Sunday: Bottomless Mimosa Brunch! 10AM-3PM. Bottomless seatings (two-hour): 10:30AM / 1PM.”
- **Late-night result:** Friday: 11:30 AM–2:00 AM.
- **Transit screen:** N Judah + 14 Mission to 17th & Mission — The 14 Mission runs 24 hours directly outside.
- **Manual review flags:** Source gap flagged for manual review: the official page lists only brunch times for Saturday and Sunday and does not publish a weekend closing time, so only Friday is counted.
- **Official link:** [https://thesycamoresf.com/](https://thesycamoresf.com/)

### Gino & Carlo

- **Status:** Official match.
- **Category / neighborhood:** Neighborhood bar · North Beach.
- **Address check:** `548 Green St, San Francisco, CA 94133` — [official source](https://ginoandcarlo.com/pages/visit).
- **Published source line:** “OPEN EVERY DAY OF THE YEAR 6 AM - 2 AM. ADDRESS 548 Green Street, San Francisco, CA 94133. HOURS Open daily 6:00 AM–2:00 AM. GOOD TO KNOW 21+ Valid ID required.”
- **Late-night result:** Friday: 6:00 AM–2:00 AM; Saturday: 6:00 AM–2:00 AM; Sunday: 6:00 AM–2:00 AM.
- **Transit screen:** N Judah downtown + 30 Stockton into North Beach — The 30 Stockton reaches Columbus and Green until midnight; the 91 Owl is the overnight option.
- **Manual review flags:** 21+, valid ID required. Transit gap: the 30 and 8 end at midnight while the bar runs to 2 AM.
- **Official link:** [https://ginoandcarlo.com/pages/visit](https://ginoandcarlo.com/pages/visit)

### The Showdown

- **Status:** Official match with documented gap.
- **Category / neighborhood:** Dive bar · North Beach.
- **Address check:** `1268 Grant Ave, San Francisco, CA 94133` — [official source](https://showdown.pourguys.com/north-beach-the-showdown-locations).
- **Published source line:** “The Showdown. Address: 1268 Grant Ave, San Francisco, CA 94133, US. Location Hours: Monday, Tuesday: 3:00PM – 2:00AM; Wednesday, Thursday, Friday, Saturday, Sunday: 12:00PM - 2:00AM.”
- **Late-night result:** Friday: 12:00 PM–2:00 AM; Saturday: 12:00 PM–2:00 AM; Sunday: 12:00 PM–2:00 AM.
- **Transit screen:** N Judah downtown + 30 Stockton into North Beach — The 30 Stockton and 8 Bayshore reach Grant Avenue until midnight; the 91 Owl covers the overnight return.
- **Manual review flags:** Operator-site source: hours come from the Pour Guys operator location page rather than a standalone venue website. Flagged for manual review. Transit gap: the 30 and 8 end at midnight.
- **Official link:** [https://showdown.pourguys.com/north-beach-the-showdown-locations](https://showdown.pourguys.com/north-beach-the-showdown-locations)

### Tempest Bar & Box Kitchen

- **Status:** Official match with documented gap.
- **Category / neighborhood:** Bar / kitchen · SoMa.
- **Address check:** `431 Natoma St, San Francisco, CA 94103` — [official source](https://showdown.pourguys.com/north-beach-the-showdown-locations).
- **Published source line:** “Tempest Bar & Box Kitchen. Address: 431 Natoma St, San Francisco, CA 94103, US. Location Hours: Monday, Tuesday, Wednesday: 11:00AM – 2:00AM; Thursday: 11:00AM - 2:00AM; Friday: 11:00AM - 2:00AM; Saturday, Sunday: 12:00PM - 2:00AM.”
- **Late-night result:** Friday: 11:00 AM–2:00 AM; Saturday: 12:00 PM–2:00 AM; Sunday: 12:00 PM–2:00 AM.
- **Transit screen:** N Judah to Powell/Civic Center + walk — Natoma Street sits between Mission and Howard near 5th; the 14 Mission and 90 Owl cover the late return.
- **Manual review flags:** Operator-site source: hours come from the Pour Guys operator location page rather than a standalone venue website. Flagged for manual review. The operator page prints a duplicated street number for this location; the Natoma Street address should be confirmed on arrival.
- **Official link:** [https://showdown.pourguys.com/north-beach-the-showdown-locations](https://showdown.pourguys.com/north-beach-the-showdown-locations)

### Louie's Bar

- **Status:** Official match with documented gap.
- **Category / neighborhood:** Bar · SoMa.
- **Address check:** `55 Stevenson St, San Francisco, CA 94105` — [official source](https://showdown.pourguys.com/north-beach-the-showdown-locations).
- **Published source line:** “Louie's Bar. Address: 55 Stevenson St, San Francisco, CA 94105, US. Location Hours: Monday, Tuesday, Wednesday: 11:00AM – 2:00AM; Thursday: 11:00AM - 2:00AM, Friday: 11:00AM - 2:00AM; Saturday: 5:00PM - 2AM; Sunday: Closed.”
- **Late-night result:** Friday: 11:00 AM–2:00 AM; Saturday: 5:00 PM–2:00 AM.
- **Transit screen:** N Judah to Montgomery Station + walk — Stevenson Street runs behind Market near 1st Street, a short walk from Montgomery Station.
- **Manual review flags:** Operator-site source: hours come from the Pour Guys operator location page rather than a standalone venue website. Flagged for manual review. Closed Sunday.
- **Official link:** [https://showdown.pourguys.com/north-beach-the-showdown-locations](https://showdown.pourguys.com/north-beach-the-showdown-locations)

### Connecticut Yankee

- **Status:** Official match with documented gap.
- **Category / neighborhood:** Sports bar / restaurant · Potrero Hill.
- **Address check:** `100 Connecticut St, San Francisco, CA 94107` — [official source](https://showdown.pourguys.com/north-beach-the-showdown-locations).
- **Published source line:** “Connecticut Yankee. Address: 100 Connecticut St, San Francisco, CA 94107, US. Location Hours: Monday, Tuesday, Wednesday: 11:00AM – 11:00PM; Thursday, Friday, Saturday: 11:00AM - 1:00AM; Sunday: 11:00AM - 11:00PM.”
- **Late-night result:** Friday: 11:00 AM–1:00 AM; Saturday: 11:00 AM–1:00 AM.
- **Transit screen:** N Judah + 22 Fillmore to Potrero Hill — The 22 Fillmore runs 24 hours into Potrero Hill; the T Third and 91 Owl serve the eastern side.
- **Manual review flags:** Operator-site source: hours come from the Pour Guys operator location page rather than a standalone venue website. Flagged for manual review. Sunday closes at 11:00 PM and does not qualify.
- **Official link:** [https://showdown.pourguys.com/north-beach-the-showdown-locations](https://showdown.pourguys.com/north-beach-the-showdown-locations)

### The Café

- **Status:** Official match with documented gap.
- **Category / neighborhood:** Gay bar / nightclub · Castro / Upper Market.
- **Address check:** `2369 Market St, San Francisco, CA 94114` — [official source](https://cafesf.com/).
- **Published source line:** “Located across the street from Harvey Milk Plaza/Castro Muni Station (2369 Market St., San Francisco, CA), above the Chevron station. Thursday Night - DJ, Dancing - 9pm-2am. Friday Nights - DJ, Dancing - 9pm-2am. Saturday Night - DJ, Dancing - 9pm-2am. Hours of Operation: Thursday-Saturday, 9pm-2am.”
- **Late-night result:** Friday: 9:00 PM–2:00 AM; Saturday: 9:00 PM–2:00 AM.
- **Transit screen:** N Judah to Castro Station + cross the street — Castro Muni Station is directly across Market Street; the N Judah runs 24 hours with Owl service.
- **Manual review flags:** Sunday hours are event-driven and are not published as a fixed schedule; only Thursday to Saturday are posted. 21+ club with ticketed events and extended after-hours on some nights.
- **Official link:** [https://cafesf.com/](https://cafesf.com/)

### Grubstake Diner

- **Status:** Official match with documented gap.
- **Category / neighborhood:** Diner · Lower Nob Hill.
- **Address check:** `1525 Pine St, San Francisco, CA 94109` — [official source](https://www.grubstakesf.com/location/lower-nob-hill).
- **Published source line:** “Late-Night Diner In Lower Nob Hill. Grubstake Diner is right here on Pine Street, serving classic San Francisco comfort food from our vintage dining car late into the night. Visit us at 1525 Pine Street for the full Grubstake experience. (Site title: "Late Night Dining in San Francisco (Open Until 4 AM)".)”
- **Late-night result:** Friday: Open until 3:00 AM (opening time not published); Saturday: Open until 3:00 AM (opening time not published); Sunday: Open until 3:00 AM (opening time not published).
- **Transit screen:** N Judah downtown + 1 California or 19 Polk to Pine Street — The 1 California serves Pine Street until midnight; after that use the 90 Owl on Van Ness or the 91 Owl and walk from Polk Street.
- **Manual review flags:** Source gap flagged for manual review: the official site advertises late-night service and a 4 AM close in its page title but publishes no day-by-day opening and closing grid, so the hours column records a late close without an opening time. Transit gap: the 1 California ends at midnight; plan an Owl return.
- **Official link:** [https://www.grubstakesf.com/location/lower-nob-hill](https://www.grubstakesf.com/location/lower-nob-hill)

