---
layout: page
description: "Publication of new #WhatTheBeep result(s)."
title: "Grand Vitara fails #WhatTheBeep."
twitter_card:
    type: "summary_large_image"
    image: https://theyawninchihua.github.io/theyawninchihua/articles/N202610301/banner.png
---

**30.10.2026**

![Banner](banner.png)

The [Maruti Suzuki GRAND VITARA](../../whatthebeep/2026-10-30-GRANDVITARA-DeltaSCNG/) has been awarded **<span style="color: red;">FAIL</span>** in a new [#WhatTheBeep seatbelt reminder evaluation](../../whatthebeep/).

## Maruti Suzuki GRAND VITARA evaluation explained

In-person testing revealed that the rear seatbelt reminder of the [Maruti Suzuki GRAND VITARA](../../whatthebeep/2026-10-30-GRANDVITARA-DeltaSCNG/) does not start its intermediate/final signal when an a rear occupant has not buckled up. It only does so when a seatbelt that was already fastened is then taken off, in order to avoid false alerts on empty seats since **its rear seats do not have occupant detection**.

The [GRAND VITARA](../../whatthebeep/2026-10-30-GRANDVITARA-DeltaSCNG/) hence fails two [#WhatTheBeep testcases](../../whatthebeep/protocol.html), earning an overall <span style="color: red;">**FAIL**</span>.

<iframe width="560" height="315" src="https://www.youtube.com/embed/xxY9YpWAPd8?si=PN_kbhzBnz16P-ll" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## [Maruti Suzuki GRAND VITARA](../../whatthebeep/2026-10-30-GRANDVITARA-DeltaSCNG/)
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
- [Datasheet for Maruti Suzuki GRAND VITARA](../../whatthebeep/2026-10-30-GRANDVITARA-DeltaSCNG/)

-TYC

[click to go back to articles](../)
