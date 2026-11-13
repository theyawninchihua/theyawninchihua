---
layout: default
title: "#WhatTheBeep Protocol"
---

# #WhatTheBeep Protocol

*This is only a set of guidelines The Yawning Chihuahua hopes to follow in good faith when publishing #WhatTheBeep evaluations, and may be modified without notice.*

## 1. Evaluation schema

1.1. Every #WhatTheBeep evaluation is identified by a unique:
   - 1.1.1. vehicle manufacturer and model
   - 1.1.2. variant or set of variants
   - 1.1.3. publication date

1.2. It is only guaranteed that the combination of attributes mentioned in 1.1. will be unique. Barring this combination, there is no limit to the number of evaluations published with a specific attribute.

## 2. Model Selection

2.1. Any M1 or N1 vehicle model sold in the Indian market at the time of publication, and available with factory-fitted rear seats, is a potential candidate for evaluation, regardless of whether or not it has a rear seatbelt reminder, and regardless of whether or not it is fully homologated in India.

2.2. Final decisions about model selection are at the sole discretion of The Yawning Chihuahua.

## 3. Information Sources

3.1. An information source is any method of obtaining #WhatTheBeep testcase outcomes in a given evaluation.

3.2. Acceptable information source types for a #WhatTheBeep evaluation are:

- 3.2.1. In-person testing

  All of the following must be satisfied for an in-person test to be considered a valid information source for an evaluation:
  - 3.2.1.1. The Yawning Chihuahua has obtained access to a unit of the exact make and model of vehicle being evaluated.
  - 3.2.1.2. Either, at the time of publication, there have been no changes to the model since the unit obtained was registered, or The Yawning Chihuahua obtains and publishes confirmation (e.g. by comparing documentation) that regardless of cosmetic or specficication changes, the rear seatbelt reminder behaviour of the unit obtained is identical to that of units on sale at the time of publication.
  - 3.2.1.3. The Yawning Chihuahua is able to record an identifying detail of the unit obtained, e.g. registration number or VIN. The ability to publish this detail is not required.
  - 3.2.1.4. The Yawning Chihuahua is able to film all #WhatTheBeep testcase scenarios, as defined in Section 4 (Requirements) being performed physically on the car, with "sufficiently clear" audio and video.

  In this case, the #WhatTheBeep testcase outcomes are determined by observing the status of the audible warning in the film in the four testcases.

- 3.2.2. Desktop research

  All of the following must be satisfied for desktop research to be considered a valid information source for an evaluation:
  - 3.2.2.1. The Yawning Chihuahua has obtained access to, and publishes a link to, a user manual of the exact make and model of vehicle being evaluated.
  - 3.2.2.2. At the time of publication, there have been no changes to the model since the manual obtained was published.
  - 3.2.2.3. The manual explicitly describes or can be used to infer, with clarity deemed "sufficient", the behaviour of the rear seatbelt reminder in all #WhatTheBeep testcases.

  In this case, the #WhatTheBeep testcase outcomes are determined by interpreting the behaviour of the audible warning in the testcases.

3.3. Audit evaluations

  - 3.3.1. If so desired, and regardless of agreement in testcase outcomes, The Yawning Chihuahua may delete an evaluation if a subsequent evaluation for the same make and model is performed with a "more reliable" information source as defined in 3.3.2., and can demonstrably be deemed to apply to the model and variant(s) evaluated in the original evaluation. In this case The Yawning Chihuahua will take down the original evaluation and include a redirect to the new evaluation on the page of the original evaluation.
  - 3.3.2 Information Source Reliability in descending order:
    - In-person testing
    - Desktop research

## 4. Requirements

## 4.1 Result determination
The result of an evaluation is deemed to be <span style="color: green;">**PASS**</span> if, based on a valid information source for that evaluation, the outcomes in *all* of the scenarios defined in 4.2 (#WhatTheBeep Testcases) match the corresponding expected outcomes; otherwise, the result is considered <span style="color: red;">**FAIL**</span>:

## 4.2 #WhatTheBeep Testcases
**Behaviour requirements for second-level warning in the 2nd-row outboard seats**

| Sequence of actions | Testcase No. | Testcase | Description | Audible warning (expected) |
| --- | --- | --- | --- | --- |
| A | | | seatbelts on any unoccupied rear seats are fastened | |
| B | 1 | ![Testcase 1](testcase_1.png) | occupant does not fasten seatbelt | <span style="color: green;">**YES**</span> |
| C | 2 | ![Testcase 2](testcase_2.png) | occupant takes off seatbelt | <span style="color: green;">**YES**</span> |
| D | | | seatbelts on any empty rear seats are unfastened and rear seatbelt reminder (if fitted) is reset e.g. by opening and closing a rear door at a stop | |
| E | 3 | ![Testcase 3](testcase_3.png) | seatbelt not fastened on an empty seat | <span style="color: green;">**NO**</span> |
| F | 4 | ![Testcase 4](testcase_4.png) | seatbelt taken off on an empty seat | <span style="color: green;">**NO**</span> |

## Appendix I: Error policy

- The #WhatTheBeep protocol may be updated from time to time with or without notice.
- The page administrator of *The Yawning Chihuahua* will make reasonable efforts to ensure that the information on this website is accurate, but does not accept responsibility for any damages resulting from use of information on this website, including but not limited to loss of property or life.
- This website is provided "as is" without any representations or warranties, express or implied. The Yawning Chihuahua makes no representations or warranties in relation to this website or the information and materials provided on this website.
- If there is reasonable evidence of an error in an evaluation, The Yawning Chihuahua may take down the evaluation with or without notice and replace the page with a note about the error.
  - If at some future point in time a fresh evaluation for the car model is published and it is reasonably clear that it would have applied to the car model on sale at the time of publication of the taken-down evaluation, the page of the taken-down evaluation may include a redirect to the fresh evaluation.

—TYC

[Back to home](../)
