---
author: Théophile Delmas
fetched_at: '2026-11-03T10:17:53.019615Z'
id: 2a66b81526dd
lane: lead
published: ''
source: linkedin
title: 'I''m proud to introduce Bios


  Bios is an open-source health app as an alternative to Google & Apple Health


  Your health d'
url: https://www.linkedin.com/posts/thdelmas_opensource-digitalsovereignty-health-activity-7523324938875764736-HONU
---

I'm proud to introduce Bios

Bios is an open-source health app as an alternative to Google & Apple Health

Your health data is the most intimate data you produce and shouldn't belong to someone else servers or commercial contract unless you specifically want to

Today the app that collects them belongs to the maker of your watch, and the hub that stores them on the phone belongs to Apple or Google

I wanted the same move for health data that e Foundation - /e/OS - my data is MY data made for the phone OS and Proton made for mail: a transparent alternative where you stay in control

Bios stores your readings in an encrypted database on your phone (SQLCipher, key wrapped by the Android Keystore)
Nothing leaves the device unless you export it manually:
The only outbound paths are ones you switch on, such as a vendor connector with your own credentials

Health Corp & software knows when you're sick way before you do, Bios is focused on prevention and early detection
It learns a 14-day baseline per signal and raises a factual alert when one drifts:
the value, in units, next to your own normal range.

It never scores you and never judges your lifestyle; it detects anomalies from your own baselines and reports what is, then you decide what to do

You can export to FHIR, the format doctors' systems read, so you can preserve you data between doctors, health systems, hospitals, countries, and avoid starting over and over
No Bios account, no Bios cloud, no tracker, everything stays on your device, encrypted

What's new in 0.3.0:
→ Day totals
steps, active calories and active minutes by day, week, month and year. Tap a day in the week or month view to see its total

→ One source per day
my phone held five producers of the same walk
(the watch app, Fitbit, the handset pedometer, and two sensor readers) and summed them all
Some days read five times the truth
Now one source wins each day, in an order you set. Days where the watch mirror is incomplete can still read low, that part is not solved yet

→ Known Sources:
one screen listing every device and app Bios has heard from, what each reports and when it last did

→ Alerts need enough data:
a night with the watch off no longer produces a heart-rate alert built on half a window

→ COROS:
a daily-step path added mid-cycle logged you out of the COROS app, so it was withdrawn. Both entries are in the notes.

Not verified yet:
the connectors for ŌURA, Garmin, Withings, POLAR, WHOOP and Dexcom are written but untested on real devices

HRV from COROS and KIPRUN watches still needs the COROS app and account, because it only exists in their cloud. We are investigating for a workaround

Download and notes: https://lnkd.in/ewm__g9m
Community: https://lnkd.in/ewwyrc92
#OpenSource #DigitalSovereignty #Health #Android #Bios
