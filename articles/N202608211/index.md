---
layout: page
description: "Publication of new #WhatTheBeep result(s)."
title: "Toyota's popular Hyryder SUV awarded FAIL in the simple #WhatTheBeep rear seatbelt reminder test"
---

**20.08.2026**

![Banner](banner.png)

*Make a sound whenever an rear occupant is not wearing their seatbelt, but do not for an unoccupied seat.* That's ALL it takes to pass the [#WhatTheBeep seatbelt reminder evaluation](../../whatthebeep/index.html).

However, like many others, the rear seatbelt reminder of the [Toyota URBAN CRUISER HYRYDER](../../whatthebeep/2026-08-21-URBANCRUISERHYRYDER-ECNGS/index.html) manages to screw up even that, and has today been awarded **<span style="color: red;">FAIL</span>** in a [#WhatTheBeep](../../whatthebeep/index.html) in-person evaluation.

## Toyota URBAN CRUISER HYRYDER evaluation explained

During testing, it was revealed that the rear seatbelt reminder of the [Toyota URBAN CRUISER HYRYDER](../../whatthebeep/2026-08-21-URBANCRUISERHYRYDER-ECNGS/index.html) starts its secondary audible signal only when a rear seatbelt *changes status from fastened to unfastened* during a drive, regardless of seat occupancy.

This means the [URBAN CRUISER HYRYDER](../../whatthebeep/2026-08-21-URBANCRUISERHYRYDER-ECNGS/index.html) fails to audibly alert rear occupants who have been unbelted from the start (likely the majority of unbelted occupants). It also falsely alerts if a belt is taken off on an empty seat (for instance, if an outboard occupant accidentally attempts to use the centre buckle).

The [URBAN CRUISER HYRYDER](../../whatthebeep/2026-08-21-URBANCRUISERHYRYDER-ECNGS/index.html) hence fails two testcases of the [#WhatTheBeep evaluation](../../whatthebeep/index.html), earning an overall <span style="color: red;">**FAIL**</span>.

<iframe width="560" height="315" src="https://www.youtube.com/embed/9KzZpo53xiM?si=5TLOYonCDSkp_IYj" title="Embedded video" allowfullscreen></iframe>

## [Toyota URBAN CRUISER HYRYDER](../../whatthebeep/2026-08-21-URBANCRUISERHYRYDER-ECNGS/index.html)
**Behaviour of second-level warning in the 2nd-row outboard seats**

| Testcase | Description | Audible warning | Verdict |
| --- | --- | --- | --- |
| ![Image](../../whatthebeep/testcase_1.png) | occupant does not fasten seatbelt | <span style="color: red;">**NO**</span> | <span style="color: red;">**NOT OK**</span> |
| ![Image](../../whatthebeep/testcase_2.png) | occupant takes off seatbelt | <span style="color: green;">**YES**</span> | <span style="color: green;">**OK**</span> |
| ![Image](../../whatthebeep/testcase_3.png) | seatbelt not fastened on an empty seat | <span style="color: green;">**NO**</span> | <span style="color: green;">**OK**</span> |
| ![Image](../../whatthebeep/testcase_4.png) | seatbelt taken off on an empty seat | <span style="color: red;">**YES**</span> | <span style="color: red;">**NOT OK**</span> |
|  |  |  | <span style="color: red;">**FAIL**</span> |

More information about results, datasheets, sources of information, and evaluation criteria are at the following links:

- [All you need to know about #WhatTheBeep](../../whatthebeep/index.html)
- [Datasheet for Toyota URBAN CRUISER HYRYDER](../../whatthebeep/2026-08-21-URBANCRUISERHYRYDER-ECNGS/index.html)

-TYC

[click to go back to articles](../index.html)
