---
layout: page
description: "Publication of new #WhatTheBeep result(s)."
title: "Kia Syros EV rear seatbelt reminder fails to do the one thing it's supposed to"
---

**05.08.2026**

![Banner](banner.png)

Does a rear seatbelt reminder alarm sound like a good idea to you? To many safety-conscious people, it does. The new [SYROS EV](../../whatthebeep/2026-08-05-SYROSEV-HTK42kWh/index.html) from Kia has one, and today, like many other new launches, we investigate how it works under [#WhatTheBeep](../../whatthebeep/index.html).

Sadly, the [SYROS EV](../../whatthebeep/2026-08-05-SYROSEV-HTK42kWh/index.html)'s rear seatbelt reminder fails to do the one thing a rear seatbelt reminder should, and does not meet the simple criteria to pass [#WhatTheBeep](../../whatthebeep/index.html), a desktop investigation of its owners' manual reveals.

## Kia SYROS EV evaluation explained

Despite having a rear seatbelt reminder, the rear seats of the [SYROS EV](../../whatthebeep/2026-08-05-SYROSEV-HTK42kWh/index.html) do not have any meaningful occupant detection. Like most such cars, it relies solely on change of belt status, starting its secondary audible signal only when a rear seatbelt *changes status to* unfastened during a drive.

This means the [SYROS EV](../../whatthebeep/2026-08-05-SYROSEV-HTK42kWh/index.html) fails to audibly alert rear occupants who have been unbelted from the start (likely the majority of unbelted occupants). It can also falsely alert if a belt is taken off on an empty seat (for instance, if an outboard occupant accidentally attempts to use the centre buckle). Both of these individually are sufficient conditions for a <span style="color: red;">**FAIL**</span> under the [#WhatTheBeep](../../whatthebeep/index.html) evaluation criteria.

## [Kia SYROS EV](../../whatthebeep/2026-08-05-SYROSEV-HTK42kWh/index.html)
**Behaviour of second-level warning in the 2nd-row outboard seats**

| Testcase | Description | Audible warning | Verdict |
| --- | --- | --- | --- |
| ![Image](../../whatthebeep/testcase_1.png) | occupant does not fasten seatbelt | **NO** | <span style="color: red;">**NOT OK**</span> |
| ![Image](../../whatthebeep/testcase_2.png) | occupant takes off seatbelt | **YES** | <span style="color: green;">**OK**</span> |
| ![Image](../../whatthebeep/testcase_3.png) | seatbelt not fastened on an empty seat | **NO** | <span style="color: green;">**OK**</span> |
| ![Image](../../whatthebeep/testcase_4.png) | seatbelt taken off on an empty seat | **YES** | <span style="color: red;">**NOT OK**</span> |
|  |  |  | <span style="color: red;">**FAIL**</span> |

More information about results, datasheets, sources of information, and evaluation criteria are at the following links:

- [All you need to know about #WhatTheBeep](../../whatthebeep/index.html)
- [Datasheet for Kia SYROS EV](../../whatthebeep/2026-08-05-SYROSEV-HTK42kWh/index.html)

-TYC

[click to go back to articles](../index.html)
