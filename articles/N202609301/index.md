---
layout: page
description: "Publication of new #WhatTheBeep result(s)."
title: "Tata Aeris' rear seatbelt reminder awarded FAIL in #WhatTheBeep evaluation"
twitter_card:
    type: "summary_large_image"
    image: https://theyawninchihua.github.io/theyawninchihua/articles/N202609301/banner.png
---

**30.09.2026**

![Banner](banner.png)

The [Tata AERIS](../../whatthebeep/2026-09-30-AERIS-Smart12Revotron/index.html) was launched in the Indian market last week. With its owners' manual published on Tata's website, The Yawning Chihuahua has been able to investigate the behaviour of the system under [#WhatTheBeep](../../whatthebeep).

The sedan today receives <span style="color: red;">**FAIL**</span> in a new [#WhatTheBeep evaluation](../../whatthebeep), with the same "ghost beeps" that affect the related [Xpres, rated earlier this year](../N202606221/index.html).

## Tata Aeris evaluation explained

With no occupant detection in the second row, the [AERIS](../../whatthebeep/2026-09-30-AERIS-Smart12Revotron/index.html) audibly alerts when a rear seatbelt isn't fastened, regardless of occupancy. This is unlike even other systems without rear occupant detection, which typically wait for a belt to change from fastened to unfastened to avoid most false alerts. Anecdotal evidence suggests this can cause annoyance to the extent of forcing drivers to keep seatbelts perpetually fastened, even if they would otherwise be in favour of rear seatbelt use.

The [AERIS](../../whatthebeep/2026-09-30-AERIS-Smart12Revotron/index.html) fails two of the four [#WhatTheBeep testcases](../../whatthebeep/protocol.html), and is awarded an overall <span style="color: red;">**FAIL**</span>.

**Behaviour of second-level warning in the 2nd-row outboard seats**

| Testcase | Description | Audible warning | Verdict |
| --- | --- | --- | --- |
| ![Image](../../whatthebeep/testcase_1.png) | occupant does not fasten seatbelt | **YES** | <span style="color: green;">**OK**</span> |
| ![Image](../../whatthebeep/testcase_2.png) | occupant takes off seatbelt | **YES** | <span style="color: green;">**OK**</span> |
| ![Image](../../whatthebeep/testcase_3.png) | seatbelt not fastened on an empty seat | **YES** | <span style="color: red;">**NOT OK**</span> |
| ![Image](../../whatthebeep/testcase_4.png) | seatbelt taken off on an empty seat | **YES** | <span style="color: red;">**NOT OK**</span> |
|  |  |  | <span style="color: red;">**FAIL**</span> |

More information about results, datasheets, sources of information, and evaluation criteria are at the following links:

- [All you need to know about #WhatTheBeep](../../whatthebeep/index.html)
- [Datasheet for Tata AERIS](../../whatthebeep/2026-09-30-AERIS-Smart12Revotron/index.html)

-TYC

[click to go back to articles](../index.html)
