title: Group Assignment 2: Testing
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

The following requirements must be satisfied to start this project:

- The team is familiar with collaborative development and code review features of GitHub (a quick recap will also be provided in the lab).
- A development environment with Java, Gradle and Docker support, preferably together with a correctly configured IDE like Eclipse or IntelliJ that allows to execute unit tests and perform coverage analysis on Java projects.
- Note that you must continue working on the same repository you created through GitHub Classroom for group project 1.

You will also likely need several additional tools to complete this assignment. Please identify and describe these tools in your report.

# Part 1: Improve Test Suite

In G1, you did not know all the techniques that could help you choose meaningful test cases and also assess the quality of your tests. Additionally, you only implemented one test per feature.

In the first part of this assignment, your task is to improve the quality of your test suite for the **six rules** in G1 as follows:

1. Use **blackbox testing techniques** to create better test cases and corresponding oracles (i.e., the concrete input values and expected output in your tests). You are advised to carefully read Tartan's specification and decide on whether there are additional scenarios you need to test for (e.g., now is the time to think about whether the rules interact and if there are edge cases you need to think of). When selecting concrete oracles, some of your options include boundary value testing, random testing, or strong/weak equivalence class testing. You may think of other strategies, too.

2. Use **whitebox testing techniques** to evaluate and improve the adequacy of your test suite. In this case, you are asked to write more tests that improve the coverage of your test suite.

## Acceptance criteria for Part 1

| **Criteria** | **Grade** |
|---|---:|
| Whitebox and blackbox test design and selection plans are completed and explained. | 12 |
| Tests must achieve at least 80% statement and 80% branch coverage for the features selected to test. | 15 |
| Automated measurement of coverage with each build is implemented. | 5 |
| All tests pass. | 10 |

**NOTE**: Please refer to the code coverage tutorial posted on Canvas and discussed in the lab to see how you can configure your coverage measurement tool to measure coverage only for your implemented features (as much as possible).


# Part 2: Implementation and Verification of a Smart Door Lock

Tartan Inc. would like your team to implement the software logic for a new smart door lock. The smart door lock hardware allows the door to be locked and unlocked automatically using a passcode, and it will provide many "smart" features that users can configure for additional security or convenience. Note that opening/closing the door is different from locking/unlocking a lock. The former refers to the physical state of the door, while the latter refers to the state of the deadbolt on the door. 

Specifically, the smart lock must support the following features that users can enable or disable:
- **Electronic Operation**: If a person requests a lock or unlock operation from an access panel, first check if that operation requires a passcode. If so, it must validate the input before proceeding. If the passcode is rejected, an appropriate response should be sent. Otherwise, the requested operation should be carried out.
- **Keyless Entry**: When sensors detect the approach of an authorized resident (e.g., proximity of a registered device), automatically unlock the door.
- **Intruder Defence**: When in-home sensors detect the possible presence of an intruder, lock the door and send "possible intruder detected" messages to the access panels. Keep the door locked until the sensors provide an "all clear" signal, at which time "all clear" messages are sent to the access panels.
- **Night Lock**: Residents configure the time when night begins and ends. At night, the door is automatically locked and always relocked if it becomes unlocked at any point during the night.

An access panel is one of these: <br>
<img id="access-panel" alt="access panel" src="{attach}adt-access-panel.jpg" style="width: 50%;"><br>
(Picture by Marco Albertini, https://securitycamcenter.com/how-to-reset-adt-alarm-system/).

For the access panel, you can add the functionality to the frontend, since we don't have any physical access panels. Make sure that your messages are shown on the frontend log of the application. You can append the access panel messages to your log in your code and make sure it's showing up on the frontend.

Note that the above feature requirements may be ambiguous. In addition, features may interact, and the door lock should behave in a reasonable way, which can be resolved with timers, priorities, or other mechanisms. For example, what happens or should happen if an intruder is detected and a resident arrives at the door? You should ask for clarification about requirements if needed and explicitly document all assumptions you make about interactions.

Integrate the smart door lock and its features with the current system and test it thoroughly. You can add additional sensors and actuators to the house, if needed.

**While developing the new door lock features, you must follow a test-driven development (TDD) approach**. Use Pull Requests to integrate each new functionality and have another team member review your code. **Each team member must perform a code review of at least 1 PR**.

To make it easier for us to spot your test-driven development, you must make your commits using RED GREEN commits. Make a git commit after each of the following steps: 
1. **Red**: Write a failing test and make a commit starting with the word "RED".
2. **Green**: Implement the code to make the test pass and commit with the word "GREEN".
3. **Refactor**: Improve the code without changing behaviour and commit with the word "REFACTOR", ensuring all tests still pass.
  
You must conduct unit testing on the new code and carefully measure coverage. However, given that this is a new feature, you should also perform integration (i.e., tests that combine multiple classes/functionality) and system testing (i.e., end-to-end testing that treats the system as a black box). You must also document the integration and system testing procedures in your report.

## Acceptance criteria (Part 2)

The following criteria must be satisfied for Part 2 to be accepted as complete.

| **Criteria** | **Grade** |
|---|---:|
| Requirements for the smart door lock are documented. It should be clear and complete and include any assumptions the team made. | 12 |
| The smart door lock implementation builds and runs successfully, and meets the functional requirements defined above. | 12 |
| Integration and system testing strategy is implemented and described. | 10 |
| Tests must achieve at least 80% statement and 80% branch coverage for **new** code. | 15 |
| The mutation score for the tests related to the new door lock functionality should be 90%. | 10 |
| Automated System Testing Integrated in CI. | 5 |
| Test-driven development has been followed. | 5 |
| New features underwent code review. | 5 |


# Report for Parts 1 & 2

You must write your report that describes your verification activities, decisions, and results for both the existing functionality and the new door lock. While marking, we will verify all acceptance criteria by checking both your report and code repository. However, we will not look “deeply” into your code repository, e.g., we will not spend more than 10 minutes trying to get your project to compile and run. 

The following describes the required details of the report:

- **Part 1:**
	- **Chosen Rules**: For completeness, restate the six rules (same as those from G1) for part 1.
	- **Testing plan and test cases**: Describe the process you used to design test cases and provide an overview of the tests you wrote. How were test cases designed? How were test values selected? Which testing techniques did you use (i.e. random testing, combinatorial testing, BVA, other)? Mention how much additional testing you needed to add in G2 when compared to G1. Finally, provide a pointer to the actual test classes/methods scripts in your repository (either a hyperlink or path description).
	- **Coverage**: Provide a screenshot of your coverage report (you can focus only on the relevant parts of the system). While marking, we will look into the actual report ourselves and make sure you satisfy the coverage criteria.

- **Part 2:**
	- **Clarified requirements for smart door lock**: Describe all assumptions you made about the requirements of the smart door lock system and its features.
	- **Software development processes**: Briefly indicate the role of each group member in this process, and describe how you planned and organized the design, development, and evaluation of the smart door lock. Include a description of how you coordinated implementation and testing.
	- **Overall testing strategy and implementation**: Indicate where your unit, integration, and system tests are implemented. Mention what you chose to test for integration testing, as well as system testing. Which tools/frameworks/techniques did you use to implement your integration and system testing?
	- **Coverage and mutation score**: Provide a screenshot of your coverage report (you can focus only on the relevant parts of the system). While marking, we will look into the actual report ourselves and make sure you satisfy the coverage criteria. Also, provide a screenshot of your mutation score report. Please mention 2-3 examples of initially live mutations (i.e., mutants that your test suite did not initially kill) and how you improved your test suite to kill these mutants.

# Submission Requirements

- **Please tag your code with `G2_Done`**
- Submit a PDF report (max. 4 pages of text, including screenshots/tables, etc) via Canvas.
- Include your team's repository link in the report.
- Please name your file using the following format:
    - `<LabCode>_<GroupName>_G2_Report.pdf`
    - Example: `D01_m01_G2_Report.pdf`
- Meets the formatting requirements in the previous section. Marks may be lost or you may receive a zero if the report is not **easy** to read and professional, or if it does not meet the formatting above.

Your report must be well formatted and not just readable, but professional and **easy** to read.

* Text must be standard and consistent. (10-11pt, Times New Roman or Computer Modern)
* Images must be sized so that text size is similar inside the image as it is outside of the image (10-11pt).
* Page orientation must stay consistently Portrait.
* Two columns.
* Letter Size (A4 is not allowed).
* Single spaced inside paragraphs + 6pt (~0.5 lines) after paragraphs.

More details can be found in the MS Word template: [https://www.ieee.org/content/dam/ieee-org/ieee/web/org/conferences/conference-template-letter.docx] or [the MS Word template rendered as a PDF]({attach}conference-template-letter.pdf). If in doubt, make your report look like the template!

More templates: 

* [https://www.ieee.org/conferences/publishing/templates] (Use US Letter only!)
* [Overleaf template](https://www.overleaf.com/read/qtgwphwhrkft#eaa1dc)

## MS Word & Google Doc Guidelines

- Submit your PDF.
    - Include your MS Word .docx in your repository OR your Google Doc URL.
    - Include all the figures in your repository.

## LaTeX Usage Guidelines

- If you are using [Overleaf](https://www.overleaf.com/) (an online collaborative LaTeX editor):  
    - Submit your PDF report along with the Overleaf project URL.  
    - Include your LaTeX source files (e.g., `.tex`, figures, `.bib`) in your GitHub repository.  

- If you are using LaTeX locally (instructions for local setup can be found at [MiKTeX](https://miktex.org/)):  
	- Submit your PDF report to Canvas.  
    - Include your LaTeX source files (e.g., `.tex`, figures, `.bib`) in your GitHub repository.  

📌 To ensure your LaTeX source file is easy to locate, place it in a logical location within the repository (e.g., a clearly named folder), and create or update the README.md to document the structure and contents.

# Grading Summary

In total, G2 is worth 133 points with the following breakdown:

- Part 1 (improving test suite): 42 points
- Part 2 (implementation and verification): 74 points
- Report: 12 points
- Peer assessment: 5 points (Assigned individually)

The report is graded based on its presentation, organization, and how clearly things are described. All the items described in the Report section above must appear in the report.

Each member must assess their team members' contributions on eClass. This is worth 5 points of the total assignment grade and is confidential (results go to the course staff). Note that if we find big discrepancies in contributions or if one team member is negatively rated by all other team members, then we will investigate and regrade team members as needed.

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
* In TDD, why do we go for RED first?
* How did you handle interactions in the requirements in part 2?
* How did you test for interactions?
* Do the computed adequacy criteria give you confidence that your software is thoroughly tested and of adequate quality?
* If you could pick your own goals for test adequacy measures, what would you aim for?
* Which testing techniques were most effective for you and why?
* Which techniques were less effective and why?
* Did mutation testing help you find weaknesses in your test suite? Can you give an example?
* If you had to conduct a similar project again, would you change any of your testing or planning strategies?
* What were the challenges you faced, and how did you solve them?

Copyright 2021, 2022 Dr. Sarah Nadi. Copyright 2023, 2024 Dr. Hazel Campbell. All rights reserved.
