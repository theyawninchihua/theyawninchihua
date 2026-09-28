---
layout: default
title: "Maruti Suzuki continues streak of poor rear seatbelt reminders with New Baleno"
---

# Maruti Suzuki continues streak of poor rear seatbelt reminders with New Baleno

**08.09.2026**

![Banner](banner.png)

The facelifted [BALENO](../../whatthebeep/2026-09-08-BALENO-Sigma/index.html) from Maruti Suzuki was launched last weekend, and today, a [#WhatTheBeep](../../whatthebeep/index.html) seatbelt reminder evaluation for it has been published.

The [BALENO](../../whatthebeep/2026-09-08-BALENO-Sigma/index.html)'s rear seatbelt reminder receives a <span style="color: red;">**FAIL**</span> result under the simple [#WhatTheBeep](../../whatthebeep/index.html) criteria, after desktop evaluation based on its owners' manual.

## Maruti Suzuki BALENO evaluation explained

Despite having a rear seatbelt reminder, the rear seats of the [BALENO](../../whatthebeep/2026-09-08-BALENO-Sigma/index.html) do not have any meaningful occupant detection, unlike, for example, units of the related Fronx produced by Maruti Suzuki for export to Australia. Like most such cars, it relies solely on change of belt status, starting its secondary audible signal only when a rear seatbelt *changes status to* unfastened during a drive.

This means the [BALENO](../../whatthebeep/2026-09-08-BALENO-Sigma/index.html) fails to audibly alert rear occupants who have been unbelted from the start (likely the majority of unbelted occupants). It can also falsely alert if a belt is taken off on an empty seat (for instance, if an outboard occupant accidentally attempts to use the centre buckle). Both of these individually are sufficient conditions for a <span style="color: red;">**FAIL**</span> under the [#WhatTheBeep](../../whatthebeep/index.html) evaluation criteria.

## [Maruti Suzuki BALENO](../../whatthebeep/2026-09-08-BALENO-Sigma/index.html)
**Behaviour of second-level warning in the 2nd-row outboard seats**
| Testcase | Description | Audible warning | Verdict |
| --- | --- | --- | --- |
| ![Image](../../whatthebeep/testcase_1.png) | occupant does not fasten seatbelt | **NO** | <span style="color: red;">**NOT OK**</span> |
| ![Image](../../whatthebeep/testcase_2.png) | occupant takes off seatbelt | **YES** | <span style="color: green;">**OK**</span> |
| ![Image](../../whatthebeep/testcase_3.png) | seatbelt not fastened on an empty seat | **NO** | <span style="color: green;">**OK**</span> |
| ![Image](../../whatthebeep/testcase_4.png) | seatbelt taken off on an empty seat | **YES** | <span style="color: red;">**NOT OK**</span> |
**<span style="color: red;">FAIL</span>**

More information about results, datasheets, sources of information, and evaluation criteria are at the following links:

- [All you need to know about #WhatTheBeep](../../whatthebeep/index.html)
- [Datasheet for Maruti Suzuki BALENO](../../whatthebeep/2026-09-08-BALENO-Sigma/index.html)

-TYC

[click to go back to articles](../index.html)
