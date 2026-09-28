---
layout: default
title: "Nissan Tekton rear seatbelt reminder earns FAIL in #WhatTheBeep evaluation"
---

# Nissan Tekton rear seatbelt reminder earns <span style="color: red;">**FAIL**</span> in #WhatTheBeep evaluation

**17.07.2026**

![Banner](banner.png)

A new [#WhatTheBeep](../../whatthebeep/index.html) seatbelt reminder evaluation has been published today, with the new [Nissan TEKTON](../../whatthebeep/2026-07-17-TEKTON-VisiaT160/index.html) SUV receiving a <span style="color: red;">**FAIL**</span> result.

The [Nissan TEKTON](../../whatthebeep/2026-07-17-TEKTON-VisiaT160/index.html) is a corporate twin to the Renault DUSTER evaluated under [#WhatTheBeep](../../whatthebeep/index.html) earlier this year, and its owners' manual has now been published by Nissan India.

## Nissan TEKTON evaluation explained

The rear outboard seats of the [Nissan TEKTON](../../whatthebeep/2026-07-17-TEKTON-VisiaT160/index.html) do not have any occupant detection system, like pressure mats. Like most such cars, it starts its secondary audible signal only when a rear seatbelt *becomes* unfastened during a drive, and not if it has been unfastened from the start.

This means the Tekton fails to audibly alert unbelted rear occupants in a common scenario, and can also falsely alert if a belt is taken off on an empty seat (for instance, if the user accidentally attempts to use the wrong buckle). Both of these individually are sufficient conditions for a <span style="color: red;">**FAIL**</span> under the [#WhatTheBeep](../../whatthebeep/index.html) evaluation criteria.

## [Nissan TEKTON](../../whatthebeep/2026-07-17-TEKTON-VisiaT160/index.html)
**Behaviour of second-level warning in the 2nd-row outboard seats**

| Testcase | Description | Audible warning | Verdict |
| --- | --- | --- | --- |
| ![Image](../../whatthebeep/testcase_1.png) | occupant does not fasten seatbelt | **NO** | <span style="color: red;">**NOT OK**</span> |
| ![Image](../../whatthebeep/testcase_2.png) | occupant takes off seatbelt | **YES** | <span style="color: green;">**OK**</span> |
| ![Image](../../whatthebeep/testcase_3.png) | seatbelt not fastened on an empty seat | **NO** | <span style="color: green;">**OK**</span> |
| ![Image](../../whatthebeep/testcase_4.png) | seatbelt taken off on an empty seat | **YES** | <span style="color: red;">**NOT OK**</span> |
|  |  |  | <span style="color: red;">FAIL</span> |

More information about results, datasheets, sources of information, and evaluation criteria are at the following links:

- [All you need to know about #WhatTheBeep](../../whatthebeep/index.html)
- [Datasheet for Nissan TEKTON](../../whatthebeep/2026-07-17-TEKTON-VisiaT160/index.html)

-TYC

[click to go back to articles](../index.html)
