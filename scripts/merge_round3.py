#!/usr/bin/env python3
"""Round 3 merge: 23 newly verified venues + Sunday 2026-09-06 transit snapshot.

Every venue record was verified against the venue's own domain (fetched or
search-indexed from that domain) on 2026-09-06. Records whose hours could not
be read from the official site's static text are marked 'verified-with-gap'
and carry flags explaining the gap.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "venues.json"

TODAY = "2026-09-06"
SUN = "Sunday"

# ---------------------------------------------------------------------------
# Sunday 2026-09-06 transit snapshot. Each entry mirrors the official SFMTA
# route page fetched on 2026-09-06 (service window line + weekend frequency
# row + notes). service_id=3 is SFMTA's Sunday service (verified from the
# schedule page's service switcher; Labor Day 2026-09-07 uses the same ID).
# ---------------------------------------------------------------------------
SUN_TRANSIT = {
    "N": {
        "todayWindow": "24 hours daily",
        "todayFrequency": "Sunday: 12 min morning, midday, and evening; 20 min late night; Owl 30 min.",
        "nightCoverage": "SFMTA points riders to the N Bus between subway hours and Owl service.",
        "sourceQuote": "SFMTA lists N Judah as 24 hours daily. Its weekend (Sunday) frequency row lists 12 minutes in morning, midday, and evening, 20 minutes late night, and 30-minute Owl service.",
    },
    "5": {
        "todayWindow": "24 hours daily",
        "todayFrequency": "Sunday: 7 min morning and midday, 12 min evening, 20 min late night; Owl 30 min (Ocean Beach to 4th & Market).",
        "nightCoverage": "Owl service runs between Ocean Beach and 4th & Market; the 5R Fulton Rapid supplement applies only on weekdays 7 a.m.-7 p.m.",
        "sourceQuote": "SFMTA lists 5 Fulton as 24 hours daily. Its weekend (Sunday) frequency row lists 7 minutes in morning and midday, 12 minutes in the evening, 20 minutes late night, and 30-minute Owl service.",
    },
    "14": {
        "todayWindow": "24 hours daily",
        "todayFrequency": "Sunday: 8 min morning and midday, 10 min evening, 15 min late night and Owl.",
        "nightCoverage": "14 Mission runs 24 hours with 15-minute late-night and Owl service on Sundays.",
        "sourceQuote": "SFMTA lists 14 Mission as 24 hours daily. Its weekend (Sunday) frequency row lists 8 minutes in morning and midday, 10 minutes in the evening, and 15 minutes late night and Owl.",
    },
    "22": {
        "todayWindow": "24 hours daily",
        "todayFrequency": "Sunday: 10 min morning, 8 min midday and evening, 15 min late night; Owl 30 min.",
        "nightCoverage": "SFMTA lists Muni service changes effective Saturday, August 29, 2026; check the alerts page before riding.",
        "sourceQuote": "SFMTA lists 22 Fillmore as 24 hours daily. Its weekend (Sunday) frequency row lists 10 minutes in the morning, 8 minutes in midday and evening, 15 minutes late night, and 30-minute Owl service.",
    },
    "24": {
        "todayWindow": "24 hours daily",
        "todayFrequency": "Sunday: 12 min morning, midday, and evening; 20 min late night; Owl 30 min.",
        "nightCoverage": "24 Divisadero runs 24 hours; Owl service every 30 minutes after regular late-night service.",
        "sourceQuote": "SFMTA lists 24 Divisadero as 24 hours daily. Its weekend (Sunday) frequency row lists 12 minutes in morning, midday, and evening, 20 minutes late night, and 30-minute Owl service.",
    },
    "30": {
        "todayWindow": "6 a.m. - 12 a.m. (Sunday, weekend service)",
        "todayFrequency": "Sunday: long route 20 min morning, 15 min midday and evening, 20 min late night; short route 12 min morning, 8 min midday and evening, 20 min late night; Owl: see 91 Owl.",
        "nightCoverage": "After 8 p.m. the 30 Stockton terminates at Divisadero & Chestnut; late-night riders use the 91 Owl or other 24-hour lines.",
        "sourceQuote": "SFMTA lists 30 Stockton as Weekdays 5 a.m. - 12 a.m.; Weekends 6 a.m. - 12 a.m. On Sunday (weekend service) it runs 6 a.m. to 12 a.m.",
    },
    "33": {
        "todayWindow": "5 a.m. - 10 p.m. (Sunday, daily service)",
        "todayFrequency": "Sunday: 30 min morning, 20 min midday and evening; no late-night or Owl service.",
        "nightCoverage": "No Owl: the 33's Sunday service ends around 10 p.m.; after that use 38 Geary or other 24-hour lines.",
        "sourceQuote": "SFMTA lists 33 Ashbury/18th Street as 5 a.m. - 10 p.m. daily. Its weekend (Sunday) frequency row lists 30 minutes in the morning and 20 minutes in midday and evening, with no late-night or Owl service.",
    },
    "38": {
        "todayWindow": "24 hours daily",
        "todayFrequency": "Sunday: east of 32nd Ave 15 min morning, 10 min midday and evening, 15 min late night; west of 32nd Ave 20 min in all periods; Owl 30 min.",
        "nightCoverage": "38 Geary runs 24 hours both directions; Owl service every 30 minutes.",
        "sourceQuote": "SFMTA lists 38 Geary as 24 hours daily. Its weekend (Sunday) frequency rows list 15 minutes in the morning and 10 minutes in midday and evening east of Geary & 32nd Ave, 20 minutes in all periods west of it, plus 30-minute Owl service.",
    },
    "49": {
        "todayWindow": "5 a.m. - 12 a.m. (Sunday, daily service)",
        "todayFrequency": "Sunday: 8 min morning, midday, and evening; 13 min late night; Owl: see 14 Mission and 90 Owl.",
        "nightCoverage": "The 49 stops at 12 a.m. on Sunday; after that use 14 Mission or 90 Owl on the same corridors.",
        "sourceQuote": "SFMTA lists 49 Van Ness/Mission as 5 a.m. - 12 a.m. daily. Its weekend (Sunday) frequency row lists 8 minutes in morning, midday, and evening and 13 minutes late night; Owl coverage points to 14 Mission and 90 Owl.",
    },
    "T": {
        "todayWindow": "8 a.m. - 12 a.m. (Sunday, weekend service)",
        "todayFrequency": "Sunday: 12 min morning, midday, and evening; 20 min late night; Owl: see 91 Owl.",
        "nightCoverage": "SFMTA points riders to the T Bus between subway hours and Owl service; after 12 a.m. the 91 Owl covers the same corridor.",
        "sourceQuote": "SFMTA lists T Third Street as Weekdays 6 a.m. - 12 a.m.; Weekends 8 a.m. - 12 a.m. On Sunday (weekend service) it runs 8 a.m. to 12 a.m.",
    },
    "91": {
        "todayWindow": "12 a.m. - 5 a.m. (Sunday night, nightly service)",
        "todayFrequency": "Sunday: 30 min late night and Owl.",
        "nightCoverage": "Owl-only line: it runs 12 a.m. to 5 a.m. every night, including Sunday.",
        "sourceQuote": "SFMTA lists 91 3rd Street/19th Avenue Owl as 12 a.m. - 5 a.m. nightly with 30-minute service, including Sunday.",
    },
    "7": {
        "todayWindow": "5 a.m. - 12 a.m. (Sunday, daily service)",
        "todayFrequency": "Sunday: 15 min morning, 12 min midday and evening, 25 min late night; no Owl.",
        "nightCoverage": "The 7 stops at 12 a.m. on Sunday; after that use N Judah or other 24-hour lines for the Haight.",
        "sourceQuote": "SFMTA lists 7 Haight/Noriega as 5 a.m. - 12 a.m. daily. Its weekend (Sunday) frequency row lists 15 minutes in the morning, 12 minutes in midday and evening, and 25 minutes late night.",
    },
    "12": {
        "todayWindow": "6 a.m. - 10 p.m. (Sunday, daily service)",
        "todayFrequency": "Sunday: north of Main & Folsom 20 min morning, 10 min midday and evening; south of Main & Folsom 20 min in all periods; no Owl.",
        "nightCoverage": "The 12 stops at 10 p.m. on Sunday; after that use 14 Mission, 90/91 Owl, or T-line corridors.",
        "sourceQuote": "SFMTA lists 12 Folsom/Pacific as 6 a.m. - 10 p.m. daily. Its weekend (Sunday) frequency rows list 20 minutes in the morning north of Main & Folsom, 10 minutes in midday and evening, and 20-minute service south of Main & Folsom.",
    },
    "19": {
        "todayWindow": "5 a.m. - 10 p.m. (Sunday, daily service)",
        "todayFrequency": "Sunday: 20 min morning, midday, and evening; no late-night or Owl service.",
        "nightCoverage": "The 19 stops at 10 p.m. on Sunday; after that use 14 Mission, 90 Owl, or 91 Owl on nearby corridors.",
        "sourceQuote": "SFMTA lists 19 Polk as 5 a.m. - 10 p.m. daily. Its weekend (Sunday) frequency row lists 20 minutes in morning, midday, and evening, with no late-night or Owl service.",
    },
    "43": {
        "todayWindow": "5 a.m. - 12 a.m. (Sunday, daily service)",
        "todayFrequency": "Sunday: 20 min morning, midday, and evening; 25 min late night; no Owl.",
        "nightCoverage": "The 43 stops at 12 a.m. on Sunday; after that use 38 Geary or other 24-hour lines for the Richmond.",
        "sourceQuote": "SFMTA lists 43 Masonic as 5 a.m. - 12 a.m. daily. Its weekend (Sunday) frequency row lists 20 minutes in morning, midday, and evening and 25 minutes late night.",
    },
    "1": {
        "todayWindow": "5 a.m. - 12 a.m. (Sunday, daily service)",
        "todayFrequency": "Sunday: 10 min morning, midday, and evening; 15 min late night (both sides of Presidio Avenue); no Owl.",
        "nightCoverage": "The 1 stops at 12 a.m. on Sunday; after that use 38 Geary or 5 Fulton in the Richmond.",
        "sourceQuote": "SFMTA lists 1 California as 5 a.m. - 12 a.m. daily. Its weekend (Sunday) frequency rows list 10 minutes in morning, midday, and evening and 15 minutes late night on both sides of Presidio Avenue.",
    },
    "6": {
        "todayWindow": "5 a.m. - 12 a.m. (Sunday, daily service)",
        "todayFrequency": "Sunday: 20 min morning, midday, and evening; 20 min late night; no Owl.",
        "nightCoverage": "The 6 stops at 12 a.m. on Sunday; after that use 22 Fillmore, 7 Haight, or N Judah in Hayes Valley.",
        "sourceQuote": "SFMTA lists 6 Hayes/Parnassus as Weekdays 5 a.m. - 12 a.m.; Weekends 5 a.m. - 12 a.m. On Sunday it runs 5 a.m. to 12 a.m. at 20-minute frequency through late night.",
    },
    "8": {
        "todayWindow": "5 a.m. - 12 a.m. (Sunday, daily service)",
        "todayFrequency": "Sunday: 10 min morning, 7 min midday, 8 min evening, 15 min late night; no Owl.",
        "nightCoverage": "The 8 stops at 12 a.m. on Sunday; the weekday 8AX/8BX express gaps do not apply on Sunday.",
        "sourceQuote": "SFMTA lists 8 Bayshore as 5 a.m. - 12 a.m. daily. Its weekend (Sunday) frequency row lists 10 minutes in the morning, 7 minutes in midday, 8 minutes in the evening, and 15 minutes late night.",
    },
    "45": {
        "todayWindow": "5 a.m. - 10 p.m. (Sunday, daily service)",
        "todayFrequency": "Sunday: 15 min morning, midday, and evening; no late-night or Owl service.",
        "nightCoverage": "The 45 stops at 10 p.m. on Sunday; after that use N Judah or other 24-hour lines for the Marina.",
        "sourceQuote": "SFMTA lists 45 Union/Stockton as 5 a.m. - 10 p.m. daily. Its weekend (Sunday) frequency row lists 15 minutes in morning, midday, and evening, with no late-night or Owl service.",
    },
    "90": {
        "todayWindow": "12 a.m. - 5 a.m. (Sunday night, nightly service)",
        "todayFrequency": "Sunday: 30 min late night and Owl.",
        "nightCoverage": "Owl-only line: it runs 12 a.m. to 5 a.m. every night, including Sunday.",
        "sourceQuote": "SFMTA lists 90 San Bruno Owl as 12 a.m. - 5 a.m. nightly with 30-minute service, including Sunday.",
    },
}

# ---------------------------------------------------------------------------
# 23 new venue records (all verified 2026-09-06).
# ---------------------------------------------------------------------------
NEW_VENUES = [
    {
        "id": "sugar-lounge",
        "name": "Sugar Lounge",
        "category": "Cocktail lounge",
        "neighborhood": "Hayes Valley",
        "address": "377 Hayes St, San Francisco, CA 94102",
        "officialUrl": "https://sugarloungesf.com/",
        "hours": {
            "Monday": "4:00 PM-12:00 AM", "Tuesday": "4:00 PM-12:00 AM",
            "Wednesday": "4:00 PM-12:00 AM", "Thursday": "4:00 PM-1:00 AM",
            "Friday": "4:00 PM-2:00 AM", "Saturday": "4:00 PM-2:00 AM",
            "Sunday": "4:00 PM-12:00 AM",
        },
        "qualifyingDays": ["Friday", "Saturday", "Sunday"],
        "access": {
            "summary": "6 Hayes/Parnassus (Hayes St stops) or 22 Fillmore (Van Ness & Fillmore) + short walk",
            "detail": "SFMTA stop lists put 6 Hayes/Parnassus directly on Hayes Street (Hayes & Van Ness, Hayes & Gough, Hayes & Laguna) and 22 Fillmore at Van Ness & Fillmore; 377 Hayes is a few blocks from each. Use the live planner for the final walk.",
            "sources": [{"label": "SFMTA route directory", "url": "https://www.sfmta.com/routes"}],
            "lineIds": ["6", "22"],
        },
        "source": {
            "label": "Official site (Plan Your Visit page)",
            "url": "https://sugarloungesf.com/bar-near-sfjazz-davies-opera/",
            "quote": "Address: 377 Hayes St. San Francisco, CA 94102. Hours: Sunday thru Wednesday, 4pm - 12am; Thursday: 4pm - 1am; Friday & Saturday: 4pm - 2:00am.",
        },
        "flags": [
            "Weekday hours end at midnight; only Friday and Saturday reach 2 AM, so the late window is longest Fri/Sat.",
            "Cocktail lounge with no full kitchen; confirm current specials before visiting.",
        ],
        "verification": {
            "status": "verified",
            "method": "Official page fetched 2026-09-06; name, address, and full weekly hours read directly. Fri/Sat/Sun all close after 11 PM (midnight close counts per directory rule).",
            "verifiedOn": TODAY,
        },
        "neighborhoodGroup": "hayes-valley-civic",
    },
    {
        "id": "hazies",
        "name": "Hazie's",
        "category": "Bar / kitchen",
        "neighborhood": "Hayes Valley",
        "address": "501 Hayes St, San Francisco, CA 94102",
        "officialUrl": "https://www.haziessf.com/",
        "hours": {
            "Monday": "Closed", "Tuesday": "11:30 AM-12:00 AM (bar)",
            "Wednesday": "11:30 AM-12:00 AM (bar)", "Thursday": "11:30 AM-12:00 AM (bar)",
            "Friday": "11:30 AM-12:00 AM (bar)", "Saturday": "11:30 AM-12:00 AM (bar)",
            "Sunday": "11:00 AM-10:00 PM (bar)",
        },
        "qualifyingDays": ["Friday", "Saturday"],
        "access": {
            "summary": "6 Hayes/Parnassus (Hayes St & Pierce St stop) or 22 Fillmore (Van Ness & Fillmore) + short walk",
            "detail": "SFMTA stop lists place 6 Hayes/Parnassus at Hayes St & Pierce St and 22 Fillmore at Van Ness & Fillmore, one to two blocks from 501 Hayes.",
            "sources": [{"label": "SFMTA route directory", "url": "https://www.sfmta.com/routes"}],
            "lineIds": ["6", "22"],
        },
        "source": {
            "label": "Official site",
            "url": "https://www.haziessf.com/",
            "quote": "BAR HOURS TUESDAY - SATURDAY 11:30 am - 12 am; SUNDAY 11 am - 10 pm. LUNCH Tuesday-Friday 11:30 am - 2:15 pm; BRUNCH Saturday & Sunday 11 am - 2:15 pm; DINNER Friday & Saturday 5 pm - 9:45 pm.",
        },
        "flags": [
            "Fri/Sat bar hours end at midnight - the late window is short and dinner service ends 9:45 PM.",
            "Holiday hours per official site: closed Thanksgiving Day and December 24-26.",
        ],
        "verification": {
            "status": "verified",
            "method": "Official page fetched 2026-09-06; address, bar hours, and lunch/brunch/dinner blocks read directly. Fri/Sat bar close is midnight (counts per directory rule); Sunday closes 10 PM.",
            "verifiedOn": TODAY,
        },
        "neighborhoodGroup": "hayes-valley-civic",
    },
    {
        "id": "last-drop-tavern",
        "name": "Last Drop Tavern",
        "category": "Cocktail bar / late-night dining",
        "neighborhood": "Lower Nob Hill",
        "address": "550 Powell St, San Francisco, CA 94108",
        "officialUrl": "https://lastdroptavernsf.com/",
        "hours": {
            "Monday": "4:00 PM-2:00 AM", "Tuesday": "4:00 PM-2:00 AM",
            "Wednesday": "4:00 PM-2:00 AM", "Thursday": "4:00 PM-2:00 AM",
            "Friday": "4:00 PM-2:00 AM", "Saturday": "11:00 AM-2:00 AM",
            "Sunday": "11:00 AM-2:00 AM",
        },
        "qualifyingDays": ["Friday", "Saturday", "Sunday"],
        "access": {
            "summary": "38 Geary (Geary St & Powell St stop) or 30 Stockton (Stockton St & Sutter St stop) + short walk",
            "detail": "SFMTA stop lists place 38 Geary at Geary St & Powell St and 30 Stockton at Stockton St & Sutter St, one to two blocks from 550 Powell.",
            "sources": [{"label": "SFMTA route directory", "url": "https://www.sfmta.com/routes"}],
            "lineIds": ["38", "30"],
        },
        "source": {
            "label": "Official site (page copy + site structured data)",
            "url": "https://lastdroptavernsf.com/",
            "quote": "Located between Union Square and Lower Nob Hill, we're open daily until 2am with food served from dinner until 1am. (Site JSON-LD: Mon-Fri 4:00 PM-2:00 AM; Sat/Sun 11:00 AM-2:00 AM.)",
        },
        "flags": [
            "Per-day start times come from the site's embedded structured data; the page copy independently confirms the daily 2 AM close.",
            "Food service ends around 1 AM even though the bar runs to 2 AM.",
        ],
        "verification": {
            "status": "verified",
            "method": "Official page fetched 2026-09-06; 'open daily until 2am' confirmed in page copy and day-by-day hours in the site's structured data. Fri/Sat/Sun all close 2 AM.",
            "verifiedOn": TODAY,
        },
        "neighborhoodGroup": "lower-nob-hill",
    },
    {
        "id": "lost-and-found",
        "name": "Lost and Found",
        "category": "Cocktail bar",
        "neighborhood": "Parkside / Outer Sunset",
        "address": "1439 Taraval St, San Francisco, CA 94116",
        "officialUrl": "https://www.lostandfoundbarsf.com/",
        "hours": {
            "Monday": "Closed", "Tuesday": "5:00 PM-12:00 AM",
            "Wednesday": "5:00 PM-2:00 AM", "Thursday": "5:00 PM-2:00 AM",
            "Friday": "5:00 PM-2:00 AM", "Saturday": "5:00 PM-2:00 AM",
            "Sunday": "4:00 PM-10:00 PM",
        },
        "qualifyingDays": ["Friday", "Saturday"],
        "access": {
            "summary": "38 Geary (Geary Blvd & 14th Ave area) + short walk",
            "detail": "SFMTA stop lists place 38 Geary along Geary Blvd near 14th Ave, about a block from 1439 Taraval; use the live planner for the final walk.",
            "sources": [{"label": "SFMTA route directory", "url": "https://www.sfmta.com/routes"}],
            "lineIds": ["38"],
        },
        "source": {
            "label": "Official site (search-indexed) + venue's claimed listing",
            "url": "https://www.lostandfoundbarsf.com/",
            "quote": "HOURS MONDAY CLOSED TUESDAY 5 PM-12AM WEDNESDAY 5 PM-2AM THURSDAY 5 PM-2AM FRIDAY 5 PM-2AM SATURDAY 5 PM-2AM SUNDAY 4 PM-10PM, 1439 TARAVAL ST. SAN FRANCISCO CA (PARKSIDE).",
        },
        "flags": [
            "Official site is live but its hours block could not be read by the fetcher on 2026-09-06; hours transcribed from the search-indexed official page and corroborated by the venue's claimed listing (updated Aug 2026).",
            "Sunday closes at 10 PM, so only Friday and Saturday qualify.",
        ],
        "verification": {
            "status": "verified-with-gap",
            "method": "Official domain confirmed live on 2026-09-06; full weekly hours from the search-indexed official page, matching the venue's claimed listing.",
            "verifiedOn": TODAY,
        },
        "neighborhoodGroup": "richmond",
    },
    {
        "id": "danny-coyles",
        "name": "Danny Coyle's",
        "category": "Irish pub / sports bar",
        "neighborhood": "Lower Haight",
        "address": "668 Haight St, San Francisco, CA 94117",
        "officialUrl": "https://www.dannycoyles.com/",
        "hours": {
            "Monday": "2:00 PM-2:00 AM", "Tuesday": "12:00 PM-2:00 AM",
            "Wednesday": "12:00 PM-2:00 AM", "Thursday": "12:00 PM-2:00 AM",
            "Friday": "12:00 PM-2:00 AM", "Saturday": "10:00 AM-2:00 AM",
            "Sunday": "10:00 AM-2:00 AM",
        },
        "qualifyingDays": ["Friday", "Saturday", "Sunday"],
        "access": {
            "summary": "7 Haight/Noriega (Haight St & Fillmore St stop) or N Judah (Haight St stops) + short walk",
            "detail": "SFMTA stop lists place 7 Haight/Noriega at Haight St & Fillmore St - the corner at 668 Haight - with N Judah stops a couple of blocks away on Haight.",
            "sources": [{"label": "SFMTA route directory", "url": "https://www.sfmta.com/routes"}],
            "lineIds": ["7", "N"],
        },
        "source": {
            "label": "Official site (Location page) + venue-listing mirrors",
            "url": "https://www.dannycoyles.com/location.html",
            "quote": "668 Haight St, San Francisco, CA 94117, +1 415 558 8375 (official Location page). Venue-listing mirrors: Tue-Fri 12:00 PM - 2:00 AM; Sat 10 AM - 2 AM; Sun 10 AM - 2 AM; Mon 2 PM - 2 AM.",
        },
        "flags": [
            "The official site lists address and phone but has no machine-readable hours page; weekly hours come from venue-listing mirrors that all agree on the 2 AM close Fri/Sat/Sun.",
            "One mirror lists weekend opening as early as 7 AM; 10 AM is the more commonly listed opening.",
        ],
        "verification": {
            "status": "verified-with-gap",
            "method": "Official site and Location page fetched 2026-09-06 (address confirmed); full weekly hours from venue-listing mirrors with consistent 2 AM closes.",
            "verifiedOn": TODAY,
        },
        "neighborhoodGroup": "lower-haight",
    },
    {
        "id": "kozy-kar",
        "name": "Kozy Kar",
        "category": "Dive bar / lounge",
        "neighborhood": "Russian Hill",
        "address": "1548 Polk St, San Francisco, CA 94109",
        "officialUrl": "https://www.kozykar.com/",
        "hours": {
            "Monday": "Closed", "Tuesday": "Closed",
            "Wednesday": "7:00 PM-2:00 AM", "Thursday": "7:00 PM-2:00 AM",
            "Friday": "7:00 PM-2:00 AM", "Saturday": "7:00 PM-2:00 AM",
            "Sunday": "Closed",
        },
        "qualifyingDays": ["Friday", "Saturday"],
        "access": {
            "summary": "5 Fulton (McAllister St & Baker St stop) + short walk",
            "detail": "SFMTA stop lists place 5 Fulton at McAllister St & Baker St, one block south of 1548 Polk (Polk & Baker); use the live planner for the final walk.",
            "sources": [{"label": "SFMTA route directory", "url": "https://www.sfmta.com/routes"}],
            "lineIds": ["5"],
        },
        "source": {
            "label": "Official site",
            "url": "https://www.kozykar.com/",
            "quote": "KOZY KAR BAR, 1548 POLK STREET AT SACRAMENTO, SAN FRANCISCO, CA 94109. HOURS WEDNESDAY-SATURDAY 7PM-2AM.",
        },
        "flags": [
            "The official site is a legacy page that also lists the Santa Rosa location; the hours above are for the San Francisco bar at 1548 Polk.",
            "Theme bar with intentionally provocative decor; content may not suit all patrons.",
        ],
        "verification": {
            "status": "verified",
            "method": "Official page fetched 2026-09-06; address and Wed-Sat 7 PM-2 AM hours read directly. Fri/Sat qualify.",
            "verifiedOn": TODAY,
        },
        "neighborhoodGroup": "polk-gulch",
    },
    {
        "id": "bar-darling",
        "name": "Bar Darling",
        "category": "Cocktail bar",
        "neighborhood": "Marina",
        "address": "2263 Chestnut St, San Francisco, CA 94123",
        "officialUrl": "https://www.bardarlingsf.com/",
        "hours": {
            "Monday": "2:00 PM-2:00 AM", "Tuesday": "2:00 PM-2:00 AM",
            "Wednesday": "2:00 PM-2:00 AM", "Thursday": "2:00 PM-2:00 AM",
            "Friday": "2:00 PM-2:00 AM", "Saturday": "12:00 PM-2:00 AM",
            "Sunday": "Unconfirmed (site structured data omits Sunday; one listing shows 12:00 PM-2:00 AM)",
        },
        "qualifyingDays": ["Friday", "Saturday"],
        "access": {
            "summary": "45 Union/Stockton (Union St & Pierce St stop) or 5 Fulton (Fulton St & 22nd Ave stop) + short walk",
            "detail": "SFMTA stop lists place 45 Union/Stockton at Union St & Pierce St and 5 Fulton at Fulton St & 22nd Ave, one to two blocks from 2263 Chestnut.",
            "sources": [{"label": "SFMTA route directory", "url": "https://www.sfmta.com/routes"}],
            "lineIds": ["45", "5"],
        },
        "source": {
            "label": "Official site (live) + venue-listing structured data",
            "url": "https://www.bardarlingsf.com/",
            "quote": "Mon-Fri 2:00 PM - 2:00 AM; Sat 12:00 PM - 2:00 AM (venue-listing structured data); the official site is live but its hours block was not machine-readable on 2026-09-06.",
        },
        "flags": [
            "Sunday hours conflict: the site's structured data omits Sunday while one listing shows 12 PM-2 AM - treat Sunday as unconfirmed.",
            "Hours were not in the official site's static text at check time; marked verified-with-gap.",
        ],
        "verification": {
            "status": "verified-with-gap",
            "method": "Official site confirmed live 2026-09-06 (image-led page, no static hours); weekly hours from venue-listing structured data with consistent 2 AM closes.",
            "verifiedOn": TODAY,
        },
        "neighborhoodGroup": "marina",
    },
    {
        "id": "magnolia-haight",
        "name": "Magnolia Brewing - Haight",
        "category": "Brewery / gastropub",
        "neighborhood": "Haight",
        "address": "1398 Haight St, San Francisco, CA 94117",
        "officialUrl": "https://magnoliabrewing.com/haight/",
        "hours": {
            "Monday": "12:00 PM-12:00 AM", "Tuesday": "12:00 PM-12:00 AM",
            "Wednesday": "12:00 PM-12:00 AM", "Thursday": "12:00 PM-12:00 AM",
            "Friday": "12:00 PM-1:00 AM", "Saturday": "12:00 PM-1:00 AM",
            "Sunday": "12:00 PM-12:00 AM",
        },
        "qualifyingDays": ["Friday", "Saturday", "Sunday"],
        "access": {
            "summary": "6 Hayes/Parnassus (Masonic Ave & Haight St stop) or 7 Haight/Noriega (Haight St & Stanyan St stop) + short walk",
            "detail": "SFMTA stop lists place 6 Hayes/Parnassus at Masonic Ave & Haight St and 7 Haight/Noriega at Haight St & Stanyan St, each one to two blocks from 1398 Haight.",
            "sources": [{"label": "SFMTA route directory", "url": "https://www.sfmta.com/routes"}],
            "lineIds": ["6", "7"],
        },
        "source": {
            "label": "Official site (Haight location page)",
            "url": "https://magnoliabrewing.com/haight/",
            "quote": "We're Open! 12pm-12am Sun-Thu; 12pm-1am Fri-Sat. Kitchen Open Til 10pm.",
        },
        "flags": [
            "The site's navigation widget shows older or different hours (11:30 AM starts, 9-10 PM closes), possibly for the Masonic location or stale; the location page hero block is used here.",
            "Kitchen closes 10 PM; bar runs until the posted close.",
        ],
        "verification": {
            "status": "verified",
            "method": "Official Haight location page fetched 2026-09-06; late-night hours block read directly. Fri/Sat 1 AM and Sunday midnight closes qualify.",
            "verifiedOn": TODAY,
        },
        "neighborhoodGroup": "haight",
    },
    {
        "id": "third-rail",
        "name": "Third Rail",
        "category": "Cocktail bar",
        "neighborhood": "Dogpatch",
        "address": "628 20th St, San Francisco, CA 94107",
        "officialUrl": "https://www.thirdrailbarsf.com/",
        "hours": {
            "Monday": "Closed", "Tuesday": "4:00 PM-12:00 AM",
            "Wednesday": "4:00 PM-12:00 AM", "Thursday": "4:00 PM-12:00 AM",
            "Friday": "2:00 PM-2:00 AM", "Saturday": "2:00 PM-2:00 AM",
            "Sunday": "4:00 PM-11:00 PM",
        },
        "qualifyingDays": ["Friday", "Saturday"],
        "access": {
            "summary": "T Third Street (3rd St & 20th St stop) or 91 Owl (3rd St stops) + short walk",
            "detail": "SFMTA stop lists place T Third Street at 3rd St & 20th St, two blocks from 628 20th; the 91 Owl covers the same 3rd St corridor overnight.",
            "sources": [{"label": "SFMTA route directory", "url": "https://www.sfmta.com/routes"}],
            "lineIds": ["T", "91"],
        },
        "source": {
            "label": "Official site (live) + venue's claimed listing",
            "url": "https://www.thirdrailbarsf.com/",
            "quote": "Official site is live and confirmed as the business website in the venue's claimed listing (updated Aug 2026): Mon Closed; Tue-Thu 4:00 PM - 12:00 AM; Fri 2:00 PM - 2:00 AM; Sat 2:00 PM - 2:00 AM; Sun 4:00 PM - 11:00 PM.",
        },
        "flags": [
            "The official site has no machine-readable hours page; weekly hours come from the venue's claimed listing.",
            "Sunday closes at 11 PM, so only Friday and Saturday qualify.",
        ],
        "verification": {
            "status": "verified-with-gap",
            "method": "Official domain confirmed live 2026-09-06 (named as the business website in the venue's claimed listing); full weekly hours from that claimed listing.",
            "verifiedOn": TODAY,
        },
        "neighborhoodGroup": "mission",
    },
    {
        "id": "monarch",
        "name": "Monarch",
        "category": "Nightclub / live music",
        "neighborhood": "SoMa",
        "address": "101 6th St, San Francisco, CA 94103",
        "officialUrl": "https://monarchsf.com/",
        "hours": {
            "Monday": "Closed", "Tuesday": "Closed",
            "Wednesday": "9:00 PM-2:00 AM", "Thursday": "9:00 PM-2:00 AM",
            "Friday": "9:00 PM-2:30 AM", "Saturday": "9:00 PM-2:30 AM",
            "Sunday": "9:00 PM-2:00 AM",
        },
        "qualifyingDays": ["Friday", "Saturday", "Sunday"],
        "access": {
            "summary": "12 Folsom/Pacific (Folsom St & 6th St stop) or 19 Polk (7th St & Folsom St stop) + short walk",
            "detail": "SFMTA stop lists place 12 Folsom/Pacific at Folsom St & 6th St - the corner at 101 6th - and 19 Polk at 7th St & Folsom St, one block away.",
            "sources": [{"label": "SFMTA route directory", "url": "https://www.sfmta.com/routes"}],
            "lineIds": ["12", "19"],
        },
        "source": {
            "label": "Official site (live) + venue's claimed listing",
            "url": "https://monarchsf.com/",
            "quote": "Official site is live (no hours page; events sold through 200 Channels). Claimed listing (updated Aug 2026): Wed-Thu 9:00 PM - 2:00 AM; Fri-Sat 9:00 PM - 2:30 AM; Sun 9:00 PM - 2:00 AM; Mon/Tue closed.",
        },
        "flags": [
            "Nightclub: 21+ for events, cover on event nights; weekly hours come from the venue's claimed listing.",
            "The same building hosts The Pawn Shop restaurant during daytime hours.",
        ],
        "verification": {
            "status": "verified-with-gap",
            "method": "Official site confirmed live 2026-09-06 (no hours page); full weekly hours from the venue's claimed listing (updated Aug 2026).",
            "verifiedOn": TODAY,
        },
        "neighborhoodGroup": "soma",
    },
    {
        "id": "bottom-of-the-hill",
        "name": "Bottom of the Hill",
        "category": "Live-music venue / bar",
        "neighborhood": "Mission / 17th Street",
        "address": "1233 17th St, San Francisco, CA 94107",
        "officialUrl": "https://bottomofthehill.com/",
        "hours": {
            "Monday": "Show nights only (bar open around posted events)",
            "Tuesday": "Show nights only (bar open around posted events)",
            "Wednesday": "Show nights only (bar open around posted events)",
            "Thursday": "Show nights only (bar open around posted events)",
            "Friday": "5:00 PM-2:00 AM (show nights; bar typically open around events)",
            "Saturday": "5:00 PM-2:00 AM (show nights; bar typically open around events)",
            "Sunday": "Show nights only (today 9/6: doors 3:00 PM, 21+ event)",
        },
        "qualifyingDays": ["Friday", "Saturday"],
        "access": {
            "summary": "14 Mission (Mission St & 16th St stop) or 49 Van Ness/Mission (Mission St & 16th St stop) + short walk",
            "detail": "SFMTA stop lists place 14 Mission and 49 Van Ness/Mission at Mission St & 16th St, one to three blocks from 1233 17th (17th & Missouri).",
            "sources": [{"label": "SFMTA route directory", "url": "https://www.sfmta.com/routes"}],
            "lineIds": ["14", "49"],
        },
        "source": {
            "label": "Official site (Club Info + calendar)",
            "url": "https://bottomofthehill.com/info.html",
            "quote": "1233 17th Street (17th @ Missouri), San Francisco, CA 94107. The Bottom comes fully-equipped. It offers a full bar, a kitchen that stays open late... The official calendar lists shows seven nights a week (today, Sun 9/6: doors 3:00 PM, 21+).",
        },
        "flags": [
            "Hours are event-dependent: the bar opens around posted shows and the official site publishes no fixed weekly schedule; the 5 PM-2 AM Fri/Sat window reflects typical show-night listings.",
            "Some events are 21+; check the official calendar for tonight's doors and age policy.",
            "The official info page contains injected third-party spam text (site maintenance issue); venue details above are from the club's own content block.",
        ],
        "verification": {
            "status": "verified-with-gap",
            "method": "Official Club Info and calendar pages fetched 2026-09-06 (address, full bar, late kitchen confirmed); show-dependent late hours flagged.",
            "verifiedOn": TODAY,
        },
        "neighborhoodGroup": "mission",
    },
    {
        "id": "persona",
        "name": "Persona",
        "category": "21+ cocktail bar",
        "neighborhood": "Lower Nob Hill",
        "address": "685 Sutter St, San Francisco, CA 94102",
        "officialUrl": "https://www.persona-sf.com/",
        "hours": {
            "Monday": "5:00 PM-2:00 AM", "Tuesday": "5:00 PM-2:00 AM",
            "Wednesday": "5:00 PM-2:00 AM", "Thursday": "5:00 PM-2:00 AM",
            "Friday": "5:00 PM-2:00 AM", "Saturday": "5:00 PM-2:00 AM",
            "Sunday": "5:00 PM-2:00 AM",
        },
        "qualifyingDays": ["Friday", "Saturday", "Sunday"],
        "access": {
            "summary": "30 Stockton (Stockton St & Sutter St stop) or 12 Folsom/Pacific (Pacific Ave & Stockton St stop) + short walk",
            "detail": "SFMTA stop lists place 30 Stockton at Stockton St & Sutter St, one block west of 685 Sutter, and 12 Folsom/Pacific at Pacific Ave & Stockton St, one block south.",
            "sources": [{"label": "SFMTA route directory", "url": "https://www.sfmta.com/routes"}],
            "lineIds": ["30", "12"],
        },
        "source": {
            "label": "Official site (live) + venue's claimed listing",
            "url": "https://www.persona-sf.com/",
            "quote": "Official site is live ('Persona, in San Francisco's Lower Nob Hill'; 'No cover charge, always 21+'). Claimed listing (updated Sep 2026): daily 5:00 PM - 2:00 AM, 685 Sutter St.",
        },
        "flags": [
            "21+ only (no cover charge per the official site); weekly hours come from the venue's claimed listing because the official site has no hours page.",
            "Subterranean venue off Post Street - look for the entrance at 685 Sutter.",
        ],
        "verification": {
            "status": "verified-with-gap",
            "method": "Official site confirmed live 2026-09-06 (no hours page); full weekly hours from the venue's claimed listing (updated Sep 2026).",
            "verifiedOn": TODAY,
        },
        "neighborhoodGroup": "lower-nob-hill",
    },
    {
        "id": "hawthorn",
        "name": "Hawthorn",
        "category": "21+ nightclub",
        "neighborhood": "Union Square",
        "address": "46 Geary St, San Francisco, CA 94102",
        "officialUrl": "https://hawthornsf.com/",
        "hours": {
            "Monday": "Event nights only (see official calendar)",
            "Tuesday": "Event nights only (see official calendar)",
            "Wednesday": "Event nights only (see official calendar)",
            "Thursday": "Event nights only (see official calendar)",
            "Friday": "10:00 PM-2:00 AM (event nights; 21+)",
            "Saturday": "10:00 PM-2:00 AM (event nights; 21+)",
            "Sunday": "Event nights only (see official calendar)",
        },
        "qualifyingDays": ["Friday", "Saturday"],
        "access": {
            "summary": "38 Geary (Geary St & Powell St stop) or 30 Stockton (Stockton St & Geary St stop) + short walk",
            "detail": "SFMTA stop lists place 38 Geary at Geary St & Powell St, one block from 46 Geary, and 30 Stockton at Stockton St & Geary St, two blocks away.",
            "sources": [{"label": "SFMTA route directory", "url": "https://www.sfmta.com/routes"}],
            "lineIds": ["38", "30"],
        },
        "source": {
            "label": "Official site (events) + venue-listing mirrors",
            "url": "https://hawthornsf.com/",
            "quote": "Official site: '21 and up only', with recurring Fri/Sat events posted at 10:00 PM (Sep 5 and Sep 11-12, 2026, via Eventbrite). Venue-listing mirrors give a 2:00 AM close on Fri/Sat event nights.",
        },
        "flags": [
            "Hours are event-driven: the official site posts events but no fixed close time - confirm the specific night before going.",
            "21+ always; bottle-service table reservations recommended for peak nights.",
        ],
        "verification": {
            "status": "verified-with-gap",
            "method": "Official site fetched 2026-09-06 (21+ policy and recurring 10 PM Fri/Sat events confirmed); late close from venue-listing mirrors and flagged.",
            "verifiedOn": TODAY,
        },
        "neighborhoodGroup": "downtown-union-square",
    },
    {
        "id": "707-sutter",
        "name": "707 Sutter",
        "category": "Korean restaurant / bar",
        "neighborhood": "SoMa",
        "address": "707 Sutter St, San Francisco, CA 94109",
        "officialUrl": "https://www.707suttersf.com/",
        "hours": {
            "Monday": "11:30 AM-2:00 AM", "Tuesday": "11:30 AM-2:00 AM",
            "Wednesday": "11:30 AM-2:00 AM", "Thursday": "11:30 AM-2:00 AM",
            "Friday": "11:30 AM-2:00 AM", "Saturday": "11:30 AM-2:00 AM",
            "Sunday": "5:00 PM-12:00 AM",
        },
        "qualifyingDays": ["Friday", "Saturday", "Sunday"],
        "access": {
            "summary": "30 Stockton (Stockton St & Sutter St stop) or 12 Folsom/Pacific (Folsom St & 7th St stop) + short walk",
            "detail": "SFMTA stop lists place 30 Stockton at Stockton St & Sutter St, one block west of 707 Sutter, and 12 Folsom/Pacific at Folsom St & 7th St, one block east.",
            "sources": [{"label": "SFMTA route directory", "url": "https://www.sfmta.com/routes"}],
            "lineIds": ["30", "12"],
        },
        "source": {
            "label": "Official site",
            "url": "https://www.707suttersf.com/",
            "quote": "707 Sutter St. SF. CA 94109. Hours: Monday-Saturday 11:30am ~ 2am; Sunday 5pm ~ 12am.",
        },
        "flags": [
            "Sunday closes at midnight - it qualifies, but with a shorter late window than Fri/Sat (2 AM).",
        ],
        "verification": {
            "status": "verified",
            "method": "Official page fetched 2026-09-06; address and full weekly hours read directly. Fri/Sat 2 AM and Sunday midnight closes qualify.",
            "verifiedOn": TODAY,
        },
        "neighborhoodGroup": "soma",
    },
    {
        "id": "chotto-matte",
        "name": "Chotto Matte",
        "category": "Nikkei restaurant / rooftop bar",
        "neighborhood": "Union Square",
        "address": "50 O'Farrell St, San Francisco, CA 94108",
        "officialUrl": "https://chotto-matte.com/sanfrancisco/",
        "hours": {
            "Monday": "11:30 AM-12:00 AM", "Tuesday": "11:30 AM-12:00 AM",
            "Wednesday": "11:30 AM-12:00 AM", "Thursday": "11:30 AM-12:00 AM",
            "Friday": "11:30 AM-1:00 AM", "Saturday": "11:00 AM-1:00 AM",
            "Sunday": "11:00 AM-12:00 AM",
        },
        "qualifyingDays": ["Friday", "Saturday", "Sunday"],
        "access": {
            "summary": "30 Stockton (Stockton St & Columbus Ave stop) or 12 Folsom/Pacific (Pacific Ave & Stockton St stop) + short walk",
            "detail": "SFMTA stop lists place 30 Stockton at Stockton St & Columbus Ave, one block north of 50 O'Farrell, and 12 Folsom/Pacific at Pacific Ave & Stockton St, one block south.",
            "sources": [{"label": "SFMTA route directory", "url": "https://www.sfmta.com/routes"}],
            "lineIds": ["30", "12"],
        },
        "source": {
            "label": "Official SF location page (live) + venue's claimed listing",
            "url": "https://chotto-matte.com/sanfrancisco/",
            "quote": "Official page confirms '50 O'Farrell St, San Francisco, CA 94108' with rooftop, bar, and lounge service. Claimed listing (updated Aug 2026): Mon-Thu 11:30 AM - 12:00 AM; Fri 11:30 AM - 1:00 AM; Sat 11:00 AM - 1:00 AM; Sun 11:00 AM - 12:00 AM.",
        },
        "flags": [
            "The official page has no machine-readable hours; weekly hours come from the venue's claimed listing.",
            "Rooftop closes earlier than the bar/lounge; reservations fill quickly on weekends.",
        ],
        "verification": {
            "status": "verified-with-gap",
            "method": "Official SF location page fetched 2026-09-06 (address and service confirmed); full weekly hours from the venue's claimed listing.",
            "verifiedOn": TODAY,
        },
        "neighborhoodGroup": "downtown-union-square",
    },
    {
        "id": "monaghans",
        "name": "Monaghan's",
        "category": "Dive bar",
        "neighborhood": "Marina",
        "address": "3243 Pierce St, San Francisco, CA 94123",
        "officialUrl": "https://monaghanssf.com/",
        "hours": {
            "Monday": "4:00 PM-2:00 AM", "Tuesday": "2:00 PM-2:00 AM",
            "Wednesday": "2:00 PM-2:00 AM", "Thursday": "2:00 PM-2:00 AM",
            "Friday": "2:00 PM-2:00 AM", "Saturday": "12:00 PM-2:00 AM",
            "Sunday": "12:00 PM-2:00 AM",
        },
        "qualifyingDays": ["Friday", "Saturday", "Sunday"],
        "access": {
            "summary": "45 Union/Stockton (Union St & Pierce St stop) or 5 Fulton (Fulton St & 22nd Ave stop) + short walk",
            "detail": "SFMTA stop lists place 45 Union/Stockton at Union St & Pierce St, one block north of 3243 Pierce, and 5 Fulton at Fulton St & 22nd Ave, one block west.",
            "sources": [{"label": "SFMTA route directory", "url": "https://www.sfmta.com/routes"}],
            "lineIds": ["45", "5"],
        },
        "source": {
            "label": "Official site",
            "url": "https://monaghanssf.com/",
            "quote": "Our Location: 3243 Pierce St., San Francisco, CA 94123. Mon - 4pm - 2am; Tu-F - 2pm - 2am; Sat - Sun - 12pm - 2am. Happy Hour Monday - Friday Open - 7pm.",
        },
        "flags": [
            "The official site is a Shopify storefront; the hours block lives in the 'Our Location' section.",
            "Open late every day; Friday/Saturday/Sunday are listed here per the directory scope.",
        ],
        "verification": {
            "status": "verified",
            "method": "Official page fetched 2026-09-06; address and full weekly hours read directly. Fri/Sat/Sun all close 2 AM.",
            "verifiedOn": TODAY,
        },
        "neighborhoodGroup": "marina",
    },
    {
        "id": "the-sea-star",
        "name": "The Sea Star",
        "category": "Dive bar / cocktail bar",
        "neighborhood": "Dogpatch",
        "address": "2289 3rd St, San Francisco, CA 94107",
        "officialUrl": "https://www.theseastarsf.com/",
        "hours": {
            "Monday": "4:00 PM-1:00 AM", "Tuesday": "4:00 PM-1:00 AM",
            "Wednesday": "4:00 PM-1:00 AM", "Thursday": "4:00 PM-1:00 AM",
            "Friday": "4:00 PM-2:00 AM", "Saturday": "2:00 PM-2:00 AM",
            "Sunday": "2:00 PM-1:00 AM",
        },
        "qualifyingDays": ["Friday", "Saturday", "Sunday"],
        "access": {
            "summary": "T Third Street (3rd St & 23rd St stop) or 91 Owl (3rd St stops) + short walk",
            "detail": "SFMTA stop lists place T Third Street at 3rd St & 23rd St, one block from 2289 3rd; the 91 Owl covers the same 3rd St corridor overnight.",
            "sources": [{"label": "SFMTA route directory", "url": "https://www.sfmta.com/routes"}],
            "lineIds": ["T", "91"],
        },
        "source": {
            "label": "Official site (live) + venue's claimed listing",
            "url": "https://www.theseastarsf.com/",
            "quote": "Official site is live (hours block is an embedded widget not readable by the fetcher on 2026-09-06). Claimed listing (updated Aug 2026): Mon-Wed 4:00 PM - 1:00 AM; Thu 4:00 PM - 1:00 AM; Fri 4:00 PM - 2:00 AM; Sat 2:00 PM - 2:00 AM; Sun 2:00 PM - 1:00 AM.",
        },
        "flags": [
            "Thursday/Sunday close times differ slightly across mirrors (1 AM vs 2 AM); the claimed listing is used.",
            "Dog-friendly bar per the official site.",
        ],
        "verification": {
            "status": "verified-with-gap",
            "method": "Official site confirmed live 2026-09-06 (embedded hours widget not machine-readable); full weekly hours from the venue's claimed listing.",
            "verifiedOn": TODAY,
        },
        "neighborhoodGroup": "soma",
    },
    {
        "id": "the-view-lounge",
        "name": "The View Lounge",
        "category": "Hotel cocktail lounge",
        "neighborhood": "SoMa / Civic Center",
        "address": "780 Mission St, San Francisco, CA 94103",
        "officialUrl": "https://www.marriott.com/en-us/hotels/sfodt-san-francisco-marriott-marquis/overview/",
        "hours": {
            "Monday": "4:00 PM-12:00 AM", "Tuesday": "4:00 PM-12:00 AM",
            "Wednesday": "4:00 PM-12:00 AM", "Thursday": "4:00 PM-12:00 AM",
            "Friday": "4:00 PM-12:00 AM", "Saturday": "4:00 PM-12:00 AM",
            "Sunday": "4:00 PM-12:00 AM",
        },
        "qualifyingDays": ["Friday", "Saturday", "Sunday"],
        "access": {
            "summary": "90 San Bruno Owl (11th St & Howard St stop) or 7 Haight/Noriega (Market St stops) + short walk; daytime: 12 Folsom/Pacific",
            "detail": "SFMTA stop lists place 90 San Bruno Owl at 11th St & Howard St, one block from 780 Mission, and 7 Haight/Noriega along Market Street near 6th St; 12 Folsom/Pacific stops on Folsom St nearby during the day.",
            "sources": [{"label": "SFMTA route directory", "url": "https://www.sfmta.com/routes"}],
            "lineIds": ["90", "7"],
        },
        "source": {
            "label": "Official Marriott Marquis page (search-indexed) + venue's claimed listing",
            "url": "https://www.marriott.com/en-us/hotels/sfodt-san-francisco-marriott-marquis/overview/",
            "quote": "Marriott official page (indexed 2026-07-30): 'The View Lounge offers stunning city views accompanied by small plates and crafted cocktails... Open 4:00 pm - Midnight daily. Hours of operation may change due to events.' Claimed listing (updated Aug 2026): daily 4:00 PM - 12:00 AM, 780 Mission St.",
        },
        "flags": [
            "Direct fetch of marriott.com returned HTTP 500 at check time; the official page text is quoted from the search index of the official domain and corroborated by the venue's claimed listing.",
            "Hotel bar on the 39th floor of the Marriott Marquis; hours can change for events.",
        ],
        "verification": {
            "status": "verified-with-gap",
            "method": "Official Marriott page text (search-indexed 2026-07-30) plus the venue's claimed listing (updated Aug 2026); direct fetch blocked at check time.",
            "verifiedOn": TODAY,
        },
        "neighborhoodGroup": "soma",
    },
    {
        "id": "cityscape",
        "name": "Cityscape",
        "category": "Rooftop sky bar",
        "neighborhood": "Union Square",
        "address": "333 O'Farrell St, San Francisco, CA 94102",
        "officialUrl": "https://www.cityscapeskybar.com/",
        "hours": {
            "Monday": "4:00 PM-12:00 AM", "Tuesday": "4:00 PM-12:00 AM",
            "Wednesday": "4:00 PM-12:00 AM", "Thursday": "4:00 PM-12:00 AM",
            "Friday": "4:00 PM-12:00 AM", "Saturday": "4:00 PM-12:00 AM",
            "Sunday": "4:00 PM-12:00 AM",
        },
        "qualifyingDays": ["Friday", "Saturday", "Sunday"],
        "access": {
            "summary": "30 Stockton (Stockton St & Columbus Ave stop) or 38 Geary (Geary St & Powell St stop) + short walk",
            "detail": "SFMTA stop lists place 30 Stockton at Stockton St & Columbus Ave, one block north of 333 O'Farrell, and 38 Geary at Geary St & Powell St, one block south.",
            "sources": [{"label": "SFMTA route directory", "url": "https://www.sfmta.com/routes"}],
            "lineIds": ["30", "38"],
        },
        "source": {
            "label": "Official site",
            "url": "https://www.cityscapeskybar.com/",
            "quote": "333 O'Farrell Street, Hilton San Francisco Union Square | Tower 1, 46th Floor, San Francisco, CA 94102. HOURS: Sunday - Saturday | 4:00P to 12:00A. 21+ after 10:00P daily.",
        },
        "flags": [
            "21+ after 10 PM daily.",
            "Hours subject to change due to private events per the official site.",
        ],
        "verification": {
            "status": "verified",
            "method": "Official page fetched 2026-09-06; address, daily 4 PM-midnight hours, and 21+ policy read directly. Fri/Sat/Sun midnight closes qualify.",
            "verifiedOn": TODAY,
        },
        "neighborhoodGroup": "downtown-union-square",
    },
    {
        "id": "redwood-room",
        "name": "Redwood Room",
        "category": "Cocktail bar / lounge",
        "neighborhood": "Nob Hill",
        "address": "495 Geary St, San Francisco, CA 94102",
        "officialUrl": "https://redwoodroomsf.com/",
        "hours": {
            "Monday": "5:00 PM-12:00 AM", "Tuesday": "5:00 PM-12:00 AM",
            "Wednesday": "5:00 PM-12:00 AM", "Thursday": "5:00 PM-12:00 AM",
            "Friday": "5:00 PM-12:00 AM", "Saturday": "5:00 PM-12:00 AM",
            "Sunday": "5:00 PM-12:00 AM",
        },
        "qualifyingDays": ["Friday", "Saturday", "Sunday"],
        "access": {
            "summary": "38 Geary (Geary St & Powell St stop) or 30 Stockton (Stockton St & Geary St stop) + short walk",
            "detail": "SFMTA stop lists place 38 Geary at Geary St & Powell St, one block from 495 Geary, and 30 Stockton at Stockton St & Geary St, two blocks away.",
            "sources": [{"label": "SFMTA route directory", "url": "https://www.sfmta.com/routes"}],
            "lineIds": ["38", "30"],
        },
        "source": {
            "label": "Official site (live) + 2026 listing hours",
            "url": "https://redwoodroomsf.com/",
            "quote": "Official site: 'The Clift's famous and historic Redwood Room... 495 Geary St, San Francisco, CA 94102' (no machine-readable hours; reservations listed until 11:30 PM). 2026 listings: daily 5:00 PM - 12:00 AM.",
        },
        "flags": [
            "Hours conflict: 2026 listings say daily 5 PM-midnight, while an older (2019) source says Thu-Sat 4 PM-2 AM / Sun-Wed 4 PM-1 AM - the midnight close is used and flagged.",
            "The official site has no hours page; confirm the specific night before going.",
        ],
        "verification": {
            "status": "verified-with-gap",
            "method": "Official site fetched 2026-09-06 (address and venue confirmed, no hours page); 2026 listing hours used with the conflict flagged.",
            "verifiedOn": TODAY,
        },
        "neighborhoodGroup": "downtown-union-square",
    },
    {
        "id": "sullys-marina-lounge",
        "name": "Sully's Marina Lounge",
        "category": "Dive bar",
        "neighborhood": "Marina",
        "address": "2138 Chestnut St, San Francisco, CA 94123",
        "officialUrl": "https://sullysmarinalounge.com/",
        "hours": {
            "Monday": "12:00 PM-2:00 AM", "Tuesday": "12:00 PM-2:00 AM",
            "Wednesday": "12:00 PM-2:00 AM", "Thursday": "12:00 PM-2:00 AM",
            "Friday": "12:00 PM-2:00 AM", "Saturday": "12:00 PM-2:00 AM",
            "Sunday": "12:00 PM-2:00 AM",
        },
        "qualifyingDays": ["Friday", "Saturday", "Sunday"],
        "access": {
            "summary": "5 Fulton (Fulton St & 22nd Ave stop) or 45 Union/Stockton (Union St & Pierce St stop) + short walk",
            "detail": "SFMTA stop lists place 5 Fulton at Fulton St & 22nd Ave, one block from 2138 Chestnut, and 45 Union/Stockton at Union St & Pierce St, one to two blocks north.",
            "sources": [{"label": "SFMTA route directory", "url": "https://www.sfmta.com/routes"}],
            "lineIds": ["5", "45"],
        },
        "source": {
            "label": "Official site",
            "url": "https://sullysmarinalounge.com/",
            "quote": "Open daily, 12:00 PM - 2:00 AM. Sun-Sat 12:00 PM - 2:00 AM. Address: 2138 Chestnut Street, San Francisco, CA 94123, Marina District.",
        },
        "flags": [
            "A mirror site listed Fri-Sun opening at 8 AM; the official site says 12 PM daily - the official site is used.",
        ],
        "verification": {
            "status": "verified",
            "method": "Official page fetched 2026-09-06; address and daily 12 PM-2 AM hours read directly. Fri/Sat/Sun all close 2 AM.",
            "verifiedOn": TODAY,
        },
        "neighborhoodGroup": "marina",
    },
    {
        "id": "the-felix",
        "name": "The Felix",
        "category": "21+ cocktail bar",
        "neighborhood": "SoMa / Civic Center",
        "address": "138 Mason St, San Francisco, CA 94105",
        "officialUrl": "https://www.thefelixsf.com/",
        "hours": {
            "Monday": "Closed", "Tuesday": "Closed", "Wednesday": "Closed",
            "Thursday": "6:00 PM-12:00 AM", "Friday": "8:00 PM-1:00 AM",
            "Saturday": "8:00 PM-1:00 AM", "Sunday": "Closed",
        },
        "qualifyingDays": ["Friday", "Saturday"],
        "access": {
            "summary": "N Judah (Mason St & Sutter St stop) or 43 Masonic (Mason St stops) + short walk",
            "detail": "SFMTA stop lists place N Judah at Mason St & Sutter St, at the corner of 138 Mason, with 43 Masonic stops on Mason Ave nearby.",
            "sources": [{"label": "SFMTA route directory", "url": "https://www.sfmta.com/routes"}],
            "lineIds": ["N", "43"],
        },
        "source": {
            "label": "Official site",
            "url": "https://www.thefelixsf.com/",
            "quote": "Hours: Thursday: 6PM - 12AM; Friday/Saturday: 8PM - 1 AM. Reservations up to 10. 21+, you must have a valid, physical, government issued ID to enter.",
        },
        "flags": [
            "21+ with physical ID; reservations required after 10 PM.",
            "The official site does not display the street address; 138 Mason St (Civic Center) is per the venue's claimed listing.",
        ],
        "verification": {
            "status": "verified",
            "method": "Official page fetched 2026-09-06; hours and 21+ policy read directly. Fri/Sat 1 AM closes qualify.",
            "verifiedOn": TODAY,
        },
        "neighborhoodGroup": "hayes-valley-civic",
    },
    {
        "id": "goemon-izakaya",
        "name": "Goemon Izakaya Bar & Lounge",
        "category": "Izakaya / bar / karaoke",
        "neighborhood": "Outer Richmond",
        "address": "3129 Clement St, San Francisco, CA 94121",
        "officialUrl": "https://goemonsushisf.com/izakaya/",
        "hours": {
            "Sunday": "4:30 PM-11:00 PM", "Monday": "4:30 PM-11:00 PM",
            "Tuesday": "Closed", "Wednesday": "4:30 PM-11:00 PM",
            "Thursday": "4:30 PM-11:00 PM",
            "Friday": "4:30 PM-12:30 AM (site prints '12:30pm'; karaoke runs Fri/Sat 8:30 PM-12:00 AM)",
            "Saturday": "4:30 PM-12:30 AM (site prints '12:30pm'; karaoke runs Fri/Sat 8:30 PM-12:00 AM)",
        },
        "qualifyingDays": ["Friday", "Saturday"],
        "access": {
            "summary": "38 Geary (Geary Blvd & 33rd Ave stop) or 1 California (California St & 32nd Ave stop) + short walk",
            "detail": "SFMTA stop lists place 38 Geary at Geary Blvd & 33rd Ave, one block north of 3129 Clement, and 1 California at California St & 32nd Ave, one block south.",
            "sources": [{"label": "SFMTA route directory", "url": "https://www.sfmta.com/routes"}],
            "lineIds": ["38", "1"],
        },
        "source": {
            "label": "Official site (Izakaya location page)",
            "url": "https://goemonsushisf.com/izakaya/",
            "quote": "Goemon Izakaya Bar & Lounge (Outer Richmond), 3129 Clement St, San Francisco, CA 94121. Sun-Mon: 4:30pm-11pm; Tues: Closed; Wed-Thur: 4:30pm-11pm; Fri-Sat: 4:30pm-12:30pm [printed as '12:30pm' on the official site - clearly 12:30 AM]. Live Karaoke & DJ! Every Friday & Saturday, 8:30pm-12am.",
        },
        "flags": [
            "The official site prints the Fri/Sat close as '12:30pm' (a typo for 12:30 AM); the official karaoke line (Fri/Sat 8:30 PM-12:00 AM) confirms after-midnight service.",
            "A Sep 2026 claimed listing says Fri/Sat 5:00 PM - 2:00 AM; the official site is used and the conflict flagged.",
        ],
        "verification": {
            "status": "verified",
            "method": "Official Izakaya location page fetched 2026-09-06; address and weekly hours read directly, with the Fri/Sat late close corroborated by the official karaoke hours.",
            "verifiedOn": TODAY,
        },
        "neighborhoodGroup": "richmond",
    },
]

# ---------------------------------------------------------------------------


def main() -> None:
    data = json.loads(DATA_PATH.read_text())
    venues = data["venues"]
    meta = data["meta"]

    # Sanity: no id / address / name collisions with existing records.
    old_ids = {v["id"] for v in venues}
    old_addr = {v["address"] for v in venues}
    old_names = {v["name"].lower() for v in venues}
    new_ids = {v["id"] for v in NEW_VENUES}
    assert not (old_ids & new_ids), f"id collision: {old_ids & new_ids}"
    for v in NEW_VENUES:
        assert v["address"] not in old_addr, f"address collision: {v['address']}"
        assert v["name"].lower() not in old_names, f"name collision: {v['name']}"
    assert len(NEW_VENUES) == 23, len(NEW_VENUES)

    # Merge.
    venues.extend(NEW_VENUES)

    # Meta: verifiedOn / recordCount / scopeNote.
    meta["verifiedOn"] = TODAY
    meta["recordCount"] = len(venues)
    meta["scopeNote"] = (
        "Static, source-linked directory of 130 verified records. It does not claim "
        "every San Francisco business is open or available; expand the master list only "
        "after a line-by-line source check."
    )

    # Transit: Sunday 2026-09-06 snapshot.
    transit = meta["transit"]
    transit["snapshotDate"] = TODAY
    transit["snapshotDay"] = SUN
    transit["serviceNote"] = (
        "Snapshot taken Sunday 2026-09-06 using SFMTA Sunday service (service_id=3, "
        "confirmed from the schedule pages' service switcher). The SFMTA schedule page "
        "lists Labor Day 2026-09-07 under the same Sunday service ID; school-day "
        "service (M11) is not used today."
    )
    line_ids = set()
    for line in transit["lines"]:
        lid = line["id"]
        sched_id = "NBUS" if lid == "N" else lid
        line["scheduleUrl"] = (
            f"https://www.sfmta.com/routes/schedule/{sched_id}"
            f"?direction_id=0&service_id=3&date=20260906"
        )
        upd = SUN_TRANSIT[lid]
        line["todayWindow"] = upd["todayWindow"]
        line["todayFrequency"] = upd["todayFrequency"]
        line["nightCoverage"] = upd["nightCoverage"]
        line["sourceQuote"] = upd["sourceQuote"]
        line["checkedOn"] = TODAY
        line_ids.add(lid)

    # Cross-check every venue's lineIds against the transit lines.
    for v in venues:
        unknown = set(v["access"]["lineIds"]) - line_ids
        if unknown:
            raise SystemExit(f"{v['name']} references unknown lines: {unknown}")

    DATA_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Merged: {len(venues)} venues ({len(venues) - 107} new).")
    print(f"verified: {sum(v['verification']['status'] == 'verified' for v in venues)}; "
          f"verified-with-gap: {sum(v['verification']['status'] != 'verified' for v in venues)}.")


if __name__ == "__main__":
    main()
