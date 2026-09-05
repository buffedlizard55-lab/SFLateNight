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
