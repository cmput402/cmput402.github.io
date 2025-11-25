title: Group Assignment 4: Static Analysis
date: 2025-10-26
tags: labs, policy, grading
authors: Hazel Victoria Campbell, Sarah Nadi
status: published
----

[TOC]

# Overview

In this project, you will evaluate the structural quality and maintainability of your Tartan Home Platform implementation by conducting static code analysis. You will use static analysis tools, including SpotBugs, PMD, and Error Prone, to identify potential defects and code quality issues without executing the system. These tools allow early detection of issues such as poor coding practices, possible null dereferences, and violations of coding standards, helping improve overall code reliability and maintainability.

Learning goals: 

*	Gain experience using a static analysis tool.
*	Understand what types of defects can and cannot be found with static analysis.
*	Critically evaluate the results of static analysis tools.

**NOTE**: You will continue to work on the same Tartan Home repository you created through GitHub Classroom for the previous projects. Please check Canvas for deadlines.

# Resources

You will use three static analysis tools to analyze your Tartan codebase for potential problems: **SpotBugs**, **PMD**, and **ErrorProne**.

To run **SpotBugs**, you have a few options:

* Use the [SpotBugs Gradle Plugin](https://plugins.gradle.org/plugin/com.github.spotbugs) to add it to your build.  
* Download the standalone version and run it as a Java application. See the [installation](https://spotbugs.readthedocs.io/en/stable/installing.html) and [running](https://spotbugs.readthedocs.io/en/stable/running.html) instructions.  
* You can also install it as a plugin in **IntelliJ IDEA** or **Eclipse**.

To use **PMD**, you can:

* Add it to your build using the [PMD Gradle Plugin](https://docs.gradle.org/current/userguide/pmd_plugin.html).  
* Or run it directly from the command line without editing your Gradle file. See the [PMD CLI guide](https://pmd.github.io/latest/pmd_userdocs_installation.html#running-pmd-via-command-line).

To run **ErrorProne**, follow the [Gradle ErrorProne Plugin guide](https://github.com/tbroyer/gradle-errorprone-plugin) to add it to your build setup. You can find more details at [errorprone.info](http://errorprone.info).


# Task

Run SpotBugs, PMD and ErrorProne on your Tartan system and analyze the results. Specifically:

1. (5 marks) Report how many errors/warnings were reported by each tool and in which categories (note that the category names or how errors/warnings are categorized in each tool may be different for each tool).
2. (5 marks) Report the similarities and discrepencies between the tools. Are there errors/warnings that one tool reports but the other doesn't (give at least 3 examples, if available)? Are there error/warnings that all three tools report? (give at least 3 examples, if available)
3. (5 marks) Report which Java class(es) from Tartan seems most problematic. Explain your result.
4. (60 marks total) Select 10 reported problems, distributed across the three tools, to analyze in more detail. For each problem, report
	* (2 marks) The identifying information for the bug, including its category, priority, file name, and line number.
	* (1 mark) A one-sentence description of the problem
	* (2 marks) A characterization of the bug in terms of whether it is an actual problem, false positive, or irrelevant true positive. Explain your reasoning.
	* (1 mark) How you fixed the problem (if you decided it was actually a problem)

(5 marks) Peer-rating of group members. This is assigned individually. Note that if we find big discrepencies in contributions or if one team members is negatively rated by all other team members, then we will investigate and regrade team members as needed.

**NOTE**: Your report must include all of the above components. Incomplete submissions may result in grade deductions. The total points for this assignment is 80 marks.

# Submission Requirements

- Submit a PDF report (max. 4 pages of text, including screenshots/tables, etc) via Canvas.
- Include your team's repository link in the report.
- Please name your file using the following format:
    - `<LabCode>_<GroupName>_G4_Report.pdf`
    - Example: `D01_m01_G4_Report.pdf`
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

The requirements for the report are the same as for [part 1]({filename}basics.md#report-format).

# Questions you should be able to answer after this assignment

* What is a false positive?
* What is a false negative?
* Are there problems in the code that the tool did not catch?
* Does running a static analysis tool replace the need for testing?

Copyright 2021, 2022 Dr. Sarah Nadi. Copyright 2023, 2024 Dr. Hazel Campbell. All rights reserved.
