---
layout: default
title: "Maruti Suzuki's new Brezza is here — is its rear seatbelt reminder any good?"
---

# Maruti Suzuki's new Brezza is here — is its rear seatbelt reminder any good?

**29.07.2026**

![Banner](banner.png)

The facelifted [BREZZA](../../whatthebeep/2026-07-29-BREZZA-LXi10BoosterJet/index.html) from Maruti Suzuki launched last week, and today, a [#WhatTheBeep](../../whatthebeep/index.html) seatbelt reminder evaluation for it has been published.

At the launch of the new Brezza, [Maruti Suzuki were vocal](https://x.com/kushanmitra/status/2080533364139040876?s=20) about the importance of rear seatbelt usage. It would appear, however, that their new SUV isn't.

The [BREZZA](../../whatthebeep/2026-07-29-BREZZA-LXi10BoosterJet/index.html)'s rear seatbelt reminder receives a <span style="color: red;">**FAIL**</span> result under the simple [#WhatTheBeep](../../whatthebeep/index.html) criteria, after desktop evaluation based on its owners' manual.

## Maruti Suzuki BREZZA evaluation explained

Despite having a rear seatbelt reminder, the rear seats of the [BREZZA](../../whatthebeep/2026-07-29-BREZZA-LXi10BoosterJet/index.html) do not have any meaningful occupant detection. Like most such cars, it relies solely on change of belt status, starting its secondary audible signal only when a rear seatbelt *changes status to* unfastened during a drive.

This means the [BREZZA](../../whatthebeep/2026-07-29-BREZZA-LXi10BoosterJet/index.html) fails to audibly alert rear occupants who have been unbelted from the start (likely the majority of unbelted occupants). It can also falsely alert if a belt is taken off on an empty seat (for instance, if an outboard occupant accidentally attempts to use the centre buckle). Both of these individually are sufficient conditions for a <span style="color: red;">**FAIL**</span> under the [#WhatTheBeep](../../whatthebeep/index.html) evaluation criteria.

## [Maruti Suzuki BREZZA](../../whatthebeep/2026-07-29-BREZZA-LXi10BoosterJet/index.html)
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
- [Datasheet for Maruti Suzuki BREZZA](../../whatthebeep/2026-07-29-BREZZA-LXi10BoosterJet/index.html)

-TYC

[click to go back to articles](../index.html)
