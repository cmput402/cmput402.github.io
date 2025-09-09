Title: Group Assignment 1: Testing Basics
date: 2025-09-05
tags: labs, policy, grading
authors: Hazel Victoria Campbell, Sarah Nadi
status: published
----

[TOC]

# Overview

The goal of this first group project is to familiarize yourself with the Tartan Home system, which you will eventually extend with new functionality and test for functional correctness, code quality, and other quality attributes.

The learning goals of G1 are:

- Familiarize yourself with technologies/concepts such as Gradle, DropWizard, Hibernate, and RESTful Web services.
- Learn to set up and manage a continuous integration strategy and supporting technologies.
- Get experience adding tests to an existing system

The following requirements must be satisfied to start this project:

- A development environment with Java, Gradle and Docker support, preferably together with a correctly configured IDE like Eclipse or IntelliJ that allows to execute unit tests and perform coverage analysis on Java projects. (IntelliJ is recommended but not required.)

- All members of the team must accept the assignment on GitHub Classroom on the following link (https://classroom.github.com/a/cousPqCv). This will create the private repository your team will work on. Make sure to join your assigned team. **The first person from your team to accept the assignment on GitHub Classroom will create the team there. Use the same team name as on eClass (e.g., Group1, Group15, etc.)**

You will also likely need several additional tools to complete this assignment. Please identify and describe these tools in your report.

For all submissions, make sure to explicitly mention your group number and all group member names and CCIDs, as well as your team's GitHub repo. You should also edit your repo's README.md file to include your group name and members.

# **Part 1: Verification of Existing Functionality**

Write **six test cases** for Tartan  

The following outlines Tartan’s rules for making decisions about the house state. Your task is to select five of these rules and evaluate whether they are correctly implemented. **You must include R1 as one of your test cases**, and for the remaining five, select 1 rule from the Easy category, 2 rules from the Medium category, and 2 rules from the Hard category. You are required to write one unit test for each of the six selected rules.

**R1:** If the house is vacant, then the light cannot be turned on.

## 🟢 Easy
- **R2:** If the alarm is enabled and the door is opened, then sound the alarm.  
- **R3:** If the house is vacant, then close the door.  
- **R4:** If the alarm is enabled and the house gets suddenly occupied (i.e., someone is detected by the proximity sensor), then sound the alarm.  
- **R5:** If the target temperature is greater than the current temperature, then turn on the heater. Otherwise, turn off the heater.  
- **R6:** If the target temperature is less than the current temperature, then turn on the air conditioner. Otherwise, turn off the air conditioner.  

## 🟡 Medium
- **R7:** When the “away timer” expires, then turn off the light, arm the alarm, and close the door.  
- **R8:** If the house becomes occupied while the alarm is disabled, then turn on the lights for the legitimate user.  
- **R9:** The alarm can be disabled only when the house is occupied (i.e. it cannot be disabled remotely).  
- **R10:** The heater and the dehumidifier cannot be run simultaneously.  
- **R11:** The IoT Controller shall allow the user to clear the log at any time.

## 🔴 Hard
- **R12:** If the house is empty, then start the away timer.  
- **R13:** The correct passcode is required to disable the alarm.  
- **R14:** The IoT Controller shall require the user to login to the house control panel using a username and password.  
  - The password has the following requirements:  
    - Minimum length: 8 characters  
    - At least one uppercase character  
    - At least one number  
    - At least one symbol  
- **R15:** The IoT Controller shall not allow the user to attempt to log in after three failed attempts.  
- **R16:** The IoT Controller shall allow the user to set the house temperature.  
  - The minimum temperature allowed is **50 degrees Fahrenheit** (10 degrees Celsius).  
  - The maximum temperature allowed is **80 degrees Fahrenheit** (27 degrees Celsius).
 
At this point, you need to only implement one unit test for each selected rule. For the purpose of G1, you can assume independence between the rules (i.e., you do not need to think about situations that combine multiple rules). 

If you find that any of the functionality is not correctly implemented, you must indicate the problem you found in your report and how you fixed it.

# **Part 2: Test Automation Infrastructure**

Now that you have written your initial tests and understand how to build and run Tartan, you will set up the **infrastructure** necessary to automate building and testing. You will set up and configure [GitHub (GH) Actions](https://github.com/features/actions) in your own repository to be used for the rest of the semester.

## **Infrastructure Setup**

Set up and configure the GH Actions workflow in your repository. As a minimum, your team should:

- Set up GH Actions in the repository.  
- Automate the build and tests of the Tartan Home system using workflows (use the tests you wrote in Part 1 to try out and demonstrate the infrastructure).  
- Configure GH Actions to automatically trigger a new build whenever changes are pushed to your GH repository (e.g., main branch).  

At this point, you are also welcome to explore additional GH Actions that may provide useful functionality, such as actions that show statistics, test coverage, or track performance results. You may find this [link](https://github.com/sdras/awesome-actions) useful if you want to set up additional workflows. This is not required for G1 but may prove useful for your next group projects.

# Acceptance Criteria for G1

You must write your report using the [IEEE Conference template](https://www.overleaf.com/read/qtgwphwhrkft#eaa1dc).

## Submission Requirements

- Submit the compiled PDF version of your report via eClass. If applicable, also submit your .tex file (see [LaTeX usage guidelines](#latex-usage-guidelines) below).

- Please name your file using the following format:  
  - `<LabCode>_<GroupX>_G1_Report.pdf` (where X is your group number)
  - Example: H01_Group1_G1_Report.pdf

## LaTeX Usage Guidelines

- If you are using [Overleaf](https://www.overleaf.com/) (an online collaborative LaTeX editor):  
  - Submit your PDF report along with the Overleaf project URL.  
  - Include your LaTeX source files (e.g., `.tex`, figures, `.bib`) in your GitHub repository.  

- If you are using LaTeX locally (instructions for local setup can be found at [MiKTeX](https://miktex.org/)):  
  - Submit your PDF report to Canvas.  
  - Include your LaTeX source files (e.g., `.tex`, figures, `.bib`) in your GitHub repository.  

📌 To ensure your LaTeX source file is easy to locate, place it in a logical location within the repository (e.g., a clearly named folder), and create or update the README.md to document the structure and contents.

## Your Report Must Include

- The **six rules** you selected:  
  (For each rule, clearly indicate the test name and the file location.)  
  - R1 (mandatory)  
  - 1 rule from Easy  
  - 2 rules from Medium  
  - 2 rules from Hard  

- A brief summary of your infrastructure setup:  
  - Describe any GitHub Actions/workflows you created.  
  - Explain how your workflow builds the code and executes the tests.  

- One or more screenshots (inserted as figures in your LaTeX report) showing:  
  - A successful build  
  - A failing build  
  - The passing tests from Part 1  

## Notes on Screenshots

- For the passing build, share a screenshot of a successful GitHub Actions workflow run.  

- For the failing build, it **needs to** be a result of a build failure (e.g., due to compilation issues) or **test** failure (i.e., a test did not pass). Failures caused by the **wrong** setup of your workflow (e.g., permission issues, "No such file or directory" errors, **etc.**) are **not** examples of a failing build. These are examples of a failed setup.  

- For the **passing tests**, the screenshot must include the name of the **passing** test. Thus, it needs to be a screenshot of either an IDE test execution window or the test report that gets generated by Gradle (located in the file `build/reports/tests/test/index.html`), such that the name of the passing test can be seen.

The following criteria must be satisfied for G1 to be accepted as complete.

| **Criteria**                                                                 | **Grade** |
|------------------------------------------------------------------------------|-----------|
| Six unit tests that cover R1 and five other rules, all passing successfully. | 20        |
| Description of bugs found (if any), and how they were fixed.                 | 6         |
| The test infrastructure is set up with automated building and testing.       | 10        |
| GitHub Actions platform reports when the build (i.e., either compilation or tests) is passing/failing. | 10        |

**Please tag your code with `G1_Done`**

# Grading Summary

In total, G1 is worth 63 points with the following breakdown:

- Acceptance criteria: 46 points  
- Report: 12 points  
- Peer assessment: 5 points (assigned individually)  

The report is graded based on its presentation, organization, and *how clearly things are described*. All the items described in the Acceptance Criteria section above must appear in the report.

Each member must assess their team members' contributions on eClass. This is worth 5 points of the total assignment grade and is confidential (results go to the course staff). Note that if we find *big* discrepancies in contributions or if one team member is negatively rated by all other team members, *then* we will investigate and regrade team members as needed.

