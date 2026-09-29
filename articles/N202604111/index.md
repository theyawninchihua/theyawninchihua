---
layout: default
title: "India-spec Kia EV9 fails #WhatTheBeep"
---

# India-spec Kia EV9 fails #WhatTheBeep

**11.04.2026**

![Banner](banner.png)

A new [#WhatTheBeep](../../whatthebeep/index.html) seatbelt reminder evaluation has been published today, with the India-spec [Kia EV9](../../whatthebeep/2026-04-11-EV9-GTLineAWD/index.html) receiving a <span style="color: red;">**FAIL**</span> result.

Despite arriving in India as a premium import, the [Kia EV9](../../whatthebeep/2026-04-11-EV9-GTLineAWD/index.html)'s SBR behaviour **does not mirror that of its global counterparts**: the India-spec version's SBR fails to notify unbelted rear occupants in common scenarios.

## Kia EV9 evaluation explained

Based on its documentation, the India-spec EV9's rear seats appear to skip out on occupant detection sensors, and as a result, its SBR only issues an audio signal when a rear seatbelt is *fastened and then unfastened* on the move. As a result, the India-spec EV9 receives a <span style="color: red;">**FAIL**</span> result.

## Kia EV9 (India)
**Behaviour of second-level warning in the 2nd-row outboard seats**

| Testcase | Description | Audible warning | Verdict |
| --- | --- | --- | --- |
| ![Image](../../whatthebeep/testcase_1.png) | occupant does not fasten seatbelt | <span style="color: red;">**NO**</span> | <span style="color: red;">**NOT OK**</span> |
| ![Image](../../whatthebeep/testcase_2.png) | occupant takes off seatbelt | <span style="color: green;">**YES**</span> | <span style="color: green;">**OK**</span> |
| ![Image](../../whatthebeep/testcase_3.png) | seatbelt not fastened on an empty seat | <span style="color: green;">**NO**</span> | <span style="color: green;">**OK**</span> |
| ![Image](../../whatthebeep/testcase_4.png) | seatbelt taken off on an empty seat | <span style="color: red;">**YES**</span> | <span style="color: red;">**NOT OK**</span> |
|  |  |  | <span style="color: red;">**FAIL**</span> |

## Double standard: European EV9 has occupant detection

Importantly, the EV9's documentation reveals that **EV9 versions destined for Europe and Australasia demonstrate superior seatbelt reminder behaviour and have occupant detection in the rear outboard seats**, likely because this is a prerequisite for SBRs to score points in [Euro NCAP](https://www.euroncap.com/assessments/kia/ev9/1052/) and [ANCAP](https://www.ancap.com.au/safety-ratings/kia/ev9/fd7032).

## Kia EV9 (Europe, Australia, and New Zealand)
**Behaviour of second-level warning in the 2nd-row outboard seats**

| Testcase | Description | Audible warning |
| --- | --- | --- |
| ![Image](../../whatthebeep/testcase_1.png) | occupant does not fasten seatbelt | <span style="color: green;">**YES**</span> |
| ![Image](../../whatthebeep/testcase_2.png) | occupant takes off seatbelt | <span style="color: green;">**YES**</span> |
| ![Image](../../whatthebeep/testcase_3.png) | seatbelt not fastened on an empty seat | <span style="color: green;">**NO**</span> |
| ![Image](../../whatthebeep/testcase_4.png) | seatbelt taken off on an empty seat | <span style="color: green;">**NO**</span> |

More information about results, datasheets, sources of information, and evaluation criteria are at the following links:

- [All you need to know about #WhatTheBeep](../../whatthebeep/index.html)
- [Datasheet for Kia EV9](../../whatthebeep/2026-04-11-EV9-GTLineAWD/index.html)

-TYC

[click to go back to articles](../index.html)
