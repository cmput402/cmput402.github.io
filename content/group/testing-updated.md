
Title: Group Assignment 2: Testing
date: 2025-09-19
tags: labs, policy, grading
authors: Hazel Victoria Campbell, Sarah Nadi
status: published
----

[TOC]

# Overview

In this project, you will extend the **Tartan Home** system with new functionality and test it for functional correctness, code quality, and other quality attributes across **unit**, **integration**, and **system** levels. You will also likely update the testing infrastructure from G1. G2 has two parts.

The learning goals of this group project are:

- Learn to set up and manage a continuous testing strategy and supporting technologies.
- Gain experience using different test case design techniques.
- Select and integrate appropriate testing techniques throughout the engineering process, using appropriate technologies.
- Select and assess various measures, including but not limited to code coverage, for the adequacy of a test suite.


The learning goals of this group project are:

- Learn to to setup and manage a continuous testing strategy and supporting
  technologies.
- Gain experience using different test case design techniques.
- Select and integrate appropriate testing techniques throughout the
  engineering process, using appropriate technologies.
- Select and assess various measures, including but not limited to code
  coverage, for the adequacy of a test suite.

The following requirements must be satisfied to start this project:

- The team is familiar with collaborative development and code review features of GitHub (a quick recap will also be provided in the lab).
- A development environment with Java, Gradle and Docker support, preferably together with a correctly configured IDE like Eclipse or IntelliJ that allows to execute unit tests and perform coverage analysis on Java projects.
- Note that you must continue working on the same repository you created through GitHub Classroom for group project 1.

You will also likely need several additional tools to complete this assignment. Please identify and describe these tools in your report.

## Part 1: Improve Test Suite

In G1, you did not know of all the techniques that could help you choose meaningful test cases and also assess the quality of your tests. Additionally, you only implemented one test per feature.

In the first part of this assignment, your task is to improve the quality of your test suite for the **six rules** in G1 as follows:

1. Use **blackbox testing techniques** to create better test cases and corresponding oracles (i.e., the concrete input values and expected output in your tests). You are advised to carefully read Tartan's specification and decide on whether there are additional scenarios you need to test for (e.g., now is the time to think about whether the rules interact and if there are edge cases you need to think of). When selecting concrete oracles, some of your options include boundary value testing, random testing, or strong/weak equivalence class testing. You may think of other strategies, too.

2. Use **whitebox testing techniques** to evaluate and improve the adequacy of your test suite. In this case, you are asked to write more tests that improve the coverage of your test suite.

### Acceptance criteria for Part 1

| Criteria | Points |
|---|---:|
| White-box & black-box **test design/selection plans** are completed and explained | 12 |
| ≥ **80% statement** and ≥ **80% branch** coverage for selected features | 15 |
| **Automated coverage measurement** runs on each build | 5 |
| **All tests pass** | 10 |

**NOTE**: Please refer to the code coverage tutorial posted on Canvas and discussed in the lab to see how you can configure your coverage measurement tool to measure coverage only for your implemented features (as much as possible).

---

## Part 2: Implementation and Verification of a Smart Door Lock

Tartan Inc. would like your team to implement the software logic for a new smart door lock. The smart door lock hardware allows the door to be locked and unlocked automatically using a passcode, and it will provide many "smart" features that users can configure for additional security or convenience. Note that opening/closing the door is different from locking/unlocking a lock. The former refers to the physical state of the door, while the latter refers to the state of the deadbolt on the door. 

Specifically, the smart lock must support the following features that users can enable or disable:
- **Electronic Operation**: If a person requests a lock or unlock operation from an access panel, first check if that operation requires a passcode. If so, it must validate the input before proceeding. If the passcode is rejected, an appropriate response should be sent. Otherwise, the requested operation should be carried out.
- **Keyless Entry**: When sensors detect the approach of an authorized resident (e.g., proximity of a registered device), automatically unlock the door.
- **Intruder Defence**: When in-home sensors detect the possible presence of an intruder, lock the door and send "possible intruder detected" messages to the access panels. Keep the door locked until the sensors provide an "all clear" signal, at which time "all clear" messages are sent to the access panels.
- **Night Lock**: Residents configure the time when night begins and ends. At night, the door is automatically locked and always relocked if it becomes unlocked at any point during the night.


### Acceptance criteria for Part 2

The following criteria must be satisfied for the assignment to be accepted as
complete.

| Criteria | Grade |
|:-------- | :----|
| Requirements for the smart door lock are documented. The documentation format is up to the team, but should be clear and complete and includes any assumptions the team made. | 10 |
| The software for the smart door lock successfully builds, runs, and implements stated requirements. | 10 |
| Integration and system testing strategy is implemented and described | 10 |
| Tests must achieve at least 80% statement and 80% branch coverage for ***new*** code. | 15 |
| The mutation score for the tests related to the new door lock functionality should be 90%| 10 |
| Test-driven development has been followed | 5 |
| New features underwent code review | 5 |


# Report for Parts 1 & 2

Create a report as a single **PDF** file that describes your verification
activities, decisions, and results for both the existing functionality and the
new door lock (max. 4 pages of text, not including screenshots/tables etc). You must upload your report to eClass by the specified deadline. While marking, we will verify all acceptance criteria by checking both your report and code repository.
**The final version of your code for all parts of this project must be in the master branch and tagged as `G2_Done` by the deadline.**

The following describe the required details of the report:

- **Part 1**:
	- **Chosen Rules**: For completeness, restate the four rules you chose for part 1 (they should be the same as those from G1).
	- **Testing plan and test cases**: Describe the
  process you used to design test cases and provide an overview of the tests
  you wrote. How were test cases designed? How were test values selected? Which
  testing techniques did you use (i.e. random testing, combinatorial testing,
  BVA, other)? Mention how much additional testing you needed to add in G2 when compared to G1. Finally, provide a pointer to the actual test classes/methods scripts in your repository.
  - **Coverage**: Provide a screenshot of your coverage report (you can focus only on the relevant parts of the system). While marking, we will look into the actual report ourselves and make sure you satisfy the coverage criteria.
- **Part 2**:
	- **Clarified requirements for smart door lock**:
  Describe all assumptions you made about the requirements of the smart door
  lock system and its features.
  - **Software development processes**: Briefly indicate
  the role of each group member in this process, describe how you planned and
  organized the design, development, and evaluation of the smart door lock.
  Include a description of how you coordinated implementation and
  testing.
  - **Overall testing strategy and implementation:** . Indicate where your unit, integration, and system tests are implemented. Mention what you chose to test for integration testing as well as system testing. Which tools/frameworks/techniques did you use to implement your integration and system testing?
  - **Coverage and mutation score:** Provide a screenshot of your coverage report (you can focus only on the relevant parts of the system). While marking, we will look into the actual report ourselves and make sure you satisfy the coverage criteria. Also, provide a screenshot of your mutation score report. Please mention 2-3 examples of initially live mutations (i.e., mutants that your test suite did not initially kill) and how you improved your test suite to kill these mutants.

# Grading Summary

In total, this project is worth 120 points with the following allocation:

- Part 1 (improving test suite): 40 points
- Part 2 (implementation and verification): 65 points
- Report: 10 points
- Peer assessment: 5 points (Assigned individually)

The report is graded based on its presentation, organization, and how clearly things are described. All the items described in the Report section above must appear in the report.

Each member must assess their team members' contributions on eClass. This is worth 5 points of the total assignment grade and is confidential (results go to the course staff). Note that if we find big discrepencies in contributions or if one team members is negatively rated by all other team members, then we will investigate and regrade team members as needed.

# Questions You Should Be Able to Answer After This Assignment

* What is a unit?
* How does TDD differ from standard types of testing?
* What is an Oracle?
* What might you need to change in the System Under Test in order to make good use of unit testing?
* What makes black box testing different from white box testing?
* Why might we want to use black box testing?
* What is the purpose of unit-testing?
* What are equivalence partitioning and boundary value analysis?
* Why do we use TDD? What is its purpose?
* Can we always have 100% code-coverage?
* What are the different types of coverage criteria?
* Does 100% coverage mean we are bug-free?
* Does 100% MCDC coverage mean we are bug-free?
* Can we prove that we’re 100% bug-free?
* In TDD, Why do we go for RED first?
* How did you handle interactions in the requirements in part 2?
* How did you test for intereactions?
* Do the computed adequacy criteria give you confidence that your software is thoroughly tested and of adequate quality?
* If you could pick your own goals for test adequacy measures, what would you aim for?
* Which testing techniques were most effective for you and why?
* Which techniques were less effective and why?
* Did mutation testing help you find weaknesses in your test suite? Can you give an example?
* If you had to conduct a similar project again, would you change any of your testing or planning strategies?
* What were the challenges you faced and how did you solve them?

Copyright 2021, 2022 Dr. Sarah Nadi. Copyright 2023, 2024 Dr. Hazel Campbell. All rights reserved.
