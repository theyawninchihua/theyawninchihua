---
layout: default
title: "FAIL for Maruti Suzuki e VITARA in #WhatTheBeep"
---

# <span style="color: red;">FAIL</span> for Maruti Suzuki e VITARA in #WhatTheBeep

**22.05.2026**

![Banner](banner.png)

A new [#WhatTheBeep](../../whatthebeep/index.html) rear seatbelt reminder evaluation has been published today, with the India-spec [Maruti Suzuki e VITARA](../../whatthebeep/2026-05-22-eVITARA-Delta49kWhFWD/index.html) receiving a <span style="color: red;">**FAIL**</span> result.

The India-spec [Maruti Suzuki e VITARA](../../whatthebeep/2026-05-22-eVITARA-Delta49kWhFWD/index.html)'s SBR behaviour **does not mirror that of its global counterparts**: the India-spec version's SBR fails to notify unbelted rear occupants in common scenarios.

## Maruti Suzuki e VITARA evaluation explained

Based on its documentation, the India-spec e VITARA's rear seats appear to skip out on occupant detection sensors, and as a result, its SBR only issues an audio signal when a rear seatbelt is *fastened and then unfastened* on the move. As a result, the India-spec e VITARA receives a <span style="color: red;">**FAIL**</span> result.

## Maruti Suzuki e VITARA (produced in India for India)
**Behaviour of second-level warning in the 2nd-row outboard seats**

| Testcase | Description | Audible warning | Verdict |
| --- | --- | --- | --- |
| ![Image](../../whatthebeep/testcase_1.png) | occupant does not fasten seatbelt | <span style="color: red;">**NO**</span> | <span style="color: red;">**NOT OK**</span> |
| ![Image](../../whatthebeep/testcase_2.png) | occupant takes off seatbelt | <span style="color: green;">**YES**</span> | <span style="color: green;">**OK**</span> |
| ![Image](../../whatthebeep/testcase_3.png) | seatbelt not fastened on an empty seat | <span style="color: green;">**NO**</span> | <span style="color: green;">**OK**</span> |
| ![Image](../../whatthebeep/testcase_4.png) | seatbelt taken off on an empty seat | <span style="color: red;">**YES**</span> | <span style="color: red;">**NOT OK**</span> |
|  |  |  | <span style="color: red;">FAIL</span> |

## Double standard: e VITARA and Toyota URBAN CRUISER exported to Europe have occupant detection

Importantly, documentation for the European e VITARA's twin the Toyota URBAN CRUISER, as well as Euro NCAP results for both cars, reveal that **e VITARA and URBAN CRUISER versions destined for Europe and Australasia have occupant detection in the rear seats and demonstrate seatbelt reminder behaviour comparable to the front passenger seat**, likely because this is a prerequisite for SBRs to score points in [Euro NCAP](https://www.euroncap.com/assessments/suzuki/e+vitara/1160/) and [ANCAP](https://www.ancap.com.au/safety-ratings/suzuki/e-vitara/8a3def).

## Suzuki e VITARA (produced in India for Europe and Australia)
**Behaviour of second-level warning in the 2nd-row outboard seats**

| Testcase | Description | Audible warning |
| --- | --- | --- |
| ![Image](../../whatthebeep/testcase_1.png) | occupant does not fasten seatbelt | <span style="color: green;">**YES**</span> |
| ![Image](../../whatthebeep/testcase_2.png) | occupant takes off seatbelt | <span style="color: green;">**YES**</span> |
| ![Image](../../whatthebeep/testcase_3.png) | seatbelt not fastened on an empty seat | <span style="color: green;">**NO**</span> |
| ![Image](../../whatthebeep/testcase_4.png) | seatbelt taken off on an empty seat | <span style="color: green;">**NO**</span> |

More information about results, datasheets, sources of information, and evaluation criteria are at the following links:

- [All you need to know about #WhatTheBeep](../../whatthebeep/index.html)
- [Datasheet for Maruti Suzuki e VITARA](../../whatthebeep/2026-05-22-eVITARA-Delta49kWhFWD/index.html)

-TYC

[click to go back to articles](../index.html)
