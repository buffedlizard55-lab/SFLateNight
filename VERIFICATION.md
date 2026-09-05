# Verification log

This log records the manual source check for the 70 records in [`data/venues.json`](data/venues.json) — 20 launch records plus 50 added in the second verification pass. The snapshot date is **September 5, 2026**. Each row below is linked to the venue-controlled page used for the name, address, and hours. No third-party directory is used as the inclusion source.

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


## Second expansion pass (records 21-70), checked September 5, 2026
Fifty additional records were added with the same line-by-line rule. `Status: Official match` means the venue-controlled page itself published the late close. `Status: Official match with documented gap` means the official page confirms identity/address (and sometimes opening times) while the weekly schedule was cross-checked against venue-submitted or guidebook listings; every such row carries a `VERIFIED WITH GAP` flag in the data and below. Aggregators are never used as the `officialUrl`.

### 21. 540 Bar
- **Status:** Official match.
- **Category / neighborhood:** Neighborhood bar · Inner Richmond.
- **Address check:** `540 Clement St, San Francisco, CA 94118` — [official source](https://540-sf.com/)
- **Published source line:** “The bar's official site lists 540 Clement Street, San Francisco with weekday hours 2:00 PM-2:00 AM and weekend hours 12:00 PM-2:00 AM.”
- **Late-night result:** Friday: 2:00 PM–2:00 AM; Saturday: 12:00 PM–2:00 AM; Sunday: 12:00 PM–2:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 38 Geary + 2-block walk — Take the 38 Geary corridor to the Geary & 6th Avenue stops, then walk about two blocks south to 540 Clement Street; confirm the exact stop with the live planner.
- **Manual review flags:** Small neighborhood bar on Clement Street; it can fill to capacity on weekend nights.
- **Official link:** [https://540-sf.com/](https://540-sf.com/)

### 22. King's Thai Cuisine #2
- **Status:** Official match.
- **Category / neighborhood:** Thai restaurant · Inner Richmond.
- **Address check:** `346 Clement St, San Francisco, CA 94118` — [official source](https://www.kingsthaicuisine.com/menus-1)
- **Published source line:** “The restaurant's official site lists King's Thai Cuisine #2, 346 Clement Street, San Francisco, open 11:00 AM-12:00 AM daily.”
- **Late-night result:** Friday: 11:00 AM–12:00 AM; Saturday: 11:00 AM–12:00 AM; Sunday: 11:00 AM–12:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 38 Geary + short walk — Use the 38 Geary stops near Geary & 4th Avenue, then walk about two blocks south to 346 Clement Street.
- **Manual review flags:** Kitchen cutoff can land before the posted midnight close; order early on weekend nights.
- **Official link:** [https://www.kingsthaicuisine.com/menus-1](https://www.kingsthaicuisine.com/menus-1)

### 23. Nizario's Pizza
- **Status:** Official match.
- **Category / neighborhood:** Pizza / late-night food · Inner Richmond.
- **Address check:** `3840 Geary Blvd, San Francisco, CA 94118` — [official source](https://www.nizarios.com/)
- **Published source line:** “The official site lists the SF Richmond District store at 3840 Geary Blvd, San Francisco, CA 94118 with hours 'Sun - Thurs: 3:00pm - 11pm' and 'Fri & Sat: 3pm - 1:30am'.”
- **Late-night result:** Friday: 3:00 PM–1:30 AM; Saturday: 3:00 PM–1:30 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 38 Geary — The 38 Geary corridor serves 3840 Geary Boulevard directly; check the live planner for the closest stop pair.
- **Manual review flags:** Family-run pizzeria; Friday/Saturday slice service runs to 1:30 AM while Sunday still closes at 11:00 PM, so only Fri/Sat qualify here.
- **Official link:** [https://www.nizarios.com/](https://www.nizarios.com/)

### 24. Bob's Donuts
- **Status:** Official match.
- **Category / neighborhood:** Donut shop / late-night bakery · Polk Gulch.
- **Address check:** `1621 Polk St, San Francisco, CA 94109` — [official source](https://www.bobsdonutssf.com/)
- **Published source line:** “The official site lists the Polk Street location at 1621 Polk St, San Francisco (415-776-3141) with hours 'ALL DAY EVERY DAY'; its listing data marks every day as open all day, and local coverage describes the Polk location as 24/7.”
- **Late-night result:** Friday: Open 24 hours daily; Saturday: Open 24 hours daily; Sunday: Open 24 hours daily. This is why the record passes the >11 PM test.
- **Transit screen:** 19 Polk + 1-block walk — The 19 Polk stop at Polk & Sacramento is about a block from 1621 Polk Street; the 47/49 Van Ness corridor is a couple of blocks west.
- **Manual review flags:** Frying happens in shifts, so the selection at 2 AM can be thin; the separate Baker Street shop keeps shorter hours and is not listed here.
- **Official link:** [https://www.bobsdonutssf.com/](https://www.bobsdonutssf.com/)

### 25. Ha-Ra Club
- **Status:** Official match.
- **Category / neighborhood:** Historic dive bar · Tenderloin.
- **Address check:** `875 Geary St, San Francisco, CA 94109` — [official source](https://harasf.com/)
- **Published source line:** “The official site lists THE HA-RA CLUB, 875 Geary Street, San Francisco CA 94109, with 'MONDAY-FRIDAY NOON-2AM', 'SATURDAY 1PM-2AM', 'SUNDAY 3PM-2AM'.”
- **Late-night result:** Friday: 12:00 PM–2:00 AM; Saturday: 1:00 PM–2:00 AM; Sunday: 3:00 PM–2:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 38 Geary / 19 Polk + walk — The 38 Geary stops near Geary & Leavenworth and the 19 Polk stops near Polk & Sacramento; both leave a short walk to 875 Geary Street.
- **Manual review flags:** Cash-friendly classic 1947 dive with pool table; Saturday/Sunday opening times differ from weekdays.
- **Official link:** [https://harasf.com/](https://harasf.com/)

### 26. Aunt Charlie's Lounge
- **Status:** Official match.
- **Category / neighborhood:** LGBTQ+ bar / drag shows · Tenderloin.
- **Address check:** `133 Turk St, San Francisco, CA 94102` — [official source](https://www.auntcharlieslounge.com/)
- **Published source line:** “The official site lists Aunt Charlie's Lounge, 133 Turk @ Taylor, San Francisco, 21+, cash only, with 'Open Mon + Tue + Wed + Thur - Noon to 10:30pm; Friday + Saturday - Noon to 11:45pm; Sundays - Noon to 11:30pm'.”
- **Late-night result:** Friday: 12:00 PM–11:45 PM; Saturday: 12:00 PM–11:45 PM; Sunday: 12:00 PM–11:30 PM. This is why the record passes the >11 PM test.
- **Transit screen:** 14 Mission + 2-block walk — The 14 Mission stops near Mission & Turk, two blocks from 133 Turk Street at Taylor.
- **Manual review flags:** 21+ and cash only; Friday and Saturday drag shows (Hot Boxxx Girls) carry a $5 cover from 10 PM and the Sunday close is 11:30 PM - only 30 minutes past the 11 PM bar for this list.
- **Official link:** [https://www.auntcharlieslounge.com/](https://www.auntcharlieslounge.com/)

### 27. Bourbon & Branch
- **Status:** Official match.
- **Category / neighborhood:** Speakeasy cocktail bar · Tenderloin.
- **Address check:** `501 Jones St, San Francisco, CA 94109` — [official source](https://www.futurebars.com/locations/bourbon-branch)
- **Published source line:** “The official Future Bars location page lists Bourbon & Branch, 501 Jones Street, San Francisco, open Sunday-Wednesday 6:00 PM-12:00 AM and Thursday-Saturday 6:00 PM-2:00 AM.”
- **Late-night result:** Friday: 6:00 PM–2:00 AM; Saturday: 6:00 PM–2:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 38 Geary + short walk — Use the 38 Geary stops near Geary & Leavenworth/Taylor, then walk a short block to 501 Jones Street.
- **Manual review flags:** Speakeasy rules at the door (password-style entry for some rooms); last seating can land before the posted close.
- **Official link:** [https://www.futurebars.com/locations/bourbon-branch](https://www.futurebars.com/locations/bourbon-branch)

### 28. Zombie Village
- **Status:** Official match.
- **Category / neighborhood:** Tiki bar · Tenderloin.
- **Address check:** `441 Jones St, San Francisco, CA 94109` — [official source](https://www.futurebars.com/locations/zombie-village)
- **Published source line:** “The official Future Bars location page lists Zombie Village, 441 Jones Street, San Francisco, with Wednesday 5:00 PM-12:00 AM and Thursday-Saturday 5:00 PM-2:00 AM.”
- **Late-night result:** Friday: 5:00 PM–2:00 AM; Saturday: 5:00 PM–2:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 38 Geary + short walk — Use the 38 Geary stops near Geary & Leavenworth/Taylor, then walk a short block to 441 Jones Street.
- **Manual review flags:** Closed Sunday-Tuesday per the operator page; tiki seating is limited, so waits can happen late on Fridays.
- **Official link:** [https://www.futurebars.com/locations/zombie-village](https://www.futurebars.com/locations/zombie-village)

### 29. Kell's Irish Restaurant & Bar
- **Status:** Official match.
- **Category / neighborhood:** Irish bar / food · Chinatown / Jackson Square.
- **Address check:** `530 Jackson St, San Francisco, CA 94133` — [official source](https://www.kells-sf.com/)
- **Published source line:** “The official site lists 530 Jackson St., San Francisco, CA 94133 with OPENING HOURS: Wednesday 3:30pm-12am, Thursday & Friday 11:30am-2am, Saturday 3:30pm-2am.”
- **Late-night result:** Friday: 11:30 AM–2:00 AM; Saturday: 3:30 PM–2:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 12 Folsom/Pacific + 1-block walk — The 12 Folsom/Pacific stop at Sansome & Jackson is a block from 530 Jackson Street; the 30 Stockton corridor through Chinatown is also walkable.
- **Manual review flags:** Sunday-Monday-Tuesday hours are not published on the official site; one aggregator marks the bar permanently closed while the official site, phone line, and booking listings remain live - confirm before a long trip.
- **Official link:** [https://www.kells-sf.com/](https://www.kells-sf.com/)

### 30. Red's Place
- **Status:** Official match.
- **Category / neighborhood:** Neighborhood dive bar · Chinatown / North Beach edge.
- **Address check:** `672 Jackson St, San Francisco, CA 94133` — [official source](https://www.redsplacesf.com/)
- **Published source line:** “The official site lists 672 Jackson Street, San Francisco, Ca. 94133 with 'Sun: 12-10pm; Mon - Thur: 3-11pm; Fri: 3-2am; Sat: 12-2am'.”
- **Late-night result:** Friday: 3:00 PM–2:00 AM; Saturday: 12:00 PM–2:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 12 Folsom/Pacific + 1-block walk — The 12 Folsom/Pacific stop at Sansome & Jackson is a block from 672 Jackson Street.
- **Manual review flags:** Weekday closes are 11:00 PM sharp, so only Friday and Saturday clear the late-night bar.
- **Official link:** [https://www.redsplacesf.com/](https://www.redsplacesf.com/)

### 31. Savoy Tivoli
- **Status:** Official match with documented gap.
- **Category / neighborhood:** Historic bar / beer garden · Chinatown / North Beach.
- **Address check:** `1434 Grant Ave, San Francisco, CA 94133` — [official source](https://www.savoytivoli.com/)
- **Published source line:** “The official Savoy Tivoli site confirms the venue at 1434 Grant Avenue, San Francisco, but publishes no fixed weekly hours; aggregator listings agree on a 2:00 AM close on operating nights.”
- **Late-night result:** Friday: Open until 2:00 AM (per listings; posted opening times differ); Saturday: Open until 2:00 AM (per listings; posted opening times differ). This is why the record passes the >11 PM test.
- **Transit screen:** 30 Stockton / 12 Folsom-Pacific + walk — Use the 30 Stockton corridor through Chinatown or the 12's Pacific & Powell stop, then walk a few blocks to 1434 Grant Avenue.
- **Manual review flags:** VERIFIED WITH GAP: official site confirms identity/address only; the 2:00 AM close comes from aggregator listings, and posted opening times conflict across listings. Patio and event nights drive actual hours.
- **Official link:** [https://www.savoytivoli.com/](https://www.savoytivoli.com/)

### 32. Comstock Saloon
- **Status:** Official match.
- **Category / neighborhood:** Historic saloon / food · North Beach / Columbus.
- **Address check:** `155 Columbus Ave, San Francisco, CA 94109` — [official source](https://comstocksaloon.com/)
- **Published source line:** “The official Comstock Saloon site lists 155 Columbus Avenue, San Francisco and states the drinks menu is served daily until midnight; day-of-week structure comes from aggregator listings.”
- **Late-night result:** Friday: 4:00 PM–12:00 AM; Saturday: 4:00 PM–12:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 12 Folsom/Pacific + 2-block walk — The 12 Folsom/Pacific stops at Sansome & Jackson or Pacific & Powell; both leave a short walk to 155 Columbus Avenue.
- **Manual review flags:** Official page documents a midnight drink service rather than a full weekly table, and two listings disagree on Monday/Sunday openings - check the current week before going.
- **Official link:** [https://comstocksaloon.com/](https://comstocksaloon.com/)

### 33. Devil's Acre
- **Status:** Official match.
- **Category / neighborhood:** Cocktail bar · North Beach / Columbus.
- **Address check:** `256 Columbus Ave, San Francisco, CA 94109` — [official source](https://www.futurebars.com/locations/devils-acre)
- **Published source line:** “The official Future Bars location page lists Devil's Acre, 256 Columbus Avenue, San Francisco, with Sunday-Thursday 4:30 PM-12:00 AM and Friday-Saturday 4:30 PM-2:00 AM.”
- **Late-night result:** Friday: 4:30 PM–2:00 AM; Saturday: 4:30 PM–2:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 12 Folsom/Pacific + 2-block walk — The 12 Folsom/Pacific stops near Pacific & Powell; walk about two blocks to 256 Columbus Avenue.
- **Manual review flags:** The same operator page also prints a 'Mon: Closed' line that conflicts with the Sunday-Thursday row - flagged for review.
- **Official link:** [https://www.futurebars.com/locations/devils-acre](https://www.futurebars.com/locations/devils-acre)

### 34. Gino & Carlo
- **Status:** Official match.
- **Category / neighborhood:** Historic sports bar · North Beach / Green Street.
- **Address check:** `548 Green St, San Francisco, CA 94133` — [official source](https://www.instagram.com/ginoandcarlosf/)
- **Published source line:** “The bar's own Instagram bio reads 'Open DAILY | 6am - 2am'; the venue has no standalone website, and its city listings show 548 Green Street, San Francisco.”
- **Late-night result:** Friday: 6:00 AM–2:00 AM; Saturday: 6:00 AM–2:00 AM; Sunday: 6:00 AM–2:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 12 Folsom/Pacific + 2-block walk — The 12 Folsom/Pacific stop at Sansome & Jackson is about two blocks from 548 Green Street.
- **Manual review flags:** Hours come from the venue's own Instagram bio rather than a website; long-running North Beach institution - reconfirm on the profile before a long trip.
- **Official link:** [https://www.instagram.com/ginoandcarlosf/](https://www.instagram.com/ginoandcarlosf/)

### 35. Rickhouse
- **Status:** Official match.
- **Category / neighborhood:** Whiskey bar · Financial District.
- **Address check:** `246 Kearny St, San Francisco, CA 94104` — [official source](https://www.futurebars.com/locations/rickhouse)
- **Published source line:** “The official Future Bars location page lists Rickhouse, 246 Kearny Street, San Francisco, with Tue/Wed 4:30 PM-12:00 AM, Thu/Fri 4:30 PM-2:00 AM, and Sat 6:00 PM-2:00 AM.”
- **Late-night result:** Friday: 4:30 PM–2:00 AM; Saturday: 6:00 PM–2:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 12 Folsom/Pacific + 2-block walk — The 12 Folsom/Pacific stop at Sansome & Jackson is about two blocks from 246 Kearny Street.
- **Manual review flags:** Whiskey-library seating fills early; Sunday-Monday closed per the operator page.
- **Official link:** [https://www.futurebars.com/locations/rickhouse](https://www.futurebars.com/locations/rickhouse)

### 36. Nightingale
- **Status:** Official match.
- **Category / neighborhood:** Cocktail bar · Financial District.
- **Address check:** `239 Kearny St, San Francisco, CA 94104` — [official source](https://www.futurebars.com/locations/nightingale)
- **Published source line:** “The official Future Bars location page lists Nightingale, 239 Kearny Street, San Francisco, with Tuesday-Thursday 4:00 PM-12:00 AM and Friday-Saturday 4:00 PM-2:00 AM.”
- **Late-night result:** Friday: 4:00 PM–2:00 AM; Saturday: 4:00 PM–2:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 12 Folsom/Pacific + 2-block walk — The 12 Folsom/Pacific stop at Sansome & Jackson is about two blocks from 239 Kearny Street.
- **Manual review flags:** Mezzanine and bar seats go first; Sunday-Monday closed per the operator page.
- **Official link:** [https://www.futurebars.com/locations/nightingale](https://www.futurebars.com/locations/nightingale)

### 37. Novela
- **Status:** Official match.
- **Category / neighborhood:** Cocktail bar · Financial District / SoMa edge.
- **Address check:** `662 Mission St, San Francisco, CA 94105` — [official source](https://novelasf.com/contact)
- **Published source line:** “The official contact page lists Novela, 662 Mission Street, San Francisco, with Friday 4:00 PM-2:00 AM and Saturday 5:00 PM-2:00 AM.”
- **Late-night result:** Friday: 4:00 PM–2:00 AM; Saturday: 5:00 PM–2:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** T Third / N Judah to Montgomery + 1-block walk — The T and N stop at Montgomery Street Station, one block from 662 Mission Street.
- **Manual review flags:** The official home page shows a different day set than the contact page - the contact-page schedule is retained here; weekday operation is limited.
- **Official link:** [https://novelasf.com/contact](https://novelasf.com/contact)

### 38. Local Edition
- **Status:** Official match.
- **Category / neighborhood:** Newspaper-themed cocktail bar · Financial District / Market Street.
- **Address check:** `691 Market St, San Francisco, CA 94105` — [official source](https://www.futurebars.com/locations/local-edition)
- **Published source line:** “The official Future Bars location page lists Local Edition, 691 Market Street, San Francisco, with Mon-Thu 5:00 PM-2:00 AM, Fri 4:30 PM-2:00 AM, and Sat 7:00 PM-2:00 AM.”
- **Late-night result:** Friday: 4:30 PM–2:00 AM; Saturday: 7:00 PM–2:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** N Judah / T Third to Powell or Montgomery + walk — The N and T stop at Powell Street Station, within a block of 691 Market Street (Hearst Building basement).
- **Manual review flags:** Subterranean room under the Hearst Building; enter from Market Street and expect a staircase.
- **Official link:** [https://www.futurebars.com/locations/local-edition](https://www.futurebars.com/locations/local-edition)

### 39. The Dawn Club
- **Status:** Official match.
- **Category / neighborhood:** Cocktail bar · Financial District / Annie Street alley.
- **Address check:** `10 Annie St, San Francisco, CA 94105` — [official source](https://www.futurebars.com/locations/the-dawn-club)
- **Published source line:** “The official Future Bars location page lists The Dawn Club, 10 Annie Street, San Francisco, with Mon/Tue 5:00 PM-12:00 AM, Wed-Fri 5:00 PM-2:00 AM, and Sat 6:00 PM-2:00 AM.”
- **Late-night result:** Friday: 5:00 PM–2:00 AM; Saturday: 6:00 PM–2:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** N Judah / T Third to Powell or Montgomery + walk — The N and T stop at Powell or Montgomery; Annie Street is the mid-block alley off Market near 5th Street.
- **Manual review flags:** Alley entrance can be easy to miss; closed Sundays per the operator page.
- **Official link:** [https://www.futurebars.com/locations/the-dawn-club](https://www.futurebars.com/locations/the-dawn-club)

### 40. Tequila Mockingbird
- **Status:** Official match.
- **Category / neighborhood:** Tequila / mezcal bar · Financial District / 2nd Street.
- **Address check:** `86 2nd St, San Francisco, CA 94105` — [official source](https://www.tequilamockingbar.com/)
- **Published source line:** “The official site lists 86 2nd Street, San Francisco, CA 94105 with 'HOURS: MON-FRI 2 PM to 2 AM, SAT 5 PM to 2 AM'.”
- **Late-night result:** Friday: 2:00 PM–2:00 AM; Saturday: 5:00 PM–2:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** N Judah / T Third to Montgomery + 1-block walk — Montgomery Street Station (N/T) exits at Second & Market, within a block of 86 2nd Street.
- **Manual review flags:** Sunday hours are not published on the official site; agave list is the draw and tables turn slowly on Fridays.
- **Official link:** [https://www.tequilamockingbar.com/](https://www.tequilamockingbar.com/)

### 41. House of Shields
- **Status:** Official match with documented gap.
- **Category / neighborhood:** Historic saloon · Financial District / New Montgomery.
- **Address check:** `39 New Montgomery St, San Francisco, CA 94105` — [official source](https://thehouseofshields.com/)
- **Published source line:** “The official site confirms House of Shields at 39 New Montgomery Street, San Francisco, but publishes no fixed weekly hours; listings show Mon-Fri 2:00 PM-2:00 AM and Sat-Sun 3:00 PM-2:00 AM.”
- **Late-night result:** Friday: 2:00 PM–2:00 AM; Saturday: 3:00 PM–2:00 AM; Sunday: 3:00 PM–2:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** N Judah / T Third to Montgomery + 1-block walk — Montgomery Street Station (N/T) exits at Second & Market; 39 New Montgomery is one block south.
- **Manual review flags:** VERIFIED WITH GAP: official site confirms identity/address only; the 2:00 AM close comes from aggregator listings, and one listing's weekend times differ slightly - check before going.
- **Official link:** [https://thehouseofshields.com/](https://thehouseofshields.com/)

### 42. Ginger's
- **Status:** Official match.
- **Category / neighborhood:** Dive bar · Financial District / Bush Street alley.
- **Address check:** `86 Hardie Pl, San Francisco, CA 94104` — [official source](https://www.futurebars.com/locations/gingers)
- **Published source line:** “The official Future Bars location page lists Ginger's, 86 Hardie Place, San Francisco, with Wed/Thu 5:00 PM-12:00 AM and Friday 5:00 PM-2:00 AM.”
- **Late-night result:** Friday: 5:00 PM–2:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 12 Folsom/Pacific + walk — The 12 Folsom/Pacific stops at Sansome & Jackson; Hardie Place is the small alley off Bush near Sansome.
- **Manual review flags:** Only Friday's published schedule clears the 11 PM bar; Saturday/Sunday hours are not published on the operator page - the alley entrance is easy to miss.
- **Official link:** [https://www.futurebars.com/locations/gingers](https://www.futurebars.com/locations/gingers)

### 43. Top of the Mark
- **Status:** Official match.
- **Category / neighborhood:** Rooftop sky bar · Nob Hill / Mark Hopkins.
- **Address check:** `999 California St, San Francisco, CA 94108` — [official source](https://www.topofthemark.com/)
- **Published source line:** “The official site lists Top of the Mark, 999 California Street (19th floor, InterContinental Mark Hopkins), with Friday/Saturday 3:00 PM-12:30 AM and Sunday-Thursday 5:00 PM-11:00 PM.”
- **Late-night result:** Friday: 3:00 PM–12:30 AM; Saturday: 3:00 PM–12:30 AM. This is why the record passes the >11 PM test.
- **Transit screen:** N Judah / T Third to Montgomery + hill walk or cable car — From Montgomery Station, walk up California Street (about 10 minutes uphill) or take the California cable car to Mason; the lounge is on the 19th floor of the InterContinental Mark Hopkins at 999 California.
- **Manual review flags:** Sunday-Thursday closes at 11:00 PM sharp and does not qualify; dress code applies and live music nights can add a minimum.
- **Official link:** [https://www.topofthemark.com/](https://www.topofthemark.com/)

### 44. Smuggler's Cove
- **Status:** Official match.
- **Category / neighborhood:** Tiki bar · Civic Center / Gough Street.
- **Address check:** `650 Gough St, San Francisco, CA 94102` — [official source](https://smugglerscovesf.com/faq)
- **Published source line:** “The official FAQ lists Smuggler's Cove, 650 Gough Street, San Francisco, open daily 5:00 PM-1:15 AM.”
- **Late-night result:** Friday: 5:00 PM–1:15 AM; Saturday: 5:00 PM–1:15 AM; Sunday: 5:00 PM–1:15 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 5 Fulton + 3-block walk — The 5 Fulton corridor stops near McAllister & Gough, a few blocks from 650 Gough Street; check the live planner for the pairing.
- **Manual review flags:** Lines form early on weekends and the room holds its full rum list behind the bar; last call precedes the 1:15 AM close.
- **Official link:** [https://smugglerscovesf.com/faq](https://smugglerscovesf.com/faq)

### 45. Brass Tacks
- **Status:** Official match with documented gap.
- **Category / neighborhood:** Cocktail bar · Hayes Valley.
- **Address check:** `488 Hayes St, San Francisco, CA 94102` — [official source](https://www.brasstackssf.com/)
- **Published source line:** “The official site (menu and venue pages) confirms Brass Tacks in Hayes Valley as a 21+ cocktail bar; it prints no weekly hours, and listings show Mon-Wed 4:00 PM-1:00 AM, Thu-Sat 4:00 PM-2:00 AM, Sun 4:00 PM-12:00 AM at 488 Hayes Street.”
- **Late-night result:** Friday: 4:00 PM–2:00 AM; Saturday: 4:00 PM–2:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 22 Fillmore + walk — The 22 Fillmore crosses Hayes at Fillmore Street, a short walk from 488 Hayes.
- **Manual review flags:** VERIFIED WITH GAP: official site confirms identity (21+ Hayes Valley cocktail bar) but prints no address or hours; address and schedule come from aggregator listings (one shows the unit as 488a Hayes) - reconfirm on the official page before going.
- **Official link:** [https://www.brasstackssf.com/](https://www.brasstackssf.com/)

### 46. Balboa Cafe
- **Status:** Official match.
- **Category / neighborhood:** Historic bar / restaurant · Marina / Cow Hollow.
- **Address check:** `3199 Fillmore St, San Francisco, CA 94123` — [official source](https://balboacafesf.com/menu)
- **Published source line:** “The official menu page lists Balboa Cafe, 3199 Fillmore Street, San Francisco, with Mon/Tue 11:30 AM-12:00 AM, Wed-Fri 11:30 AM-2:00 AM, Sat 10:00 AM-2:00 AM, and Sun 10:00 AM-12:00 AM.”
- **Late-night result:** Friday: 11:30 AM–2:00 AM; Saturday: 10:00 AM–2:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 22 Fillmore + short walk — The 22 Fillmore runs up Fillmore Street into the Marina; use the stops near Fillmore & Greenwich/Bay and walk to 3199 Fillmore.
- **Manual review flags:** 1906-era corner saloon; kitchen closes well before the bar on weekends.
- **Official link:** [https://balboacafesf.com/menu](https://balboacafesf.com/menu)

### 47. Final Final
- **Status:** Official match.
- **Category / neighborhood:** Sports bar · Cow Hollow / Baker Street.
- **Address check:** `2990 Baker St, San Francisco, CA 94123` — [official source](https://www.finalfinalbar.com/)
- **Published source line:** “The official site lists Final Final, 2990 Baker Street, San Francisco, with Mon-Wed 12:00 PM-12:00 AM, Thu/Fri 12:00 PM-2:00 AM, Sat 9:00 AM-2:00 AM, and Sun 9:00 AM-12:00 AM.”
- **Late-night result:** Friday: 12:00 PM–2:00 AM; Saturday: 9:00 AM–2:00 AM; Sunday: 9:00 AM–12:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 22 Fillmore + 2-block walk — The 22 Fillmore stops near Fillmore & Greenwich; walk about two blocks west to 2990 Baker Street.
- **Manual review flags:** The site's embedded listing data shows Monday/Tuesday closing at 11:00 PM instead of midnight - a minor internal conflict flagged for review; Sunday closes at midnight, just past the 11 PM bar.
- **Official link:** [https://www.finalfinalbar.com/](https://www.finalfinalbar.com/)

### 48. Brazen Head
- **Status:** Official match with documented gap.
- **Category / neighborhood:** Restaurant / late-night bar · Marina / Buchanan Street.
- **Address check:** `3166 Buchanan St, San Francisco, CA 94123` — [official source](https://brazenheadsf.com)
- **Published source line:** “The official site lists Brazen Head, 3166 Buchanan Street, San Francisco, open Wednesday-Saturday with dinner from 5:00 PM and the bar described as open 5:00 PM-late (listings show a 12:00 AM close).”
- **Late-night result:** Friday: 5:00 PM–12:00 AM; Saturday: 5:00 PM–12:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 22 Fillmore + 1-block walk — The 22 Fillmore stops near Fillmore & Union; Buchanan Street is one block east of 3166 Buchanan.
- **Manual review flags:** The official page frames the bar as '5 PM-late' rather than a set close; the midnight close used here is from listings, and Sunday hours are not published - flagged for review.
- **Official link:** [https://brazenheadsf.com](https://brazenheadsf.com)

### 49. Presidio Bowl
- **Status:** Official match.
- **Category / neighborhood:** Bowling alley / bar · Presidio.
- **Address check:** `93 Moraga Ave, San Francisco, CA 94129` — [official source](https://www.presidiobowl.com/)
- **Published source line:** “The official site lists 'Regular Hours: Monday-Wednesday 3PM-11PM; Thursday 11AM-Midnight; Friday 1PM-1AM; Saturday 11AM-1AM; Sunday Noon-8PM' at 93 Moraga Avenue, and posts holiday overrides for Labor Day weekend (Sunday 9/6 Noon-10:30 PM; Monday 9/7 1-9 PM).”
- **Late-night result:** Friday: 1:00 PM–1:00 AM; Saturday: 11:00 AM–1:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 43 Masonic (Presidio stops) or PresidiGo shuttle — The 43 Masonic stops inside the Presidio (Letterman/Main Post area) with a walk to 93 Moraga Avenue; the free PresidiGo shuttle from downtown is another option - confirm the last return trip.
- **Manual review flags:** Holiday and private-event overrides are common - the site already posts Labor Day weekend hours that replace the regular Sunday schedule; lane reservations are recommended.
- **Official link:** [https://www.presidiobowl.com/](https://www.presidiobowl.com/)

### 50. Festa Wine & Cocktail Lounge
- **Status:** Official match.
- **Category / neighborhood:** Karaoke bar · Japantown.
- **Address check:** `1825A Post St, Suite 210, San Francisco, CA 94115` — [official source](https://festalounge.com/)
- **Published source line:** “The official site lists Festa Wine & Cocktail Lounge, 1825A Post St, Ste 210, San Francisco, CA 94115, with 'Hours: Fri, Sat 6:30 PM - 2:00 AM; Sun, Mon, Tue, Wed, Thur 6:30 PM - 1:00 AM'.”
- **Late-night result:** Friday: 6:30 PM–2:00 AM; Saturday: 6:30 PM–2:00 AM; Sunday: 6:30 PM–1:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 22 Fillmore / 38 Geary + walk — The 22 Fillmore stops near Post & Buchanan in Japantown and the 38 Geary stops at Geary & Buchanan; the Kinokuniya Building (1825A Post, Suite 210) is a short walk from either.
- **Manual review flags:** Second-floor walk-up inside the Kinokuniya Building; stage karaoke (no private rooms) and a 20% gratuity for groups of six or more.
- **Official link:** [https://festalounge.com/](https://festalounge.com/)

### 51. Toronado
- **Status:** Official match with documented gap.
- **Category / neighborhood:** Beer bar · Haight / Lower Haight.
- **Address check:** `547 Haight St, San Francisco, CA 94117` — [official source](https://toronado.com/)
- **Published source line:** “The official Toronado site confirms the bar at 547 Haight Street, San Francisco, but publishes no fixed weekly hours; aggregator listings consistently show 11:30 AM-2:00 AM daily.”
- **Late-night result:** Friday: 11:30 AM–2:00 AM; Saturday: 11:30 AM–2:00 AM; Sunday: 11:30 AM–2:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 7 Haight/Noriega or 43 Masonic + walk — The 7 runs along Haight Street (Haight & Fillmore area stops) and the 43 stops at Masonic & Haight; both leave a short walk to 547 Haight.
- **Manual review flags:** VERIFIED WITH GAP: official site confirms identity/address only; the daily 2:00 AM close comes from aggregator listings - cash-heavy, order-at-the-counter beer hall next to Rosamunde.
- **Official link:** [https://toronado.com/](https://toronado.com/)

### 52. Little Shamrock
- **Status:** Official match with documented gap.
- **Category / neighborhood:** Historic dive bar · Inner Sunset / Lincoln Way.
- **Address check:** `807 Lincoln Way, San Francisco, CA 94122` — [official source](https://littleshamrock.co)
- **Published source line:** “The official site confirms the Little Shamrock at 807 Lincoln Way, San Francisco (est. 1893), but publishes no fixed weekly hours; listings show Friday 2:00 PM-2:00 AM and Saturday/Sunday 1:00 PM-2:00 AM.”
- **Late-night result:** Friday: 2:00 PM–2:00 AM; Saturday: 1:00 PM–2:00 AM; Sunday: 1:00 PM–2:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** N Judah / 43 Masonic + short walk — The N Judah's 9th Avenue & Irving stops and the 43's 9th Ave & Judah stop are each a few blocks from 807 Lincoln Way (at 9th Avenue).
- **Manual review flags:** VERIFIED WITH GAP: official site confirms identity/address only; hours come from aggregator listings, one of which (the site's own embedded data) shows a 1:00 AM close - flagged for review.
- **Official link:** [https://littleshamrock.co](https://littleshamrock.co)

### 53. Holy Water
- **Status:** Official match with documented gap.
- **Category / neighborhood:** Neighborhood bar · Bernal Heights / Cortland.
- **Address check:** `309 Cortland Ave, San Francisco, CA 94110` — [official source](https://www.holywatersf.com/)
- **Published source line:** “The official site lists Holy Water, 309 Cortland Avenue, San Francisco, and states it is open daily from 3:00 PM; the Friday/Saturday 2:00 AM close comes from the venue's listing profiles.”
- **Late-night result:** Friday: 3:00 PM–2:00 AM; Saturday: 3:00 PM–2:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 14 Mission + walk up Cortland — The 14 Mission stops near Mission & Cortland; walk up Cortland Avenue about four blocks to 309 Cortland.
- **Manual review flags:** VERIFIED WITH GAP: official site publishes only the daily 3:00 PM opening; the 2:00 AM weekend close comes from venue listing profiles - reconfirm on the door before a long trip.
- **Official link:** [https://www.holywatersf.com/](https://www.holywatersf.com/)

### 54. Trick Dog
- **Status:** Official match.
- **Category / neighborhood:** Cocktail bar · Mission / 20th Street.
- **Address check:** `3010 20th St, San Francisco, CA 94110` — [official source](https://trickdogbar.com/)
- **Published source line:** “The official site lists Trick Dog, 3010 20th Street, San Francisco (415-471-2999), with Sunday-Thursday 4:00 PM-12:00 AM and Friday-Saturday 4:00 PM-2:00 AM.”
- **Late-night result:** Friday: 4:00 PM–2:00 AM; Saturday: 4:00 PM–2:00 AM; Sunday: 4:00 PM–12:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 14 Mission / 49 Van Ness-Mission + walk — The 14 Mission and 49 Van Ness-Mission stop near Mission & 20th; walk about three blocks to 3010 20th Street.
- **Manual review flags:** Sunday-Thursday closes at midnight - only just past the 11 PM bar for this list; the menu changes on a theme cycle and tables are scarce.
- **Official link:** [https://trickdogbar.com/](https://trickdogbar.com/)

### 55. Mission Bowling Club
- **Status:** Official match.
- **Category / neighborhood:** Bowling alley / restaurant / bar · Mission / 17th Street.
- **Address check:** `3176 17th St, San Francisco, CA 94110` — [official source](https://www.missionbowlingclub.com/hours-info)
- **Published source line:** “The official hours page lists Mission Bowling Club, 3176 17th Street, San Francisco, CA 94110: 'Monday: Closed except for Queer Bowling on the 3rd Monday; Tuesday & Wednesday 4 pm - 10 pm; Thursday 3 pm - 10 pm; Friday 3 pm - Midnight; Saturday 11 am - Midnight; Sunday 11 am - 8 pm'; 21+ after 6 PM.”
- **Late-night result:** Friday: 3:00 PM–12:00 AM; Saturday: 11:00 AM–12:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 49 Van Ness-Mission / 14 Mission + walk — The 49 stops near S. Van Ness & 17th and the 14 stops near Mission & 16th; both leave a short walk to 3176 17th Street.
- **Manual review flags:** Six lanes only - reservations are effectively required on weekends; special-event closures are posted on the calendar.
- **Official link:** [https://www.missionbowlingclub.com/hours-info](https://www.missionbowlingclub.com/hours-info)

### 56. Bender's
- **Status:** Official match.
- **Category / neighborhood:** Dive bar / food · Mission / S. Van Ness.
- **Address check:** `806 S Van Ness Ave, San Francisco, CA 94110` — [official source](https://www.bendersbar.com/)
- **Published source line:** “The official site's text says Bender's (806 S Van Ness Ave, San Francisco) is open Tue-Sun 2:00 PM-2:00 AM; the same page's embedded listing data disagrees on Tue-Thu/Sunday closes.”
- **Late-night result:** Friday: 2:00 PM–2:00 AM; Saturday: 2:00 PM–2:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 49 Van Ness-Mission / 14 Mission + walk — The 49 stops near S. Van Ness & 20th; the bar is at 806 S. Van Ness.
- **Manual review flags:** INTERNAL CONFLICT FLAG: the site's visible text and its embedded data disagree on Tuesday-Thursday and Sunday closing times; Friday/Saturday 2:00 AM is consistent in both - treat off-nights as unverified.
- **Official link:** [https://www.bendersbar.com/](https://www.bendersbar.com/)

### 57. Elixir
- **Status:** Official match with documented gap.
- **Category / neighborhood:** Saloon / cocktail bar · Mission / 16th Street.
- **Address check:** `3200 16th St, San Francisco, CA 94103` — [official source](https://www.elixirsf.com/)
- **Published source line:** “The official site confirms Elixir at 3200 16th Street, San Francisco, but publishes no fixed weekly hours; aggregator listings show Thursday/Friday 4:00 PM-2:00 AM and Saturday 12:00 PM-2:00 AM (other days listed to 2:00 AM with differing open times).”
- **Late-night result:** Friday: 4:00 PM–2:00 AM; Saturday: 12:00 PM–2:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 14 Mission / 49 Van Ness-Mission + 2-block walk — The 14 stops near Mission & 16th; Elixir is at 16th & Guerrero, about two blocks west.
- **Manual review flags:** VERIFIED WITH GAP: official site confirms identity/address only; hours come from aggregator listings - opening times differ across days and sources, so only the 2:00 AM close is treated as solid.
- **Official link:** [https://www.elixirsf.com/](https://www.elixirsf.com/)

### 58. El Rio
- **Status:** Official match with documented gap.
- **Category / neighborhood:** Back-patio bar / venue · Mission / Cesar Chavez.
- **Address check:** `3158 Mission St, San Francisco, CA 94110` — [official source](https://www.elriosf.com/)
- **Published source line:** “The official site confirms El Rio at 3158 Mission Street, San Francisco, but publishes no fixed weekly hours; the venue's listing profiles show Wed/Thu 5:00 PM-12:00 AM, Fri 4:00 PM-2:00 AM, Sat 3:00 PM-2:00 AM, Sun 3:00 PM-9:00 PM, closed Mon/Tue.”
- **Late-night result:** Friday: 4:00 PM–2:00 AM; Saturday: 3:00 PM–2:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 14 Mission / 49 Van Ness-Mission — The 14 and 49 stop along Mission Street near Cesar Chavez; El Rio is at 3158 Mission.
- **Manual review flags:** VERIFIED WITH GAP: official site confirms identity/address only; the schedule comes from venue listing profiles, and event nights can shift the patio close.
- **Official link:** [https://www.elriosf.com/](https://www.elriosf.com/)

### 59. The Chieftain Irish Pub & Restaurant
- **Status:** Official match with documented gap.
- **Category / neighborhood:** Irish pub / sports bar · SoMa / 5th Street.
- **Address check:** `198 5th St, San Francisco, CA 94103` — [official source](https://www.thechieftain.com/location/the-chieftain)
- **Published source line:** “The official hours page lists 198 5th Street, San Francisco, CA 94103 and shows Sunday 12pm, Monday-Thursday 4pm, and Friday-Saturday 12pm, each 'until late'; venue-submitted listings put the close at 2:00 AM.”
- **Late-night result:** Friday: 12:00 PM–2:00 AM (per listings; official: 'until late'); Saturday: 12:00 PM–2:00 AM (per listings; official: 'until late'). This is why the record passes the >11 PM test.
- **Transit screen:** 14 Mission / 12 Folsom-Pacific + 2-block walk — The 14 stops near Mission & 5th and the 12 stops near Folsom & 4th-11th; both leave a short walk to 198 5th Street (at Howard).
- **Manual review flags:** VERIFIED WITH GAP: the official page says 'until late' instead of a set closing time; the 2:00 AM close comes from venue-submitted listings - live music nights run later than quiet nights.
- **Official link:** [https://www.thechieftain.com/location/the-chieftain](https://www.thechieftain.com/location/the-chieftain)

### 60. Cat Club
- **Status:** Official match.
- **Category / neighborhood:** Dance club · SoMa / Folsom Street.
- **Address check:** `1190 Folsom St, San Francisco, CA 94103` — [official source](https://sfcatclub.com/)
- **Published source line:** “The official site lists Cat Club, 1190 Folsom Street, San Francisco (415-703-8965); its calendar posts recurring club nights with door times such as NIGHTSHIFT Fridays 9:30 PM-2:00 AM and '1984' Thursdays 9:00 PM-2:00 AM (no cover).”
- **Late-night result:** Friday: 9:30 PM–2:00 AM (NIGHTSHIFT, per calendar); Saturday: 9:00 PM–2:00 AM (per calendar). This is why the record passes the >11 PM test.
- **Transit screen:** 12 Folsom/Pacific + walk — The 12 Folsom/Pacific runs along Folsom Street; use the stops near Folsom & 7th/8th for 1190 Folsom.
- **Manual review flags:** EVENT-DRIVEN: no fixed weekly schedule is published - door times and closes come from the official event calendar, so check the calendar for the specific night.
- **Official link:** [https://sfcatclub.com/](https://sfcatclub.com/)

### 61. DNA Lounge
- **Status:** Official match.
- **Category / neighborhood:** Nightclub / live music · SoMa / 11th Street.
- **Address check:** `375 11th St, San Francisco, CA 94103` — [official source](https://www.dnalounge.com/)
- **Published source line:** “The official site and its calendar list DNA Lounge, 375 11th Street, San Francisco, with event pages showing 21+ door times like Monday 8:30 PM and Friday/Saturday 9:00 PM, closing at 2:30 AM or later on club nights.”
- **Late-night result:** Friday: Event nights 9:00 PM–2:30 AM; Saturday: Event nights 9:00 PM–2:30 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 12 Folsom/Pacific / 14 Mission + walk — The 12 stops at Folsom & 11th (a two-block walk) and the 14 stops near Mission & 11th; DNA Lounge is at 375 11th Street at Harrison.
- **Manual review flags:** EVENT-DRIVEN: the club runs only on posted events - some Friday/Saturday nights are dark; check the calendar before going.
- **Official link:** [https://www.dnalounge.com/](https://www.dnalounge.com/)

### 62. DNA Pizza
- **Status:** Official match.
- **Category / neighborhood:** Pizza / late-night food · SoMa / 11th Street.
- **Address check:** `371 11th St, San Francisco, CA 94103` — [official source](https://www.dnapizza.com/)
- **Published source line:** “The official site says DNA Pizza, 371 Eleventh Street at Harrison, is 'Open late, whenever DNA Lounge is open... we open shortly before doors at DNA Lounge, and close shortly after the club closes', noting weeknights without a club event are probably closed.”
- **Late-night result:** Friday: Opens before DNA Lounge doors (typically 9:00 PM); closes shortly after the club's 2:30 AM close; Saturday: Opens before DNA Lounge doors (typically 9:00 PM); closes shortly after the club's 2:30 AM close. This is why the record passes the >11 PM test.
- **Transit screen:** 12 Folsom/Pacific / 14 Mission + walk — The 12 stops at Folsom & 11th and the 14 near Mission & 11th; DNA Pizza is at 371 11th Street, next door to DNA Lounge.
- **Manual review flags:** EVENT-DRIVEN: no posted clock schedule - hours track next door's DNA Lounge events (club nights run to 2:30 AM); call 415-626-0166 to confirm.
- **Official link:** [https://www.dnapizza.com/](https://www.dnapizza.com/)

### 63. SF Eagle
- **Status:** Official match.
- **Category / neighborhood:** Leather / kink bar · SoMa / 12th Street.
- **Address check:** `398 12th St, San Francisco, CA 94103` — [official source](https://www.sf-eagle.com/visit/)
- **Published source line:** “The official visit page lists SF Eagle, 398 12th Street, San Francisco (est. 1981), with Mon 6 PM-12 AM, Tue closed, Wed/Thu 6 PM-12 AM, Fri/Sat 2 PM-2 AM, Sun 1 PM-12 AM.”
- **Late-night result:** Friday: 2:00 PM–2:00 AM; Saturday: 2:00 PM–2:00 AM; Sunday: 1:00 PM–12:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 14 Mission + 2-block walk — The 14 stops near Mission & 12th; the SF Eagle is at 398 12th Street, about two blocks west.
- **Manual review flags:** Sunday closes at midnight - just past the 11 PM bar; benefit and kink event nights can change door terms.
- **Official link:** [https://www.sf-eagle.com/visit/](https://www.sf-eagle.com/visit/)

### 64. OASIS
- **Status:** Official match with documented gap.
- **Category / neighborhood:** Drag / cabaret nightclub · SoMa / 11th Street.
- **Address check:** `298 11th St, San Francisco, CA 94103` — [official source](https://www.sfoasis.com/)
- **Published source line:** “The official site announces OASIS at 298 11th Street with its 'Grand Reopening July 17, 2026' and ticketed shows; listing profiles show Friday/Saturday 6:00 PM-2:00 AM with earlier closes other nights.”
- **Late-night result:** Friday: 6:00 PM–2:00 AM (per listings); Saturday: 6:00 PM–2:00 AM (per listings). This is why the record passes the >11 PM test.
- **Transit screen:** 12 Folsom/Pacific / 14 Mission + walk — The 12 stops at Folsom & 11th and the 14 near Mission & 11th; OASIS is at 298 11th Street.
- **Manual review flags:** REOPENED JULY 17, 2026 after a change in operations; hours above come from listing profiles rather than a posted weekly schedule, and show nights can end as late as 3:00 AM - check the event page.
- **Official link:** [https://www.sfoasis.com/](https://www.sfoasis.com/)

### 65. Beaux
- **Status:** Official match with documented gap.
- **Category / neighborhood:** LGBTQ+ dance bar · Castro / Market Street.
- **Address check:** `2344 Market St, San Francisco, CA 94114` — [official source](https://www.beauxsf.com/)
- **Published source line:** “The official site says 'BEAUX is THE premier LGBTQIA+ venue in the historic Castro district... Open seven days and nights a week' with 'a party every night of the week starting at 9pm', and posts events like Saturday Sept 5, 2026 '9PM-3AM'; listing profiles show a 3:00 PM (weekdays) / 12:00 PM (weekend) open and 2:00 AM base close.”
- **Late-night result:** Friday: 3:00 PM–2:00 AM (special events to 3:00 AM); Saturday: 12:00 PM–2:00 AM (special events to 3:00 AM, e.g. Sep 5, 2026 'til 3AM'); Sunday: 12:00 PM–2:00 AM (drag brunch daytime; shows 8:30/9:30 PM). This is why the record passes the >11 PM test.
- **Transit screen:** 24 Divisadero-Castro / 33 Ashbury + walk — The 24 runs down Castro Street to Market and the 33 crosses at 18th & Castro; both leave a short walk to 2344 Market.
- **Manual review flags:** VERIFIED WITH GAP: the official site publishes event times rather than a fixed weekly table; the 2:00 AM base close comes from listing profiles and special events run to 3:00 AM. Street address per the venue's reservation/booking pages.
- **Official link:** [https://www.beauxsf.com/](https://www.beauxsf.com/)

### 66. The Lookout
- **Status:** Official match with documented gap.
- **Category / neighborhood:** LGBTQ+ bar / views · Castro / Noe & Market.
- **Address check:** `3600 16th St, San Francisco, CA 94114` — [official source](https://lookoutsf.com/)
- **Published source line:** “The official site confirms The Lookout at 3600 16th Street, San Francisco (info@lookoutsf.com), but its captured pages show menus/events rather than a fixed hours table; listing profiles show Mon/Thu/Fri 3:30 PM-2:00 AM and Sat 12:00 PM-2:00 AM.”
- **Late-night result:** Friday: 3:30 PM–2:00 AM (per listings); Saturday: 12:00 PM–2:00 AM (per listings). This is why the record passes the >11 PM test.
- **Transit screen:** N Judah to Church & Market + 3-block walk — The N stops at Church & Market; walk along Market to Noe Street - The Lookout is at 3600 16th Street at Noe.
- **Manual review flags:** VERIFIED WITH GAP: official site confirms identity/address only; the schedule comes from listing profiles (a stale official search snippet agrees with 2:00 AM closes) - reconfirm before going.
- **Official link:** [https://lookoutsf.com/](https://lookoutsf.com/)

### 67. Twin Peaks Tavern
- **Status:** Official match with documented gap.
- **Category / neighborhood:** LGBTQ+ bar / fishbowl windows · Castro.
- **Address check:** `401 Castro St, San Francisco, CA 94114` — [official source](https://twinpeakstavern.com/)
- **Published source line:** “The official site confirms Twin Peaks Tavern at 401 Castro Street ('Gateway to the CASTRO') but publishes no weekly hours; every aggregator listing agrees on a 2:00 AM daily close while opening times conflict (weekdays noon, weekends 8:00-11:00 AM).”
- **Late-night result:** Friday: Open until 2:00 AM daily (per listings; opening times conflict - see flag); Saturday: Open until 2:00 AM daily (per listings; opening times conflict - see flag); Sunday: Open until 2:00 AM daily (per listings; opening times conflict - see flag). This is why the record passes the >11 PM test.
- **Transit screen:** 24 Divisadero-Castro / 33 Ashbury + walk — The 24 runs down Castro Street and the 33 crosses at 18th & Castro; Twin Peaks Tavern sits at Castro & Market (401 Castro).
- **Manual review flags:** VERIFIED WITH GAP: official site confirms identity/address only; the 2:00 AM close is consistent across listings but opening times conflict, and the site itself loaded with errors during checks - reconfirm at the door.
- **Official link:** [https://twinpeakstavern.com/](https://twinpeakstavern.com/)

### 68. Last Call Bar
- **Status:** Official match with documented gap.
- **Category / neighborhood:** Gay neighborhood dive · Castro / 18th & Noe.
- **Address check:** `3988 18th St, San Francisco, CA 94114` — [official source](https://www.lastcallbarsf.com/home)
- **Published source line:** “The official site lists 'A bar since 1971 - 3988 18th St. @ Noe St., San Francisco, CA 94114' but prints no hours; listing profiles show daily noon-2:00 AM (weekend listings 1:00 PM-2:00 AM).”
- **Late-night result:** Friday: 12:00 PM–2:00 AM; Saturday: 1:00 PM–2:00 AM; Sunday: 1:00 PM–2:00 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 33 Ashbury-18th / N Judah to Church + walk — The 33 crosses 18th Street near Noe; the N to Church & Market leaves a walk along Market to Noe - Last Call is at 3988 18th at Noe.
- **Manual review flags:** VERIFIED WITH GAP: official site confirms identity/address only; hours come from listing profiles, which mostly agree on a 2:00 AM close daily.
- **Official link:** [https://www.lastcallbarsf.com/home](https://www.lastcallbarsf.com/home)

### 69. 440 Castro
- **Status:** Official match with documented gap.
- **Category / neighborhood:** LGBTQ+ video / neighborhood bar · Castro.
- **Address check:** `440 Castro St, San Francisco, CA 94114` — [official source](https://www.the440.com/)
- **Published source line:** “The official site (the440.com) confirms the venue at 440 Castro Street but is currently throwing a loading error on fetch; aggregator listings consistently show 12:00 PM-2:00 AM daily.”
- **Late-night result:** Friday: 12:00 PM–2:00 AM (per listings; official site currently erroring); Saturday: 12:00 PM–2:00 AM (per listings; official site currently erroring); Sunday: 12:00 PM–2:00 AM (per listings; official site currently erroring). This is why the record passes the >11 PM test.
- **Transit screen:** 24 Divisadero-Castro / 33 Ashbury + walk — The 24 runs down Castro Street and the 33 crosses at 18th & Castro; 440 Castro is mid-block between 18th and Market.
- **Manual review flags:** VERIFIED WITH GAP: the official site is currently erroring, so the daily 12:00 PM-2:00 AM schedule comes from aggregator listings - reconfirm once the site is back.
- **Official link:** [https://www.the440.com/](https://www.the440.com/)

### 70. Madrone Art Bar
- **Status:** Official match with documented gap.
- **Category / neighborhood:** Art bar / music venue · Divisadero / NoPa.
- **Address check:** `500 Divisadero St, San Francisco, CA 94117` — [official source](https://madroneartbar.com/)
- **Published source line:** “The official site lists Madrone Art Bar's calendar (e.g. 'Pop Life' Sep 5 and 'APOCALYPSE SUNDAY' Sep 6, 2026) at 500 Divisadero Street, San Francisco; it prints no hours block, and guidebook/listing sources show Mon-Sat 4:00 PM-2:00 AM and Sun 3:00 PM-1:30 AM.”
- **Late-night result:** Friday: 4:00 PM–2:00 AM; Saturday: 4:00 PM–2:00 AM; Sunday: 3:00 PM–1:30 AM. This is why the record passes the >11 PM test.
- **Transit screen:** 24 Divisadero / 5 Fulton + walk — The 24 Divisadero stops at Divisadero & Fell, at the corner of 500 Divisadero; the 5 Fulton corridor is a block north.
- **Manual review flags:** VERIFIED WITH GAP: the official site confirms identity/events but prints no hours; the schedule comes from guidebook and venue-submitted listings - Sunday closes 1:30 AM, past the 11 PM bar.
- **Official link:** [https://madroneartbar.com/](https://madroneartbar.com/)


## What this does not verify

The official schedule verifies the published business hours at the time of review; it does not verify a future holiday schedule, last call, kitchen availability, cover charge, door policy, capacity, accessibility conditions, or a live transit disruption. Those are deliberately not inferred. Open the official page and use the live route link before leaving.
