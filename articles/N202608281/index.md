---
layout: page
description: "Publication of new #WhatTheBeep result(s)."
title: "FAIL for Ertiga and Rumion's sad excuse for a rear seatbelt reminder — #WhatTheBeep"
---

**28.08.2026**

![Banner](banner.png)

With more than 51% combined market share among MPVs across segments ([see Auto Punditz](https://www.autopunditz.com/post/best-selling-muvs-india-july-2026-ertiga-innova-carens)), the **Maruti Suzuki ERTIGA** and its corporate twin the **Toyota RUMION** carry a large number of Indian passengers in their rear seats every day.

It is with deep disappointment that The Yawning Chihuahua announces that the rear seatbelt reminder of the [ERTIGA](../../whatthebeep/2026-08-28-ERTIGA-VXiOSCNG/) and [RUMION](../../whatthebeep/2026-08-28-RUMION-SCNG/) have today been awarded **<span style="color: red;">FAIL</span>** in a pair of [#WhatTheBeep](../../whatthebeep/) in-person evaluations.

## Maruti Suzuki ERTIGA and Toyota RUMION evaluation explained

During testing, it was revealed that the rear seatbelt reminders of the [ERTIGA](../../whatthebeep/2026-08-28-ERTIGA-VXiOSCNG/) and [RUMION](../../whatthebeep/2026-08-28-RUMION-SCNG/) start their secondary audible signals only when a rear seatbelt *changes status from fastened to unfastened* during a drive, regardless of seat occupancy.

This means the [ERTIGA](../../whatthebeep/2026-08-28-ERTIGA-VXiOSCNG/) and [RUMION](../../whatthebeep/2026-08-28-RUMION-SCNG/) fail to audibly alert rear occupants who have been unbelted from the start (likely the majority of unbelted occupants). They also falsely alert when a belt is taken off on an empty seat (for instance, if an outboard occupant accidentally attempts to use the centre buckle).

The [ERTIGA](../../whatthebeep/2026-08-28-ERTIGA-VXiOSCNG/) and [RUMION](../../whatthebeep/2026-08-28-RUMION-SCNG/) hence each fail two testcases of the [#WhatTheBeep evaluation](../../whatthebeep/), earning overall <span style="color: red;">**FAIL**</span>s.

<iframe width="560" height="315" src="https://www.youtube.com/embed/HcstmHC3nCI?si=cdGLFfBcCDjlNUiv" title="Embedded video" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/DYwji79LpeE?si=CGhfF9T26tcbOM13" title="Embedded video" allowfullscreen></iframe>

## [Maruti Suzuki ERTIGA](../../whatthebeep/2026-08-28-ERTIGA-VXiOSCNG/) / [Toyota RUMION](../../whatthebeep/2026-08-28-RUMION-SCNG/)
**Behaviour of second-level warning in the 2nd-row outboard seats**

| Testcase | Description | Audible warning | Verdict |
| --- | --- | --- | --- |
| ![Image](../../whatthebeep/testcase_1.png) | occupant does not fasten seatbelt | <span style="color: red;">**NO**</span> | <span style="color: red;">**NOT OK**</span> |
| ![Image](../../whatthebeep/testcase_2.png) | occupant takes off seatbelt | <span style="color: green;">**YES**</span> | <span style="color: green;">**OK**</span> |
| ![Image](../../whatthebeep/testcase_3.png) | seatbelt not fastened on an empty seat | <span style="color: green;">**NO**</span> | <span style="color: green;">**OK**</span> |
| ![Image](../../whatthebeep/testcase_4.png) | seatbelt taken off on an empty seat | <span style="color: red;">**YES**</span> | <span style="color: red;">**NOT OK**</span> |
|  |  |  | <span style="color: red;">**FAIL**</span> |

More information about results, datasheets, sources of information, and evaluation criteria are at the following links:

- [All you need to know about #WhatTheBeep](../../whatthebeep/)
- [Datasheet for Maruti Suzuki ERTIGA](../../whatthebeep/2026-08-28-ERTIGA-VXiOSCNG/)
- [Datasheet for Toyota RUMION](../../whatthebeep/2026-08-28-RUMION-SCNG/)

-TYC

[click to go back to articles](../)
