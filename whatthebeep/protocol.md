---
layout: default
title: "#WhatTheBeep Protocol"
---

*Italics indicate informal explanations. This is not legally binding, but a good-faith contract The Yawning Chihuahua claims to follow when publishing #WhatTheBeep evaluations.*

## 1. Evaluation schema

1.1. Every #WhatTheBeep evaluation is identified by a unique:
   - 1.1.1. vehicle manufacturer and model
   - 1.1.2. variant or set of variants
   - 1.1.3. publication date
1.2. It is only guaranteed that the combination of attributes mentioned in 1.1. will be unique. Barring this combination, there is no limit to the number of evaluations published with a specific attribute.

*TL;DR: You are relying on good faith of The Yawning Chihuahua to not spam you with results. As long as the car, variant(s) or publication date are different, The Yawning Chihuahua will consider them different evaluations and we have to just hope they will not be different results on different days.*

## 2. Model Selection

2.1. Any M1 or N1 vehicle model sold in the Indian market at the time of publication, and available with factory-fitted rear seats, is a potential candidate for evaluation, regardless of whether or not it has a rear seatbelt reminder, and regardless of whether or not it is fully homologated in India.

2.2. Final decisions about model selection are at the sole discretion of The Yawning Chihuahua.

*TL;DR: In theory, The Yawning Chihuahua can perform or refuse to perform a #WhatTheBeep evaluation on whatever the hell he wants to, with obvious limits. For example, he cannot evaluate the behaviour of the rear seatbelt reminder of a potato, a motorcycle, or even a 2-seater car, for that matter. However, please **do not hesitate to [suggest a car for evaluation](mailto:theyawningchihuahua@gmail.com)**, unless you are professionally affiliated with a vehicle component supplier or a rival vehicle manufacturer.*

## 3. Information Sources

3.1. An information source is any method of obtaining #WhatTheBeep testcase outcomes in a given evaluation.

3.2. Acceptable information sources for a #WhatTheBeep evaluation are:

- 3.2.1. In-person testing. All of the following must be satisfied for an in-person test to be considered a valid information source for an evaluation:
  - 3.2.1.1. The Yawning Chihuahua has obtained access to a unit of the exact make and model of vehicle being evaluated.
  - 3.2.1.2. Either, at the time of publication, there have been no changes to the model since the unit obtained was registered, or The Yawning Chihuahua obtains and publishes confirmation (e.g. by comparing documentation) that the rear seatbelt reminder behaviour of the unit obtained is identical to that of units on sale at the time of publication.
  - 3.2.1.3. The Yawning Chihuahua is able to record, and publishes, an identifying detail of the unit obtained, e.g. registration number or VIN.
  - 3.2.1.4. The Yawning Chihuahua is able to film all #WhatTheBeep testcase scenarios being performed physically on the car, with "sufficiently clear" audio and video.

  In this case, the #WhatTheBeep testcase outcomes are determined by observing the status of the audible warning in the film in the four testcases.

- 3.2.2. Desktop research. All of the following must be satisfied for desktop research to be considered a valid information source for an evaluation:
  - 3.2.2.1. The Yawning Chihuahua has obtained access to, and publishes a link to, a user manual of the exact make and model of vehicle being evaluated.
  - 3.2.2.2. At the time of publication, there have been no changes to the model since the manual obtained was published.
  - 3.2.2.3. The Yawning Chihuahua is able to locate, and publishes, a brochure indicating if the variant(s) being evaluated have a rear seatbelt reminder.
  - 3.2.2.4. The manual implicitly or explicitly describes, with "sufficient" clarity, the behaviour of the rear seatbelt reminder in all #WhatTheBeep testcases.

  In this case, the #WhatTheBeep testcase outcomes are determined by interpreting the behaviour of the audible warning in the testcases.

3.3. Audit evaluations

- If so desired, and regardless of agreement in testcase outcomes, The Yawning Chihuahua may delete an evaluation if a subsequent evaluation for the same make and model is performed with a "more reliable" information source, and can demonstrably be deemed to apply to the model and variant(s) evaluated in the original evaluation. In this case The Yawning Chihuahua will take down the original evaluation and include a redirect to the new evaluation on the page of the original evaluation.
- In-person testing is considered "more reliable" than desktop research.

*TL;DR: The Yawning Chihuahua will evaluate cars by testing them in person or reading and interpreting their manuals, and publish a bunch of evidence that the results actually apply to the car being evaluated. But not all sources are equally reliable, so if The Yawning Chihuahua is able to get a more reliable evaluation source then the car may be re-evaluated and the original result deleted to avoid confusion.*

## 4. Requirements

The result of an evaluation is deemed to be <span style="color: green;">**PASS**</span> if, based on a valid information source for that evaluation, the #WhatTheBeep testcase outcomes are as follows in *all* of the following #WhatTheBeep testcases; otherwise, the result is considered <span style="color: red;">**FAIL**</span>:

**Behaviour requirements for second-level warning in the 2nd-row outboard seats**

| Testcase | Description | Audible warning (expected) |
| --- | --- | --- |
| ![Testcase 1](testcase_1.png) | occupant does not fasten seatbelt | <span style="color: green;">**YES**</span> |
| ![Testcase 2](testcase_2.png) | occupant takes off seatbelt | <span style="color: green;">**YES**</span> |
| ![Testcase 3](testcase_3.png) | seatbelt not fastened on an empty seat | <span style="color: green;">**NO**</span> |
| ![Testcase 4](testcase_4.png) | seatbelt taken off on an empty seat | <span style="color: green;">**NO**</span> |

*TL;DR: To pass #WhatTheBeep, the rear seatbelt reminder in the outboard second-row seats should beep [if and only if](https://en.wikipedia.org/wiki/If_and_only_if) an occupant is not belted, at least for the part of the main beep that activates while driving (not necessarily the beep at startup).*

## Appendix I: Error policy

- The page administrator of *The Yawning Chihuahua* does not accept responsibility for any damages resulting from use of information on this page, including but not limited to loss of property or life.
- If there is reasonable evidence of an error The Yawning Chihuahua may take down the evaluation with or without notice and replace the page with a note about the error.
  - If at some future point in time a fresh evaluation for the car model is published and it is reasonably clear that it would have applied to the car model on sale at the time of publication of the taken-down evaluation, the page of the taken-down evaluation may include a redirect to the fresh evaluation.

*TL;DR: The Yawning Chihuahua washes his hands off any responsibility beforehand. Errors are bound to happen from time to time despite all efforts in good faith to avoid them. Please do not hesitate to [report errors](mailto:theyawningchihuahua@gmail.com) to The Yawning Chihuahua.*

—TYC

[Back to home](../index.html)