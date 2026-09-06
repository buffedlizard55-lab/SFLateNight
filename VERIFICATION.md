# Verification log

This log records the manual source check for the 70 records (20 original + 50 added September 5, 2026) in [`data/venues.json`](data/venues.json). The snapshot date is **September 5, 2026**. Each row below is linked to the venue-controlled page used for the name, address, and hours. No third-party directory is used as the inclusion source.

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

## Records 21–70 (added September 5, 2026)

Fifty records were added on the same snapshot date using the same inclusion test. Every record below was checked against a venue-controlled page (the venue’s own site, official location/contact page, or the operator’s official group site). Where a venue publishes only a closing time, a structured business-hours block, or conflicting text, the record is marked **Official match with documented gap** and the gap is spelled out in the flags. Nothing was filled in from review sites or memory.

### Candidates checked and rejected

The following places were researched for this batch and **not** added because their official page publishes no closing time, closes at or before 11 PM on Fri/Sat/Sun, is closed, or has no working official site: Abbey Tavern, Absinthe (10 PM), Alembic (address only), Anina (no close), Aunt Charlie’s (address only), Balboa Cafe (kitchen 10 PM), Beaux (no fixed close), Beretta, Black Cat, Blackthorn (closed), Bourbon & Branch, Brass Tacks, Bus Stop, Cat Club (event-based), Causwells (10:30 PM), The Chieftain (“until late”), Connecticut Yankee sister venue Louie’s (7 PM), Danny Coyle’s, Doc’s Clock, DNA Lounge (event-based), Durty Nelly’s, El Rio, Elixir, Golden Boy Pizza (11 PM), Grubstake (no close), Harry’s Bar, Holy Water (no close), Hot Sauce & Panko (7 PM), The Interval (11 PM), Johnny Foley’s (no daily hours), Kezar Pub, The Knockout, Last Call Bar, Lookout, Maggie McGarry’s, Magnolia Brewing (self-conflicting hours), Mel’s Drive-In Lombard (official page down), Monk’s Kettle SF (closed), Monsieur Benjamin (closed), Nopa (11 PM), North Beach Pizza (11 PM), Pancho Villa, Pagan Idol, Pandora Karaoke (no close), Perry’s (9 PM), Powerhouse, Rite Spot (9 PM), Royal Exchange (9 PM), Serrano’s Pizza (11 PM), Sheba Piano Lounge, The Showdown (official page prints no street number), Silver Cloud, The Snug (closed), Super Duper Castro/Marina/Irving (11:30 PM or earlier), Suppenküche (10 PM), The Sycamore (weekend close not published), Third Rail (11 PM), Thee Parkside (no close), Toyose, Twin Peaks Tavern (address only), Whitechapel (private events), White Cap (official site prints no address), Woods Outbound/Cole Valley/Cerveceria (11 PM or earlier), Yancy’s, Zuni Café (9:30 PM). Dead, parked, for-sale, or hijacked domains encountered (e.g., Bond Bar, Homestead, Brewcade, Comet Club, Royal Cuckoo, Hobson’s Choice, Badlands, 540 Club, Whiskey Thieves, Old Devil Moon, Bloodhound, Gold Dust, Black Sands, Skylark) were never used as sources.

### Record-by-record checks (21–70)

### 21. The Little Shamrock

- **Status:** Official match.

- **Category / neighborhood:** Historic neighborhood bar · Inner Sunset.

- **Address check:** `807 Lincoln Way, San Francisco, CA 94122` — [official source](https://www.littleshamrock.co/).

- **Published source line:** “Address block: 807 Lincoln Way, SF, CA, 94122. Business hours block: Monday–Friday 3pm–1am; Saturday–Sunday 2pm–1am.”

- **Late-night result:** Friday: 3:00 PM–1:00 AM; Saturday: 2:00 PM–1:00 AM; Sunday: 2:00 PM–1:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** N Judah / 44 / 7 + short walk — Official stop lists place the N Judah at Judah St & 9th Ave, the 44 O’Shaughnessy at 9th Ave & Lincoln Way, and the 7 Haight/Noriega at Lincoln Way & 9th Ave, all within about two blocks of 807 Lincoln Way; use the live planner for the final walk. Mapped lines: N, 44, 7.

- **Manual review flags:** Hours were read from the official site’s structured business-hours block rather than a prose hours line; third-party listings show a 2 AM close, so the earlier official 1 AM value is used here.

- **Verification method:** Official site checked for name, address, and a seven-day business-hours block; Friday, Saturday, and Sunday all close at 1 AM.

- **Official link:** [https://www.littleshamrock.co/](https://www.littleshamrock.co/)

### 22. The Temple Bar

- **Status:** Official match.

- **Category / neighborhood:** Irish pub / sports bar · Inner Sunset.

- **Address check:** `834 Irving St, San Francisco, CA 94122` — [official source](https://templebarsf.com/contact/).

- **Published source line:** “Hours: Mon–Fri 2pm–2am; Sat 12pm–2am; Sun 1pm–2am; Sunday (NFL) 9:30am–2am. Address (menu page): 834 Irving St.”

- **Late-night result:** Friday: 2:00 PM–2:00 AM; Saturday: 12:00 PM–2:00 AM; Sunday: 1:00 PM–2:00 AM (NFL Sundays 9:30 AM–2:00 AM). This is why the record passes the >11 PM test.

- **Transit screen:** N Judah / 44 + short walk — The N Judah stop at Judah St & 9th Ave and the 44 O’Shaughnessy stops at 9th Ave & Irving St are about a block from 834 Irving; use the live planner for the final walk. Mapped lines: N, 44.

- **Manual review flags:** The official site publishes an earlier 9:30 AM opening on NFL Sundays; the street address is printed on the menu page rather than the contact page.

- **Verification method:** Official contact and menu pages checked for hours and address; Friday, Saturday, and Sunday all close at 2 AM.

- **Official link:** [https://templebarsf.com/contact/](https://templebarsf.com/contact/)

### 23. The Plough and Stars

- **Status:** Official match.

- **Category / neighborhood:** Irish pub / live music · Inner Richmond.

- **Address check:** `116 Clement St, San Francisco, CA 94118` — [official source](https://theploughandstars.com/).

- **Published source line:** “116 Clement St, San Francisco, CA 94118. Hours: Sun 11am–2am; Mon 5pm–2am; Tue 5pm–2am; Wed 3pm–2am; Thu 4pm–2am; Fri 3pm–2am; Sat 2pm–2am.”

- **Late-night result:** Friday: 3:00 PM–2:00 AM; Saturday: 2:00 PM–2:00 AM; Sunday: 11:00 AM–2:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 44 to 6th Ave & Clement / 38 Geary + walk — From the origin, the N Judah to 9th Ave connects to the 44 O’Shaughnessy (24 hours) north to 6th Ave & Clement St; the 38 Geary (24 hours) stops at Geary Blvd & 3rd Ave one block south, and the 1 California (until midnight) at California St & 4th Ave. Use the live planner for the final walk. Mapped lines: 44, 38, 1.

- **Manual review flags:** The official site notes a cover charge on Friday and Saturday live-music nights.

- **Verification method:** Official site checked for address and full weekly hours; Friday, Saturday, and Sunday all close at 2 AM.

- **Official link:** [https://theploughandstars.com/](https://theploughandstars.com/)

### 24. The Bitter End

- **Status:** Official match.

- **Category / neighborhood:** Irish pub / sports bar · Inner Richmond.

- **Address check:** `441 Clement St, San Francisco, CA` — [official source](https://www.thebitterendsf.com/).

- **Published source line:** “441 Clement Street, San Francisco. (415) 221-9538. Hours: Mon–Fri 4pm – 2am; Sat + Sun noon – 2am.”

- **Late-night result:** Friday: 4:00 PM–2:00 AM; Saturday: 12:00 PM–2:00 AM; Sunday: 12:00 PM–2:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 44 to 6th Ave & Clement / 38 Geary + walk — The 44 O’Shaughnessy (24 hours) stops at 6th Ave & Clement St, the 38 Geary (24 hours) at Geary Blvd & 6th Ave, and the 1 California (until midnight) at California St & 6th Ave; use the live planner for the final block to 441 Clement. Mapped lines: 44, 38, 1.

- **Manual review flags:** The official page prints the street address without a ZIP code; none is inferred here.

- **Verification method:** Official site checked for address and weekly hours; Friday, Saturday, and Sunday all close at 2 AM.

- **Official link:** [https://www.thebitterendsf.com/](https://www.thebitterendsf.com/)

### 25. Nizario’s Pizza (Richmond District)

- **Status:** Official match.

- **Category / neighborhood:** Pizza / late-night food · Inner Richmond.

- **Address check:** `3840 Geary Blvd, San Francisco, CA 94118` — [official source](https://www.nizarios.com/).

- **Published source line:** “SF Richmond District: 3840 Geary Blvd, San Francisco, CA 94118. 415-752-7777. Sun – Thurs: 3:00pm – 11pm. Fri & Sat: 3pm – 1:30am.”

- **Late-night result:** Friday: 3:00 PM–1:30 AM; Saturday: 3:00 PM–1:30 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 38 Geary (24 hours) / 44 + walk — The 38 Geary (24 hours) stops at Geary Blvd & 3rd Ave, and the 44 O’Shaughnessy (24 hours) at 6th Ave & Geary Blvd; from the origin, N Judah to 9th Ave then 44 north is the simplest late connection. Use the live planner for the final walk. Mapped lines: 38, 44.

- **Manual review flags:** Counter-service pizza shop; only the Geary Blvd location qualifies (the SFSU location closes by 6 PM).

- **Verification method:** Official site checked for address and weekly hours; Friday and Saturday close at 1:30 AM.

- **Official link:** [https://www.nizarios.com/](https://www.nizarios.com/)

### 26. Escape From New York Pizza (Haight)

- **Status:** Official match.

- **Category / neighborhood:** Pizza / late-night food · Upper Haight.

- **Address check:** `1737 Haight St, San Francisco, CA` — [official source](https://escapefromnewyorkpizza.com/).

- **Published source line:** “1737 Haight Street. Pickup hours: Mon – Wed 10:30a – 9:30p; Thursday 10:30a – 10:30p; Fri – Sat 10:30a – 1:30a; Sunday 10:30a – 9:30p.”

- **Late-night result:** Friday: 10:30 AM–1:30 AM; Saturday: 10:30 AM–1:30 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 7 Haight / N Judah (Carl & Cole) + walk — The 7 Haight/Noriega (until midnight) stops at Haight St & Clayton St and Haight St & Stanyan St; the N Judah stop at Carl St & Cole St is about two blocks south, and the N Owl stops at Cole St & Haight St overnight. Use the live planner for the final walk to 1737 Haight. Mapped lines: 7, N, NOWL.

- **Manual review flags:** The official site labels these as “Pickup hours” for a counter-service slice shop; no ZIP code is printed for this location.

- **Verification method:** Official site checked for address and weekly pickup hours; Friday and Saturday close at 1:30 AM.

- **Official link:** [https://escapefromnewyorkpizza.com/](https://escapefromnewyorkpizza.com/)

### 27. Toronado

- **Status:** Official match with documented gap.

- **Category / neighborhood:** Beer bar · Lower Haight.

- **Address check:** `547 Haight St, San Francisco, CA 94117` — [official source](https://www.toronado.com/contact/).

- **Published source line:** “Hours: 11:30am to 2:00am daily. 547 Haight St, San Francisco, CA 94117.”

- **Late-night result:** Friday: 11:30 AM–2:00 AM; Saturday: 11:30 AM–2:00 AM; Sunday: 11:30 AM–2:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 7 Haight / 22 Fillmore / N Owl + walk — The 7 Haight/Noriega (until midnight) stops at Haight St & Fillmore St, the 22 Fillmore (24 hours) at Fillmore St & Haight St, and the N Owl (midnight–5 AM) at Haight St & Fillmore St; use the live planner for the final block. Mapped lines: 7, 22, NOWL.

- **Manual review flags:** The official contact page did not render text in our direct fetch (the site served its beer list on every path); the hours line was read from the search-engine copy of that official page and should be confirmed on site.

- **Verification method:** Official domain confirmed; hours text taken from the indexed copy of the official contact page because the live page did not render.

- **Official link:** [https://www.toronado.com/contact/](https://www.toronado.com/contact/)

### 28. Noc Noc

- **Status:** Official match.

- **Category / neighborhood:** Beer, wine & sake bar · Lower Haight.

- **Address check:** `557 Haight St, San Francisco, CA 94117-3406` — [official source](https://www.nocnocs.com/).

- **Published source line:** “557 Haight Street, San Francisco, CA 94117-3406 (Between Fillmore and Steiner). Open every day: Sunday – Thursday 5 pm – 1 am; Friday – Saturday 5 pm – 2 am.”

- **Late-night result:** Friday: 5:00 PM–2:00 AM; Saturday: 5:00 PM–2:00 AM; Sunday: 5:00 PM–1:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 7 Haight / 22 Fillmore / N Owl + walk — Same corridor as Toronado: 7 Haight/Noriega and N Owl at Haight St & Fillmore St, 22 Fillmore at Fillmore St & Haight St; the bar is between Fillmore and Steiner. Use the live planner for the final block. Mapped lines: 7, 22, NOWL.

- **Manual review flags:** The official site describes a beer, wine, and sake bar (no liquor); Sunday qualifies with a 1 AM close.

- **Verification method:** Official site checked for address and weekly hours; Friday and Saturday close at 2 AM and Sunday at 1 AM.

- **Official link:** [https://www.nocnocs.com/](https://www.nocnocs.com/)

### 29. Woods Lowside

- **Status:** Official match.

- **Category / neighborhood:** Brewery taproom / natural wine bar · Lower Haight.

- **Address check:** `530 Haight St, San Francisco, CA` — [official source](https://www.woodsbeer.com/lowside).

- **Published source line:** “530 Haight Street. (415) 548-5734. BAR Hours: Monday – Wednesday: 5pm to 11pm; Thursday: 5pm to 11pm; Friday: 4pm to 12am; Saturday: 1pm to 12am; Sunday: 1pm to 10pm. KITCHEN Hours: 5pm to 9pm.”

- **Late-night result:** Friday: 4:00 PM–12:00 AM; Saturday: 1:00 PM–12:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 7 Haight / 22 Fillmore / N Owl + walk — Same Haight & Fillmore corridor: 7 Haight/Noriega (until midnight), 22 Fillmore (24 hours), and the N Owl after midnight; use the live planner for the final block to 530 Haight. Mapped lines: 7, 22, NOWL.

- **Manual review flags:** Qualifies only under the midnight-counts-as-late policy (Friday and Saturday close at 12 AM); the Tacos Oscar kitchen closes at 9 PM.

- **Verification method:** Official location page checked for address and separate bar/kitchen hours; Friday and Saturday bar close is 12 AM.

- **Official link:** [https://www.woodsbeer.com/lowside](https://www.woodsbeer.com/lowside)

### 30. Horsefeather

- **Status:** Official match.

- **Category / neighborhood:** Cocktail bar / food · Divisadero / NoPa.

- **Address check:** `528 Divisadero St, San Francisco, CA 94117` — [official source](https://horsefeather.com/sf/book).

- **Published source line:** “528 Divisadero St, San Francisco, CA 94117. MONDAY–THURSDAY 2p–12a (kitchen 11:30pm); FRIDAY 2p–2a (kitchen 1:00am); SATURDAY 11a–2a (kitchen 1:00am); SUNDAY 11a–12a (kitchen 11:30pm).”

- **Late-night result:** Friday: 2:00 PM–2:00 AM; kitchen until 1:00 AM; Saturday: 11:00 AM–2:00 AM; kitchen until 1:00 AM; Sunday: 11:00 AM–12:00 AM; kitchen until 11:30 PM. This is why the record passes the >11 PM test.

- **Transit screen:** 24 Divisadero (24 hours) / 6 Hayes + walk — The 24 Divisadero (24 hours) stops at Divisadero St & Hayes St and Divisadero St & Oak St; the 6 Hayes/Parnassus (until midnight) stops at Hayes St & Divisadero St. Use the live planner for the final steps to 528 Divisadero. Mapped lines: 24, 6.

- **Manual review flags:** Sunday qualifies only under the midnight policy; kitchen closes 30–60 minutes before the bar.

- **Verification method:** Official page checked for address and full weekly bar/kitchen hours; Friday and Saturday close at 2 AM, Sunday at midnight.

- **Official link:** [https://horsefeather.com/sf/book](https://horsefeather.com/sf/book)

### 31. Madrone Art Bar

- **Status:** Official match.

- **Category / neighborhood:** Art bar / DJ nights · Divisadero / NoPa.

- **Address check:** `500 Divisadero St, San Francisco, CA 94117` — [official source](https://madroneartbar.com/contact/).

- **Published source line:** “500 Divisadero Street, San Francisco, CA 94117 (at Divisadero & Fell). Open daily, 4pm–2am.”

- **Late-night result:** Friday: 4:00 PM–2:00 AM; Saturday: 4:00 PM–2:00 AM; Sunday: 4:00 PM–2:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 24 Divisadero (24 hours) / 6 Hayes + walk — The 24 Divisadero stops at Divisadero St & Hayes St (the bar is at Divisadero & Fell) and the 6 Hayes/Parnassus at Hayes St & Divisadero St until midnight; use the live planner for the final block. Mapped lines: 24, 6.

- **Manual review flags:** Event and DJ nights can add a cover; the official page publishes a single daily hours line.

- **Verification method:** Official contact page checked for address and daily hours; all three weekend days close at 2 AM.

- **Official link:** [https://madroneartbar.com/contact/](https://madroneartbar.com/contact/)

### 32. The Page

- **Status:** Official match with documented gap.

- **Category / neighborhood:** Neighborhood bar · Divisadero / NoPa.

- **Address check:** `298 Divisadero St, San Francisco, CA 94117` — [official source](https://www.thepagebar.com/).

- **Published source line:** “Open Daily until 2am. 298 Divisadero St, San Francisco, CA 94117 (address printed on the venue’s music calendar page).”

- **Late-night result:** Friday: Open until 2:00 AM; opening time not stated; Saturday: Open until 2:00 AM; opening time not stated; Sunday: Open until 2:00 AM; opening time not stated. This is why the record passes the >11 PM test.

- **Transit screen:** 24 Divisadero (24 hours) / 7 Haight / N Owl + walk — The 24 Divisadero stops at Divisadero St & Haight St and Divisadero St & Oak St; the 7 Haight/Noriega (until midnight) and N Owl (after midnight) stop at Haight St & Divisadero St, one block from Page St. Use the live planner for the final block. Mapped lines: 24, 7, NOWL.

- **Manual review flags:** The official site publishes only a daily closing time; the opening time is not stated and is not inferred.

- **Verification method:** Official site checked for closing time and address; opening time is not published.

- **Official link:** [https://www.thepagebar.com/](https://www.thepagebar.com/)

### 33. Fly Bar

- **Status:** Official match with documented gap.

- **Category / neighborhood:** Neighborhood bar / food · Divisadero / NoPa.

- **Address check:** `762 Divisadero St, San Francisco, CA 94117` — [official source](https://www.flybardivis.com/).

- **Published source line:** “762 Divisadero St, San Francisco, CA 94117. HOURS: Open Everyday to 2 am. Mon–Thurs: 2 pm – 2 am; Sat: 12 pm – 2 am; Sun: 10 am – 2 am.”

- **Late-night result:** Friday: Open until 2:00 AM; opening time not stated; Saturday: 12:00 PM–2:00 AM; Sunday: 10:00 AM–2:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 24 Divisadero (24 hours) / 5 Fulton + walk — The 24 Divisadero stops at Divisadero St & McAllister St and the 5 Fulton (24 hours) at McAllister St & Divisadero St, two blocks from Fulton; use the live planner for the final blocks. Mapped lines: 24, 5.

- **Manual review flags:** The official hours block omits a Friday opening time while stating the bar is open every day until 2 AM; Friday is recorded as close-only. flybarsf.com redirects to flybardivis.com.

- **Verification method:** Official site checked for address and hours; Friday opening time is not published.

- **Official link:** [https://www.flybardivis.com/](https://www.flybardivis.com/)

### 34. Smuggler’s Cove

- **Status:** Official match.

- **Category / neighborhood:** Tiki / rum bar · Hayes Valley.

- **Address check:** `650 Gough St, San Francisco, CA 94102` — [official source](https://www.smugglerscovesf.com/).

- **Published source line:** “Address block: 650 Gough St, San Francisco, CA 94102. Business hours block: daily 5:00PM to 1:15AM.”

- **Late-night result:** Friday: 5:00 PM–1:15 AM; Saturday: 5:00 PM–1:15 AM; Sunday: 5:00 PM–1:15 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 5 Fulton (24 hours) / N Judah to Van Ness + walk — The 5 Fulton (24 hours) stops at McAllister St & Gough St, one block from 650 Gough; the N Judah Van Ness Station is about four blocks east and the 6 Hayes/Parnassus (until midnight) stops at Grove St & Gough St. Use the live planner for the final walk. Mapped lines: 5, N, 6.

- **Manual review flags:** Hours were read from the official site’s structured business-hours block; SFMTA posts a Hayes Valley Shared Spaces reroute for the 6 Hayes/Parnassus on Fridays 4–10 PM and Saturdays 7 AM–10 PM in September 2026.

- **Verification method:** Official site checked for address and a seven-day business-hours block; every day closes at 1:15 AM.

- **Official link:** [https://www.smugglerscovesf.com/](https://www.smugglerscovesf.com/)

### 35. Super Duper Burgers (Fillmore)

- **Status:** Official match.

- **Category / neighborhood:** Burgers / late-night food · Fillmore / Japantown.

- **Address check:** `1701 Fillmore St, San Francisco, CA 94115` — [official source](https://www.superduperburgers.com/store-locator/).

- **Published source line:** “Fillmore: 1701 Fillmore St, San Francisco, CA 94115. Hours of Operation: Sun–Thurs 10:00am to 11:00pm, Fri–Sat 10:00am–12:00am.”

- **Late-night result:** Friday: 10:00 AM–12:00 AM; Saturday: 10:00 AM–12:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 22 Fillmore / 38 Geary (both 24 hours) + walk — The 22 Fillmore stops at Fillmore St & O’Farrell St and Fillmore St & Sutter St, and the 38 Geary at Geary Blvd & Fillmore St, all within a block of 1701 Fillmore (at Post); use the live planner for the final steps. Mapped lines: 22, 38.

- **Manual review flags:** Qualifies only under the midnight policy (Friday and Saturday close at 12 AM); other Super Duper locations close earlier and are not included.

- **Verification method:** Official store locator checked for address and weekly hours; Friday and Saturday close at midnight.

- **Official link:** [https://www.superduperburgers.com/location/fillmore/](https://www.superduperburgers.com/location/fillmore/)

### 36. Brazen Head

- **Status:** Official match with documented gap.

- **Category / neighborhood:** Restaurant / late-night bar · Cow Hollow.

- **Address check:** `3166 Buchanan St, San Francisco, CA 94123` — [official source](https://www.brazenheadsf.com/about).

- **Published source line:** “Kitchen: Sun–Tue 5–11pm; Wed–Sat 5–12am. Bar: 5–2am daily. Address (site listing): 3166 Buchanan St. SF.”

- **Late-night result:** Friday: Bar 5:00 PM–2:00 AM; kitchen 5:00 PM–12:00 AM; Saturday: Bar 5:00 PM–2:00 AM; kitchen 5:00 PM–12:00 AM; Sunday: Bar 5:00 PM–2:00 AM; kitchen 5:00 PM–11:00 PM. This is why the record passes the >11 PM test.

- **Transit screen:** 22 Fillmore (24 hours) / 28 19th Ave + walk — The 22 Fillmore (24 hours) stops at Fillmore St & Union St and Fillmore St & Lombard St, two blocks west of Buchanan & Greenwich; from the origin the 28 19th Avenue (until midnight) reaches Lombard St & Laguna St. Use the live planner for the final walk. Mapped lines: 22, 28.

- **Manual review flags:** The street address appears in the official site’s listing/metadata rather than in the About page text we captured; confirm the entrance at Buchanan & Greenwich before going.

- **Verification method:** Official About page checked for bar and kitchen hours; address taken from the official site listing.

- **Official link:** [https://www.brazenheadsf.com/about](https://www.brazenheadsf.com/about)

### 37. Wilder

- **Status:** Official match.

- **Category / neighborhood:** Restaurant / cocktail bar · Cow Hollow / Marina.

- **Address check:** `3154 Fillmore St, San Francisco, CA 94123` — [official source](https://wildersfc.com/).

- **Published source line:** “3154 Fillmore St, San Francisco, CA 94123. Call (415) 741-6605. Sunday 11:00 AM – 8:00 PM; Monday Closed; Tuesday Closed; Wednesday 5:00 PM – 11:00 PM; Thursday 5:00 PM – 11:00 PM; Friday 4:00 PM – 1:00 AM; Saturday 11:00 AM – 1:00 AM.”

- **Late-night result:** Friday: 4:00 PM–1:00 AM; Saturday: 11:00 AM–1:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 22 Fillmore (24 hours) / 28 19th Ave + walk — The 22 Fillmore (24 hours) stops at Fillmore St & Union St and Fillmore St & Lombard St, bracketing 3154 Fillmore; from the origin the 28 19th Avenue (until midnight) stops at Lombard St & Fillmore St. Use the live planner for the final steps. Mapped lines: 22, 28.

- **Manual review flags:** Closed Monday and Tuesday per the official hours block; wildersf.com redirects to wildersfc.com.

- **Verification method:** Official site checked for address and weekly hours; Friday and Saturday close at 1 AM.

- **Official link:** [https://wildersfc.com/](https://wildersfc.com/)

### 38. Woods Polk Station

- **Status:** Official match.

- **Category / neighborhood:** Brewery taproom / bar · Russian Hill.

- **Address check:** `2255 Polk St, San Francisco, CA` — [official source](https://www.woodsbeer.com/polk-station).

- **Published source line:** “2255 Polk Street. (415) 463-7418. Hours: Monday – Thursday 4pm to 10pm; Friday – Saturday 1pm to 12am; Sunday 1pm to 8pm.”

- **Late-night result:** Friday: 1:00 PM–12:00 AM; Saturday: 1:00 PM–12:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 49 Van Ness (until midnight) + one-block walk — The 49 Van Ness/Mission stops at Van Ness Ave & Union St and Van Ness Ave & Vallejo St, one block west of 2255 Polk (at Green); the 19 Polk ends at 10 PM and the 47 Van Ness is listed as suspended. Use the live planner for the return leg. Mapped lines: 49.

- **Manual review flags:** Qualifies only under the midnight policy; the last 49 Van Ness trips also run around midnight, so the return leg needs a live check.

- **Verification method:** Official location page checked for address and weekly hours; Friday and Saturday close at 12 AM.

- **Official link:** [https://www.woodsbeer.com/polk-station](https://www.woodsbeer.com/polk-station)

### 39. Tommy’s Joynt

- **Status:** Official match.

- **Category / neighborhood:** Hofbrau / restaurant & bar · Van Ness / Polk Gulch.

- **Address check:** `1101 Geary Blvd, San Francisco, CA 94109` — [official source](https://tommysjoynt.com/).

- **Published source line:** “1101 Geary Blvd, San Francisco, CA 94109. Sun & Mon 12–8pm; Tue & Wed 12–9pm; Thu & Fri 12–12 midnight; Sat 1pm–12 midnight.”

- **Late-night result:** Friday: 12:00 PM–12:00 AM; Saturday: 1:00 PM–12:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 38 Geary (24 hours) / 49 Van Ness + short walk — The 38 Geary stops at O’Farrell St & Van Ness Ave (inbound) and Geary Blvd & Van Ness Ave (outbound), and the 49 Van Ness/Mission at Van Ness Ave & Geary Blvd, all at the restaurant’s corner; use the live planner for the return leg. Mapped lines: 38, 49.

- **Manual review flags:** Qualifies only under the midnight policy (Friday and Saturday close at 12 midnight); Sunday closes at 8 PM.

- **Verification method:** Official site checked for address and weekly hours; Friday and Saturday close at midnight.

- **Official link:** [https://tommysjoynt.com/](https://tommysjoynt.com/)

### 40. Lush Lounge

- **Status:** Official match.

- **Category / neighborhood:** Cocktail lounge · Polk Gulch.

- **Address check:** `1221 Polk St, San Francisco, CA 94109` — [official source](https://www.lushloungesf.com/).

- **Published source line:** “1221 Polk Street, San Francisco, CA 94109. Lush Lounge is open daily. Monday–Friday 3pm until 2am; Saturday and Sunday 1pm until 2am.”

- **Late-night result:** Friday: 3:00 PM–2:00 AM; Saturday: 1:00 PM–2:00 AM; Sunday: 1:00 PM–2:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 49 Van Ness / 38 Geary + walk — The 49 Van Ness/Mission (until midnight) stops at Van Ness Ave & Bush St one block west of Polk & Sutter; the 38 Geary (24 hours) stops at O’Farrell St & Larkin St about three blocks south. Use the live planner for the return leg. Mapped lines: 49, 38.

- **Manual review flags:** The page title on the same official site says weekends open at 3pm while the body text says 1pm; the 2 AM close is consistent in both.

- **Verification method:** Official site checked for address and weekly hours; all three weekend days close at 2 AM (opening-time conflict flagged).

- **Official link:** [https://www.lushloungesf.com/](https://www.lushloungesf.com/)

### 41. Bob’s Donuts

- **Status:** Official match with documented gap.

- **Category / neighborhood:** Donut shop (24 hours) · Polk Gulch.

- **Address check:** `1621 Polk St, San Francisco, CA 94109` — [official source](https://bobsdonutssf.com/).

- **Published source line:** “Address block: 1621 Polk St, San Francisco, CA, 94109. Business hours block: every day marked Open with a 0:00–0:00 range (24 hours).”

- **Late-night result:** Friday: Open 24 hours; Saturday: Open 24 hours; Sunday: Open 24 hours. This is why the record passes the >11 PM test.

- **Transit screen:** 1 California / 49 Van Ness + walk (no overnight line on Polk) — The 1 California (until midnight) stops at Sacramento St & Polk St and the 49 Van Ness/Mission (until midnight) at Van Ness Ave & Clay St; after midnight the nearest 24-hour corridor is the 38 Geary at O’Farrell St & Van Ness Ave, about eight blocks south. Use the live planner for the return leg. Mapped lines: 1, 49, 38.

- **Manual review flags:** The 24-hour claim comes from the official site’s structured business-hours block, not a prose hours line; confirm overnight service before relying on it.

- **Verification method:** Official site checked for address; 24-hour operation read from structured business-hours data only.

- **Official link:** [https://bobsdonutssf.com/](https://bobsdonutssf.com/)

### 42. Kozy Kar

- **Status:** Official match.

- **Category / neighborhood:** Theme bar · Polk Gulch.

- **Address check:** `1548 Polk St, San Francisco, CA 94109` — [official source](https://www.kozykar.com/).

- **Published source line:** “KOZY KAR BAR, 1548 POLK STREET AT SACRAMENTO, SAN FRANCISCO, CA. 94109. HOURS: WEDNESDAY–SATURDAY 7PM–2AM.”

- **Late-night result:** Friday: 7:00 PM–2:00 AM; Saturday: 7:00 PM–2:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 1 California / 49 Van Ness + walk — The 1 California (until midnight) stops at Sacramento St & Polk St at the bar’s corner and the 49 Van Ness/Mission (until midnight) at Van Ness Ave & Clay St; after midnight use the 38 Geary corridor or the live planner. Mapped lines: 1, 49.

- **Manual review flags:** Open Wednesday through Saturday only; the official site describes adult-themed 1970s décor and video content, so it is not for every group.

- **Verification method:** Official site checked for address and weekly hours; Friday and Saturday close at 2 AM.

- **Official link:** [https://www.kozykar.com/](https://www.kozykar.com/)

### 43. Top of the Mark

- **Status:** Official match.

- **Category / neighborhood:** Hotel sky lounge / cocktail bar · Nob Hill.

- **Address check:** `999 California St, San Francisco, CA 94108` — [official source](https://www.topofthemark.com/).

- **Published source line:** “Location: 999 California Street, San Francisco, CA 94108. Hours: Sunday – Thursday 4:00 pm – 11:00 pm; Friday – Saturday 3:00 pm – 12:30 am (kitchen: 4:00 pm – 9:30 pm last order).”

- **Late-night result:** Friday: 3:00 PM–12:30 AM; kitchen last order 9:30 PM; Saturday: 3:00 PM–12:30 AM; kitchen last order 9:30 PM. This is why the record passes the >11 PM test.

- **Transit screen:** 1 California (until midnight) / N Judah to Powell + steep walk — The 1 California stops at Sacramento St & Powell St one block north of the hotel until about midnight; the N Judah Powell Station is about five steep blocks south, and the 38 Geary (24 hours) at O’Farrell St & Powell St is the overnight fallback. Use the live planner for the return leg after 12 AM. Mapped lines: 1, N, 38.

- **Manual review flags:** The official site lists a $15 cover for Saturday live bands ($10 for hotel guests) and a full closure for a private event on October 21, 2026.

- **Verification method:** Official site checked for address and weekly hours; Friday and Saturday close at 12:30 AM.

- **Official link:** [https://www.topofthemark.com/](https://www.topofthemark.com/)

### 44. Zeki’s Bar

- **Status:** Official match.

- **Category / neighborhood:** Neighborhood cocktail bar · Nob Hill.

- **Address check:** `1319 California St, San Francisco, CA` — [official source](https://www.zekisbar.com/).

- **Published source line:** “Visit Us: Monday 4pm – midnight; Tuesday 4pm – 2am; Wednesday 4pm – 2am; Thursday 4pm – 2am; Friday 4pm – 2am; Saturday noon – 2am; Sunday noon – midnight. 1319 California St., San Francisco, CA.”

- **Late-night result:** Friday: 4:00 PM–2:00 AM; Saturday: 12:00 PM–2:00 AM; Sunday: 12:00 PM–12:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 1 California (until midnight) / 38 Geary + uphill walk — The 1 California stops at Sacramento St & Leavenworth St and Sacramento St & Hyde St, one block north of 1319 California, until about midnight; the 38 Geary (24 hours) at O’Farrell St & Leavenworth St is about five uphill blocks south. Use the live planner for the return leg. Mapped lines: 1, 38.

- **Manual review flags:** Sunday qualifies only under the midnight policy; the official page prints no ZIP code.

- **Verification method:** Official site checked for address and weekly hours; Friday and Saturday close at 2 AM, Sunday at midnight.

- **Official link:** [https://www.zekisbar.com/](https://www.zekisbar.com/)

### 45. The Royale

- **Status:** Official match.

- **Category / neighborhood:** Cocktail bar / live music · Lower Nob Hill.

- **Address check:** `800 Post St, San Francisco, CA 94109` — [official source](https://www.theroyalesf.com/).

- **Published source line:** “LOCATION: 800 Post Street, San Francisco, CA 94109. HOURS: Sun – Wed 5pm – 12am; Thurs – Sat 5pm – 2am.”

- **Late-night result:** Friday: 5:00 PM–2:00 AM; Saturday: 5:00 PM–2:00 AM; Sunday: 5:00 PM–12:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 38 Geary (24 hours) + two-block walk / N Judah to Powell — The 38 Geary stops at O’Farrell St & Leavenworth St two blocks south of Post & Leavenworth and runs 24 hours; the N Judah Powell Station is about a 10-minute walk. Use the live planner for the final blocks. Mapped lines: 38, N.

- **Manual review flags:** Sunday qualifies only under the midnight policy; live-music nights may change the door experience.

- **Verification method:** Official site checked for address and weekly hours; Friday and Saturday close at 2 AM, Sunday at midnight.

- **Official link:** [https://www.theroyalesf.com/](https://www.theroyalesf.com/)

### 46. Rickhouse

- **Status:** Official match.

- **Category / neighborhood:** Whiskey / cocktail bar · Financial District.

- **Address check:** `246 Kearny St, San Francisco, CA 94108` — [official source](https://www.rickhousebar.com/).

- **Published source line:** “246 Kearny Street, San Francisco, CA 94108. MON – Wed: 3pm–12am | Thu–FRI: 3pm–2am | SAT: 6PM–2AM | Sun: Closed to rest.”

- **Late-night result:** Friday: 3:00 PM–2:00 AM; Saturday: 6:00 PM–2:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** N Judah to Montgomery + walk / 38 Geary / 30 Stockton — The N Judah Montgomery Station is about three blocks south of Kearny & Bush; the 38 Geary (24 hours) stops at Geary St & Kearny St and the 30 Stockton (until midnight) at Stockton St & Sutter St. Use the live planner for the final walk. Mapped lines: N, 38, 30.

- **Manual review flags:** Closed Sunday per the official site.

- **Verification method:** Official site checked for address and weekly hours; Friday and Saturday close at 2 AM.

- **Official link:** [https://www.rickhousebar.com/](https://www.rickhousebar.com/)

### 47. Escape From New York Pizza (Downtown)

- **Status:** Official match.

- **Category / neighborhood:** Pizza / late-night food · Financial District.

- **Address check:** `333 Bush St #104, San Francisco, CA` — [official source](https://escapefromnewyorkpizza.com/).

- **Published source line:** “333 Bush Street #104. Mon – Wed 10:30a – 7:00p; Thursday 10:30a – 1:00a; Friday 10:30a – 2:00a; Saturday 5:00p – 2:00a; Sunday 5:00p – 1:00a.”

- **Late-night result:** Friday: 10:30 AM–2:00 AM; Saturday: 5:00 PM–2:00 AM; Sunday: 5:00 PM–1:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** N Judah to Montgomery + walk / 38 Geary / N Owl — The N Judah Montgomery Station is about two blocks south of Bush & Montgomery; the 38 Geary (24 hours) stops at Geary St & Kearny St and the N Owl at Market St & New Montgomery St overnight. Use the live planner for the final walk. Mapped lines: N, 38, NOWL.

- **Manual review flags:** Counter-service slice shop; the official site prints no ZIP code for this location.

- **Verification method:** Official site checked for address and weekly hours; Friday and Saturday close at 2 AM, Sunday at 1 AM.

- **Official link:** [https://escapefromnewyorkpizza.com/](https://escapefromnewyorkpizza.com/)

### 48. Local Edition

- **Status:** Official match.

- **Category / neighborhood:** Cocktail bar / live jazz · Financial District.

- **Address check:** `691 Market St, San Francisco, CA 94105` — [official source](https://www.localeditionsf.com/).

- **Published source line:** “We are open Monday Through Saturday; 21+ WITH VALID ID. Mon: 4:30pm – 12am; Tues–Wed: 4:30pm – 1am; Thurs–Fri: 4:30pm – 2am; Sat: 6pm – 2am; Sun: closed. Location: 691 Market St., San Francisco, CA. Located just before Third St. on Market. Just head down the stairs.”

- **Late-night result:** Friday: 4:30 PM–2:00 AM; Saturday: 6:00 PM–2:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** N Judah to Montgomery / N Owl / 38 Geary on Market — The N Judah Montgomery Station and the N Owl stop at Market St & New Montgomery St are at the door of the Hearst Building (Market at 3rd); the 38 Geary also stops at Market St & 3rd St. Use the live planner for the return leg. Mapped lines: N, NOWL, 38.

- **Manual review flags:** 21+ with valid ID and closed Sunday per the official site; our page render truncated the location block, so the 691 Market St line was confirmed from the indexed copy of the same official page.

- **Verification method:** Official site checked for hours and address (basement entrance on Market near 3rd); Friday and Saturday close at 2 AM.

- **Official link:** [https://www.localeditionsf.com/](https://www.localeditionsf.com/)

### 49. The Irish Bank

- **Status:** Official match.

- **Category / neighborhood:** Irish pub / restaurant · Financial District.

- **Address check:** `10 Mark Lane, San Francisco, CA 94108` — [official source](https://www.theirishbank.com/).

- **Published source line:** “Hours are 11.30am – 12.00 midnight Sunday through Thursday. 11.30am – 2am Friday and Saturday. Address (events page): 10 Mark Lane, San Francisco, CA 94108, 415 788-7152.”

- **Late-night result:** Friday: 11:30 AM–2:00 AM; Saturday: 11:30 AM–2:00 AM; Sunday: 11:30 AM–12:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** N Judah to Montgomery + walk / 30 Stockton / 38 Geary — Mark Lane is an alley off Bush St between Grant and Kearny: the N Judah Montgomery Station is about three blocks south, the 30 Stockton (until midnight) stops at Stockton St & Sutter St, and the 38 Geary (24 hours) at Geary St & Kearny St. Use the live planner for the final walk. Mapped lines: N, 30, 38.

- **Manual review flags:** The same official site carries a site-wide hours block reading 11:30am to 2am every day and a structured-data address of “10 Market Street” that conflicts with the alley address; the homepage hours and the Mark Lane address are used here. Sunday qualifies only under the midnight policy.

- **Verification method:** Official homepage checked for hours and the official events page for address; Friday and Saturday close at 2 AM (conflicts flagged).

- **Official link:** [https://www.theirishbank.com/](https://www.theirishbank.com/)

### 50. Comstock Saloon

- **Status:** Official match with documented gap.

- **Category / neighborhood:** Historic saloon / restaurant · North Beach.

- **Address check:** `155 Columbus Ave, San Francisco, CA 94133` — [official source](https://www.comstocksaloon.com/).

- **Published source line:** “155 Columbus Ave, San Francisco, CA 94133. DRINK MENU served daily until midnight. FOOD MENU served daily until 11pm.”

- **Late-night result:** Friday: Open until 12:00 AM (drink menu served daily until midnight); opening time not stated; Saturday: Open until 12:00 AM (drink menu served daily until midnight); opening time not stated; Sunday: Open until 12:00 AM (drink menu served daily until midnight); opening time not stated. This is why the record passes the >11 PM test.

- **Transit screen:** 30 Stockton (until midnight) / N Judah to Montgomery + walk — The 30 Stockton stops at Stockton St & Pacific Ave two blocks west of Columbus & Pacific until about midnight; the N Judah Montgomery Station is roughly a 12-minute walk south. Use the live planner for the return leg. Mapped lines: 30, N.

- **Manual review flags:** The official site publishes closing times for the drink and food menus but no opening time; midnight qualifies only under the midnight policy.

- **Verification method:** Official site checked for address and closing times; opening time is not published.

- **Official link:** [https://www.comstocksaloon.com/](https://www.comstocksaloon.com/)

### 51. Gino & Carlo

- **Status:** Official match.

- **Category / neighborhood:** Historic neighborhood bar · North Beach.

- **Address check:** `548 Green St, San Francisco, CA` — [official source](https://ginoandcarlo.com/).

- **Published source line:** “548 Green Street, North Beach. OPEN EVERY DAY OF THE YEAR 6 AM – 2 AM.”

- **Late-night result:** Friday: 6:00 AM–2:00 AM; Saturday: 6:00 AM–2:00 AM; Sunday: 6:00 AM–2:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 30 Stockton (until midnight) + walk — The 30 Stockton stops at Columbus Ave & Union St and Stockton St & Columbus Ave, a block or two from Green & Grant, until about midnight; after that the N Owl on Market Street is the nearest overnight line. Use the live planner for the return leg. Mapped lines: 30, NOWL.

- **Manual review flags:** The official page prints no ZIP code; the 30 Stockton ends around midnight, so the return leg after 12 AM needs a live check.

- **Verification method:** Official site checked for address and daily hours; every day closes at 2 AM.

- **Official link:** [https://ginoandcarlo.com/](https://ginoandcarlo.com/)

### 52. Tony Nik’s Cafe

- **Status:** Official match.

- **Category / neighborhood:** Historic cocktail bar · North Beach.

- **Address check:** `1534 Stockton St, San Francisco, CA 94133` — [official source](https://www.tonyniks.com/contact/).

- **Published source line:** “1534 Stockton Street, San Francisco, CA 94133. Mon–Thurs: 4PM–1AM; Fridays: 3PM–2AM; Saturday: 2PM–2AM; Sunday: 2PM–1AM.”

- **Late-night result:** Friday: 3:00 PM–2:00 AM; Saturday: 2:00 PM–2:00 AM; Sunday: 2:00 PM–1:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 30 Stockton (until midnight) + walk — The 30 Stockton stops at Stockton St & Columbus Ave and Columbus Ave & Union St at the bar’s block until about midnight; after that the N Owl on Market Street is the nearest overnight line. Use the live planner for the return leg. Mapped lines: 30, NOWL.

- **Manual review flags:** The 30 Stockton ends around midnight, so the return leg after 12 AM needs a live check.

- **Verification method:** Official contact page checked for address and weekly hours; Friday and Saturday close at 2 AM, Sunday at 1 AM.

- **Official link:** [https://www.tonyniks.com/contact/](https://www.tonyniks.com/contact/)

### 53. The Buena Vista Cafe

- **Status:** Official match.

- **Category / neighborhood:** Historic cafe / bar · Fisherman’s Wharf.

- **Address check:** `2765 Hyde St, San Francisco, CA 94109` — [official source](https://www.thebuenavista.com/home/home.html).

- **Published source line:** “2765 Hyde St (at Beach), San Francisco, CA 94109. Mon–Thu 9am – 11pm (kitchen closed 9:30pm); Fri 9am – 12am (kitchen closed 9:30pm); Sat 8am – 12am (kitchen closed 9:30pm); Sun 8am – 11pm (kitchen closed 9:30pm).”

- **Late-night result:** Friday: 9:00 AM–12:00 AM; kitchen closes 9:30 PM; Saturday: 8:00 AM–12:00 AM; kitchen closes 9:30 PM. This is why the record passes the >11 PM test.

- **Transit screen:** 30 Stockton / 28 19th Ave to North Point & Hyde (both until midnight) — Both the 30 Stockton and the 28 19th Avenue stop at North Point St & Hyde St, one block from Hyde & Beach, and both end around midnight; from the origin the 28 is a one-seat ride from 19th Ave & Judah. There is no overnight line at the Wharf, so plan the return leg with the live planner. Mapped lines: 28, 30.

- **Manual review flags:** Qualifies only under the midnight policy (Friday and Saturday close at 12 AM); the kitchen closes at 9:30 PM and the last buses leave around the same time the bar closes.

- **Verification method:** Official site checked for address and weekly bar/kitchen hours; Friday and Saturday close at midnight.

- **Official link:** [https://www.thebuenavista.com/home/home.html](https://www.thebuenavista.com/home/home.html)

### 54. In-N-Out Burger (Fisherman’s Wharf)

- **Status:** Official match.

- **Category / neighborhood:** Burgers / late-night food · Fisherman’s Wharf.

- **Address check:** `333 Jefferson St, San Francisco, CA 94133` — [official source](https://locations.in-n-out.com/154).

- **Published source line:** “San Francisco CA – 333 Jefferson, 94133. On Jefferson W of Jones; By Fisherman’s Wharf. Normal Hours of Operation: Sunday – Thursday 10:30 a.m. – 1:00 a.m.; Friday – Saturday 10:30 a.m. – 1:30 a.m. This location does not have a drive-thru.”

- **Late-night result:** Friday: 10:30 AM–1:30 AM; Saturday: 10:30 AM–1:30 AM; Sunday: 10:30 AM–1:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 28 19th Ave / 30 Stockton to North Point (both until midnight) — The 28 19th Avenue stops at North Point St & Jones St and North Point St & Mason St, two blocks south of Jefferson & Jones; the 30 Stockton reaches North Point St & Hyde St. Both end around midnight and no overnight line serves the Wharf, so use the live planner for the return leg. Mapped lines: 28, 30.

- **Manual review flags:** Chain fast-food counter; Muni service near the Wharf ends around midnight, well before the 1:00–1:30 AM close.

- **Verification method:** Official location page checked for address and weekly hours; Friday and Saturday close at 1:30 AM, Sunday at 1 AM.

- **Official link:** [https://locations.in-n-out.com/154](https://locations.in-n-out.com/154)

### 55. Churchill

- **Status:** Official match.

- **Category / neighborhood:** Cocktail bar · Duboce Triangle / Upper Market.

- **Address check:** `198 Church St, San Francisco, CA` — [official source](https://www.churchillsf.com/).

- **Published source line:** “198 CHURCH ST @ MARKET, SAN FRANCISCO, CA. HOURS: sun–thur 4pm–12am; fri–sat 4pm–2am. HAPPY HOUR: EVERYDAY TIL 7PM.”

- **Late-night result:** Friday: 4:00 PM–2:00 AM; Saturday: 4:00 PM–2:00 AM; Sunday: 4:00 PM–12:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** N Judah to Church Station / 22 Fillmore / N Owl — The N Judah Church Station, the 22 Fillmore stop at Church St & Market St, and the N Owl stop at Church St & Duboce Ave are all within a block of Church & Market; use the live planner for the final steps. Mapped lines: N, 22, NOWL.

- **Manual review flags:** Sunday qualifies only under the midnight policy; the official page prints no ZIP code.

- **Verification method:** Official site checked for address and weekly hours; Friday and Saturday close at 2 AM, Sunday at midnight.

- **Official link:** [https://www.churchillsf.com/](https://www.churchillsf.com/)

### 56. The Cafe

- **Status:** Official match.

- **Category / neighborhood:** LGBTQ+ nightclub / bar · Castro.

- **Address check:** `2369 Market St, San Francisco, CA` — [official source](https://cafesf.com/).

- **Published source line:** “2369 Market St (across from Castro Muni Station). Hours of Operation: Thursday–Saturday, 9pm–2am, See Events Below for Extended Hours & Special Events.”

- **Late-night result:** Friday: 9:00 PM–2:00 AM; Saturday: 9:00 PM–2:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** N Judah to Castro Station / 24 Divisadero — The venue sits across from the N Judah Castro Station at Market & Castro; the 24 Divisadero (24 hours) stops at Castro St & 17th St and Castro St & 18th St. Use the live planner for the return leg. Mapped lines: N, 24.

- **Manual review flags:** 21+ nightclub with event-night covers; Sunday through Wednesday hours are not published and depend on special events.

- **Verification method:** Official site checked for address and published Thursday–Saturday hours; Friday and Saturday close at 2 AM.

- **Official link:** [https://cafesf.com/](https://cafesf.com/)

### 57. The Edge

- **Status:** Official match.

- **Category / neighborhood:** LGBTQ+ neighborhood bar · Castro.

- **Address check:** `4149 18th St, San Francisco, CA 94114` — [official source](https://edgesf.com/).

- **Published source line:** “HOURS: Mon: 2pm–2am; Tues: 2pm–1am; Wed: 2pm–2am; Thurs: 2pm–1am; Fri: 2pm–2am; Sat–Sun: 12pm–2am. LOCATION: 4149 18th St. San Francisco, CA 94114.”

- **Late-night result:** Friday: 2:00 PM–2:00 AM; Saturday: 12:00 PM–2:00 AM; Sunday: 12:00 PM–2:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** N Judah to Castro Station / 24 Divisadero + walk — The 24 Divisadero (24 hours) stops at Castro St & 18th St, one block east of 18th & Collingwood; the N Judah Castro Station is about three blocks away. Use the live planner for the final walk. Mapped lines: N, 24.

- **Manual review flags:** Weekly theme nights (e.g., Musical Mondays) are listed on the official site and can change the crowd and entry experience.

- **Verification method:** Official site checked for address and weekly hours; all three weekend days close at 2 AM.

- **Official link:** [https://edgesf.com/](https://edgesf.com/)

### 58. Blackbird Bar

- **Status:** Official match.

- **Category / neighborhood:** Cocktail bar · Upper Market / Castro.

- **Address check:** `2124 Market St, San Francisco, CA 94114` — [official source](https://www.blackbirdbar.com/location/blackbird-bar).

- **Published source line:** “2124 Market Street, San Francisco, CA 94114. (415) 872-5310. Monday 5pm–11pm; Tuesday 5pm–12pm; Wednesday 5pm–12pm; Thursday 5pm–12pm; Friday 4pm–2am; Saturday 2pm–2am; Sunday 2pm–11pm. Closed Thanksgiving & Christmas.”

- **Late-night result:** Friday: 4:00 PM–2:00 AM; Saturday: 2:00 PM–2:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** N Judah to Church Station / 22 Fillmore / N Owl + walk — The N Judah Church Station and the 22 Fillmore stop at Church St & Market St are about two blocks east of 2124 Market (near 14th/Church); the N Owl stops at Church St & Duboce Ave and Market St & Dolores St overnight. Use the live planner for the final walk. Mapped lines: N, 22, NOWL.

- **Manual review flags:** The official page prints “12pm” for the Tuesday–Thursday close, almost certainly meaning midnight; those days are not counted and Friday/Saturday are the qualifying days.

- **Verification method:** Official location page checked for address and weekly hours; Friday and Saturday close at 2 AM.

- **Official link:** [https://www.blackbirdbar.com/location/blackbird-bar](https://www.blackbirdbar.com/location/blackbird-bar)

### 59. Hot Cookie (Castro)

- **Status:** Official match.

- **Category / neighborhood:** Bakery / late-night dessert · Castro.

- **Address check:** `407 Castro St, San Francisco, CA` — [official source](https://hotcookie.com/stores/castro-sf).

- **Published source line:** “407 Castro, San Francisco. Fri–Sat: 11am–2am | Sun–Thu: 11am–11pm.”

- **Late-night result:** Friday: 11:00 AM–2:00 AM; Saturday: 11:00 AM–2:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** N Judah to Castro Station / 24 Divisadero — The N Judah Castro Station at Market & Castro is a block from 407 Castro, and the 24 Divisadero (24 hours) stops at Castro St & 17th St and Castro St & 18th St. Use the live planner for the return leg. Mapped lines: N, 24.

- **Manual review flags:** Cookie and ice-cream counter, not a bar; the Polk Street store closes at 1 AM Fri–Sat and is not included.

- **Verification method:** Official store page checked for address and weekly hours; Friday and Saturday close at 2 AM.

- **Official link:** [https://hotcookie.com/stores/castro-sf](https://hotcookie.com/stores/castro-sf)

### 60. Trick Dog

- **Status:** Official match.

- **Category / neighborhood:** Cocktail bar / food · Mission.

- **Address check:** `3010 20th St, San Francisco, CA` — [official source](https://www.trickdogbar.com/).

- **Published source line:** “3010 20th Street, San Francisco. Sunday–Thursday: 4pm–12am, food til 10pm. Friday + Saturday: 4pm–2am, food til midnight.”

- **Late-night result:** Friday: 4:00 PM–2:00 AM; food until 12:00 AM; Saturday: 4:00 PM–2:00 AM; food until 12:00 AM; Sunday: 4:00 PM–12:00 AM; food until 10:00 PM. This is why the record passes the >11 PM test.

- **Transit screen:** 14 Mission / 22 Fillmore + longer walk — The 14 Mission (24 hours) stops at Mission St & 20th St about half a mile west of 20th & Florida, and the 22 Fillmore (24 hours) at 16th St & Bryant St about five blocks north; the 12 Folsom and 27 Bryant stop running by 10 PM. Use the live planner for the final walk. Mapped lines: 14, 22.

- **Manual review flags:** Sunday qualifies only under the midnight policy; the nearest 24-hour lines are a longer walk away.

- **Verification method:** Official site checked for address and weekly hours; Friday and Saturday close at 2 AM, Sunday at midnight.

- **Official link:** [https://www.trickdogbar.com/](https://www.trickdogbar.com/)

### 61. Bender’s Bar & Grill

- **Status:** Official match.

- **Category / neighborhood:** Dive bar / kitchen · Mission.

- **Address check:** `806 S Van Ness Ave, San Francisco, CA 94110` — [official source](https://bendersbar.com/).

- **Published source line:** “806 S. Van Ness Ave, San Francisco, CA 94110. BUSINESS HOURS TUES–SUN 2PM–2AM. KITCHEN HOURS TUES–SAT 4–11PM. SUN – PIZZA! 5–9PM (hours subject to change).”

- **Late-night result:** Friday: 2:00 PM–2:00 AM; kitchen 4:00 PM–11:00 PM; Saturday: 2:00 PM–2:00 AM; kitchen 4:00 PM–11:00 PM; Sunday: 2:00 PM–2:00 AM; pizza 5:00 PM–9:00 PM. This is why the record passes the >11 PM test.

- **Transit screen:** 14 Mission / 49 Van Ness-Mission + one-block walk — The 14 Mission (24 hours) and 49 Van Ness/Mission (until midnight) stop at Mission St & 18th St and Mission St & 20th St, one block west of South Van Ness & 19th; use the live planner for the return leg. Mapped lines: 14, 49.

- **Manual review flags:** Monday is absent from the official hours block and is recorded as closed; the site adds “hours subject to change.”

- **Verification method:** Official site checked for address and Tuesday–Sunday hours; all three weekend days close at 2 AM.

- **Official link:** [https://bendersbar.com/](https://bendersbar.com/)

### 62. Kilowatt

- **Status:** Official match.

- **Category / neighborhood:** Dive bar / live music · Mission.

- **Address check:** `3160 16th St, San Francisco, CA 94103` — [official source](https://kilowattbar.com/).

- **Published source line:** “LOCATION: 3160 16TH STREET (@ ALBION), SAN FRANCISCO, CA 94103. OPENING HOURS: MON–FRI: 5PM–2AM; SAT–SUN: 1PM–2AM. PHONE: 415-861-2595.”

- **Late-night result:** Friday: 5:00 PM–2:00 AM; Saturday: 1:00 PM–2:00 AM; Sunday: 1:00 PM–2:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 22 Fillmore (16th & Valencia) / 14 Mission / 49 — The 22 Fillmore (24 hours) stops at 16th St & Valencia St half a block from 16th & Albion; the 14 Mission (24 hours) and 49 Van Ness/Mission (until midnight) stop at Mission St & 16th St. Use the live planner for the return leg. Mapped lines: 22, 14, 49.

- **Manual review flags:** Live shows and DJ nights are listed on the official events page and may carry a cover.

- **Verification method:** Official site checked for address and weekly hours; all three weekend days close at 2 AM.

- **Official link:** [https://kilowattbar.com/](https://kilowattbar.com/)

### 63. Casanova Lounge

- **Status:** Official match.

- **Category / neighborhood:** Neighborhood bar / DJ nights · Mission.

- **Address check:** `527 Valencia St, San Francisco, CA 94110` — [official source](https://www.casanovasf.com/).

- **Published source line:** “527 VALENCIA ST, SF CA 94110. DAILY 5pm – 2am. HAPPY HOUR till 7pm.”

- **Late-night result:** Friday: 5:00 PM–2:00 AM; Saturday: 5:00 PM–2:00 AM; Sunday: 5:00 PM–2:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 22 Fillmore (16th & Valencia) / 14 Mission / 49 — The 22 Fillmore (24 hours) stops at 16th St & Valencia St, steps from 527 Valencia; the 14 Mission (24 hours) and 49 Van Ness/Mission (until midnight) stop at Mission St & 16th St. Use the live planner for the return leg. Mapped lines: 22, 14, 49.

- **Manual review flags:** The official page is a single-screen site with one daily hours line; holiday exceptions are not published.

- **Verification method:** Official site checked for address and daily hours; every day closes at 2 AM.

- **Official link:** [https://www.casanovasf.com/](https://www.casanovasf.com/)

### 64. Lone Star Saloon

- **Status:** Official match.

- **Category / neighborhood:** LGBTQ+ bar / patio · SoMa.

- **Address check:** `1354 Harrison St, San Francisco, CA 94103` — [official source](https://www.lonestarsf.com/).

- **Published source line:** “1354 Harrison St, San Francisco, CA 94103. (415) 863-9999. Hours: Mon–Sat 4p–2a; Sun 2p–2a.”

- **Late-night result:** Friday: 4:00 PM–2:00 AM; Saturday: 4:00 PM–2:00 AM; Sunday: 2:00 PM–2:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 14 Mission / N Owl on Market + walk — Harrison between 9th and 10th is about three blocks south of the 14 Mission (24 hours) stops at Mission St & 9th St and Mission St & 11th St, and of the N Owl stop at Market St & 9th St; the 12 Folsom ends at 10 PM. Use the live planner for the final walk. Mapped lines: 14, NOWL.

- **Manual review flags:** 21+ bar with event nights; the walk from Mission/Market Street crosses several SoMa blocks late at night.

- **Verification method:** Official site checked for address and weekly hours; all three weekend days close at 2 AM.

- **Official link:** [https://www.lonestarsf.com/](https://www.lonestarsf.com/)

### 65. SF Eagle

- **Status:** Official match.

- **Category / neighborhood:** LGBTQ+ bar / beer garden · SoMa.

- **Address check:** `398 12th St, San Francisco, CA 94103` — [official source](https://www.sf-eagle.com/visit/).

- **Published source line:** “398 12th St, San Francisco, CA 94103. HOURS: Monday 6PM – 12AM; Tuesday Closed; Wed – Thu 6PM – 12AM; Fri – Sat 2PM – 2AM; Sunday 1PM – 12AM.”

- **Late-night result:** Friday: 2:00 PM–2:00 AM; Saturday: 2:00 PM–2:00 AM; Sunday: 1:00 PM–12:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 14 Mission / 49 / N Owl at Market & South Van Ness + walk — The 14 Mission (24 hours) stops at Mission St & South Van Ness Ave and Mission St & 11th St, the 49 (until midnight) at South Van Ness Ave & Market St, and the N Owl at Market St & South Van Ness Ave, all about four blocks north of 12th & Harrison. Use the live planner for the final walk. Mapped lines: 14, 49, NOWL.

- **Manual review flags:** Closed Tuesday; Sunday qualifies only under the midnight policy; event nights can add a cover.

- **Verification method:** Official Visit page checked for address and weekly hours; Friday and Saturday close at 2 AM, Sunday at midnight.

- **Official link:** [https://www.sf-eagle.com/visit/](https://www.sf-eagle.com/visit/)

### 66. Hole in the Wall Saloon

- **Status:** Official match with documented gap.

- **Category / neighborhood:** LGBTQ+ neighborhood bar · SoMa.

- **Address check:** `1369 Folsom St, San Francisco, CA` — [official source](https://holeinthewallsaloon.com/).

- **Published source line:** “1369 Folsom Street, SF. Your Friendly Neighborhood Gay Biker’s Bar. Open MON > FRI 2pm ’til 2am; SAT + SUN > noon ’til 2am.”

- **Late-night result:** Friday: 2:00 PM–2:00 AM; Saturday: 12:00 PM–2:00 AM; Sunday: 12:00 PM–2:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 14 Mission / N Owl at Market & 9th + walk — Folsom between 9th and 10th is about two blocks south of the 14 Mission (24 hours) stops at Mission St & 9th St and Mission St & 11th St and the N Owl stop at Market St & 9th St; the 12 Folsom ends at 10 PM. Use the live planner for the final walk. Mapped lines: 14, NOWL.

- **Manual review flags:** The venue’s own domain redirects to a page hosted at blackwolfmetal.com titled “HITWS”; the hours and address were read there, so confirm on site.

- **Verification method:** Venue domain resolved to a redirected official page; address and weekly hours transcribed from it.

- **Official link:** [https://holeinthewallsaloon.com/](https://holeinthewallsaloon.com/)

### 67. The Willows

- **Status:** Official match.

- **Category / neighborhood:** Gastropub / beer bar · SoMa.

- **Address check:** `1582 Folsom St, San Francisco, CA 94103` — [official source](https://thewillowssf.com/).

- **Published source line:** “1582 Folsom Street, San Francisco, CA 94103. Phone: 415.226.7768. Hours: Monday–Thursday: 11:30 AM to midnight; Friday: 11:30 AM to 2:00 AM; Saturday: 11:00 AM to 2:00 AM; Sunday: 11:00 AM to midnight.”

- **Late-night result:** Friday: 11:30 AM–2:00 AM; Saturday: 11:00 AM–2:00 AM; Sunday: 11:00 AM–12:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 14 Mission / 49 / N Owl at Market & South Van Ness + walk — Folsom at 12th is about three blocks south of the 14 Mission (24 hours) stop at Mission St & South Van Ness Ave, the 49 (until midnight) at South Van Ness Ave & Market St, and the N Owl at Market St & South Van Ness Ave. Use the live planner for the final walk. Mapped lines: 14, 49, NOWL.

- **Manual review flags:** Sunday qualifies only under the midnight policy.

- **Verification method:** Official site checked for address and weekly hours; Friday and Saturday close at 2 AM, Sunday at midnight.

- **Official link:** [https://thewillowssf.com/](https://thewillowssf.com/)

### 68. The Hotel Utah Saloon

- **Status:** Official match.

- **Category / neighborhood:** Historic saloon / music venue · SoMa.

- **Address check:** `500 4th St, San Francisco, CA 94107` — [official source](https://hotelutah.com/).

- **Published source line:** “500 4th St. S.F., CA 94107. 415-546-6300. HOURS: Open Daily at 11:00 AM; bar open until midnight (or later on show nights). Kitchen hours 11:00AM to 11PM.”

- **Late-night result:** Friday: 11:00 AM–12:00 AM (later on show nights); kitchen 11:00 AM–11:00 PM; Saturday: 11:00 AM–12:00 AM (later on show nights); kitchen 11:00 AM–11:00 PM; Sunday: 11:00 AM–12:00 AM (later on show nights); kitchen 11:00 AM–11:00 PM. This is why the record passes the >11 PM test.

- **Transit screen:** N Judah to 4th & King / 30 Stockton / N Owl (Townsend & 4th) — The N Judah ends at 4th & King two blocks south of 4th & Bryant, the 30 Stockton (until midnight) stops at 4th St & Folsom St and Townsend St & 4th St, and the N Owl stops at Townsend St & 4th St overnight. Use the live planner for the final walk. Mapped lines: N, 30, NOWL.

- **Manual review flags:** Qualifies under the midnight policy; the official page says the bar may stay open later on show nights, and most shows are ticketed and 21+.

- **Verification method:** Official site checked for address and daily bar/kitchen hours; every day lists a midnight bar close.

- **Official link:** [https://hotelutah.com/](https://hotelutah.com/)

### 69. Tempest Bar & Box Kitchen

- **Status:** Official match.

- **Category / neighborhood:** Dive bar / kitchen · SoMa.

- **Address check:** `431 Natoma St, San Francisco, CA 94103` — [official source](https://tempest.pourguys.com/).

- **Published source line:** “Location: 431 Natoma St, San Francisco, CA 94103. Hours: Mon, Tue, Wed, Thur, Fri 11:00 AM – 2:00 AM; Sun, Sat 12:00 PM – 2:00 AM. Call us at (415)-495-1863.”

- **Late-night result:** Friday: 11:00 AM–2:00 AM; Saturday: 12:00 PM–2:00 AM; Sunday: 12:00 PM–2:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** N Judah to Powell / 14 Mission / N Owl on Market — Natoma between 5th and 6th is a block south of the 14 Mission (24 hours) stops at Mission St & 5th St and Mission St & 6th St, two blocks from the N Judah Powell Station, and near the N Owl stops at Market St & 5th St and Market St & 6th St. Use the live planner for the final walk. Mapped lines: N, 14, NOWL.

- **Manual review flags:** The official page is a subdomain of the operator’s group site (pourguys.com) built on a restaurant-website platform; the alley location is dark late at night.

- **Verification method:** Official venue page checked for address and weekly hours; all three weekend days close at 2 AM.

- **Official link:** [https://tempest.pourguys.com/](https://tempest.pourguys.com/)

### 70. Connecticut Yankee

- **Status:** Official match.

- **Category / neighborhood:** Sports bar / restaurant · Potrero Hill.

- **Address check:** `100 Connecticut St, San Francisco, CA 94107` — [official source](https://connecticutyankee.pourguys.com/).

- **Published source line:** “Location: 100 Connecticut St, San Francisco, CA 94107. Hours: Thur, Fri, Sat 11:00 AM – 1:00 AM; Sun, Mon, Tue, Wed 11:00 AM – 11:00 PM. Call us at (415)-552-4440.”

- **Late-night result:** Friday: 11:00 AM–1:00 AM; Saturday: 11:00 AM–1:00 AM. This is why the record passes the >11 PM test.

- **Transit screen:** 22 Fillmore (24 hours) to 16th & Missouri + one-block walk — The 22 Fillmore stops at 16th St & Missouri St and 16th St & Wisconsin St, one block north of Connecticut & 17th; from the origin, ride the N Judah to Church Station and transfer to the outbound 22 at Church St & Market St. The 19 Polk ends at 10 PM. Use the live planner for the return leg. Mapped lines: 22, N.

- **Manual review flags:** The official page is a subdomain of the operator’s group site (pourguys.com); Sunday closes at 11 PM and does not qualify.

- **Verification method:** Official venue page checked for address and weekly hours; Friday and Saturday close at 1 AM.

- **Official link:** [https://connecticutyankee.pourguys.com/](https://connecticutyankee.pourguys.com/)

## What this does not verify

The official schedule verifies the published business hours at the time of review; it does not verify a future holiday schedule, last call, kitchen availability, cover charge, door policy, capacity, accessibility conditions, or a live transit disruption. Those are deliberately not inferred. Open the official page and use the live route link before leaving.
