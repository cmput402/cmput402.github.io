Title: Group Assignment 3: Testing in Production
date: 2025-09-20
tags: labs, policy, grading
authors: Hazel Victoria Campbell, Sarah Nadi
status: published
----

[TOC]

# Overview

In this project, you will build infrastructure for Tartan in order to conduct tests in
production. First, you will deploy your application with [Docker
containers](https://www.docker.com/resources/what-container) and automate
deployment into production, as well as making it easy to roll back changes.
Second, you will extend the project and build an AB testing infrastructure that
can be used to assess specific changes.

Learning goals:

- Design an AB-testing infrastructure to run tests in production.
- Deploy the system through a virtualized infrastructure and support rapid updates and rollback operations with test automation.
  
**NOTE**: You will continue to work on the same Tartan Home repository you created through GitHub Classroom for the previous projects. Please check Canvas for deadlines.

# Part 1: Continuous Deployment

Having learned about continuous deployment, members of your company are curious
to try it. You will investigate Docker containers and run your infrastructure
in containers. You can also run the house simulators in Docker containers if
you like. Because your company does not have in-house server machines, your
company is going to acquire VM resources from
[Cybera](https://cloud.cybera.ca/).  Since Cybera uses
[OpenStack](https://www.openstack.org/software/) to manage its computing
resources, you will also use it to create your own VM instance. After creating
and configuring that instance (e.g., associate a floating (public) IP address,
install Docker), you will deploy and run your containers there. Note that we
already provided a setup for Docker (`docker-compose.yml` file) with the
original release, which you are welcome to use or modify.

You will need to extend your build and test automation, such that Docker containers for all
backend services (controller, database, and possibly additional services you
may create) are *created automatically* every time you push a commit to GitHub
and it passes all tests. You can either *launch* the new containers
automatically, replacing the currently running ones, or provide a lightweight
mechanism where a human operator can launch a new version with a single button
or command-line instruction. (The house simulators are not part of the backend
and should usually continue running while the controller is updated.)

Finally, implement a technique for how to undo a release and revert back
to the previous version. Similar to releasing new versions, undoing a release
should be possible with a single button click or command-line instruction. Make sure to test your roll-back technique and to fully document the exact steps that should be done to perform a roll-back.

For the purpose of this assignment, it is not necessary to roll out changes incrementally or build a canary test infrastructure. However, you may possibly need to slightly modify the controller or houses to deal with short-term connection failures during updates.

# Part 2: AB Testing

In addition to automating deployment, you will extend the Tartan Smart Home
system with a **reporting feature** that sends customers weekly or monthly reports
about how they use their system. You will then design an experimentation
infrastructure in which you test different versions of the reporting "in
production" to see whether customers change their behaviour.

You have significant flexibility in the assignment in deciding what kind of
reporting you add and what kind of experiments you want to run. For example,
you may find inspiration in decades of
[studies](https://www.sciencedirect.com/science/article/pii/0378778894009124)
that analyzes what kind of information in electricity bills actually encourages
customers to reduce their electricity consumption, but you can also report on
other behaviour of the smart home, such as temperature, door locking status,
etc. Note that building the experiment infrastructure is more important than
the actual experiments and certainly more important than whether your new
reporting feature looks pretty.

In this assignment, you may want to change multiple parts of the system or may be able to work only with modular additions (e.g., adding a new microservice for reporting and another one for configuration and analysis). Given that you
cannot actually test with a production system yet (the team developing the
hardware for the houses is still not ready, \*sigh\*), you may want to change the
simulation infrastructure to have more houses and houses with different
behaviour to test your infrastructure in simulation.

Specifically:

- Build a reporting system that creates reports for each customer with a Tartan Smart Home installation, reporting an aspect of your choice. For example, how much electricity they are using or how long they are keeping their lights on. Users should be able to see this information on their UI.
- Build an experimentation infrastructure that (a) allows you to send different versions of the reports to different customers or at different times (For example, you can show one set of users their electricity usage using kWh and show another set of users their estimated cost of electricity), (b) analyzes whether these changes have an effect on outcomes of how these customers use the system. You may need to modify how you track different customers, and you may need to collect additional data about outcomes.
- At the end of the experimentation period, generate some form of visualization (e.g., chart, graph, table, whether as an HTML page or as a downloadable file) that shows which report variant was sent to which customer and how it affected them. For example, the result can be that the users who were shown the cost of electricity usage is now using less electricity than the ones who were shown their kWh usage. You can have the downloadable file in your repository or in Google Drive, and mention the link to the file in your group assignment report.

# Part 3: Testing Reflection Presentation
Each team must submit a video presentation (max 8 minutes) reflecting on the testing concepts and practices applied throughout G1 to G3. The video should summarize your team’s learning outcomes, testing strategies, and key takeaways. You should conduct the presentation like you would a live presentation to shareholders, e.g., demo important/interesting features of your application and experiment. **You should not need to do any video editing**. A phone camera recording is sufficient.

## Purpose
Demonstrate your team’s understanding of the software testing lifecycle and highlight key lessons learned. It also provides an opportunity to reflect critically on the development and testing strategies used in your implementation. 

## Content Guidelines
* **Team Introduction (~1 minute)**  
  * Group name and member names  
  * Brief summary of each person’s contribution  
* **Testing Learnings (~2 minutes)**  
  * What testing strategies did you apply (e.g., unit, integration, system)?  
  * How did your team improve test coverage and mutation scores?  
  * What were the main challenges you faced during testing, and how did you address them?  
* **Continuous Deployment & Experimentation (~2 minutes)**  
  * What did you learn from implementing CI/CD pipelines and rollback mechanisms?  
  * What insights did you gain from designing and running AB tests?  
* **Key Takeaways (~2 minutes)**  
  * What would your team do differently next time?  
  * Which testing skills do you think will be most useful in future projects or jobs?  
* **Closing Remarks (~1 minute)**  
  * Final thoughts, acknowledgements, or creative elements (optional)
 
This component will be assessed based on clarity, depth of reflection, and your ability to communicate testing knowledge effectively. All team members are expected to participate.

## Submission for video presentation

All teams are required to upload their Testing Reflection Presentation video to **YouTube** as an **Unlisted** video. The video link must be clearly included in the G3 report. The video must be publicly accessible. Failure to provide a working YouTube link will result in grade deductions.


# Acceptance Criteria

The following criteria must be satisfied for the assignment to be accepted as complete.

| Criteria (Continuous Deployment) | Grade |
| :------------------------------- | :----|
| The system, including the simulation of houses and the new experimentation infrastructure, is deployed with Docker containers. | 10 |
| All changes that pass the automated test suites are *automatically built* as deployable Docker containers. | 15 |
| The *deployment* of newly built versions of the Docker containers on the virtual machine is either fully automated or can be done with a single command that is described in the repository's README file. | 20 |
| Reverting the running system to the previous version can be achieved with a single command that is described in the repository's README file. | 15 |

| Criteria (AB Testing) | Grade |
| :-------------------- | :---- |
| A reporting system has been implemented that can periodically send reports to customers. | 15 |
| An experimentation infrastructure has been implemented that tracks which customers should see which variants of the software. **\*NOTE:** At least two report versions are implemented. The report must include a table showing which house received which version, along with the file path to the config.| 20 |
| An analysis infrastructure has been implemented that can evaluate the outcome of experiments (given one metric, how did the customer's behaviour change). | 15 |
| An experiment has been conducted using the experimentation infrastructure, sending different variants of the report to different customers and observing different outcomes. | 20 |

| Criteria (Testing Reflection Presentation) | Grade |
| :---- | :---- |
| Content Coverage: The video addresses all required topics (testing strategies, CI/CD, AB testing, key takeaways, etc.) | 6 |
| Depth of Reflection: The team demonstrates critical thinking and insight into their testing practices and learning process. | 6 |
| Clarity and Communication: The presentation is structured, well-paced, and easy to follow | 5 |
| Team Participation: All team members contribute meaningfully to the video **Note**: A team member’s sole contribution to G3 can NOT be solely performing **optional** video editing. All members must contribute to the work of G3 itself. | 2 |
| Creativity and Engagement (Optional): The team presents the material in an engaging or innovative way | 1 (bonus) |

## README
In your repository, please include technical documentation of how to launch containers, update containers after a build, and revert containers. Documentation should be organized according to the repository structure. All required commands must be easy to find and clearly explained.

# Report for Parts 1 & 2

The following describes the required details of the report:

* **Reporting feature** (\<1 page text): Describe your reporting feature and the goal for which you are optimizing (e.g., reducing energy consumption); include an example of a report.  
* **Experiment design** (\< 1 page text): Describe your experiment(s): what are the experimental conditions (independent variables) and measured outcomes (dependent variables), and how you measure those.  
* **Experimentation infrastructure** (\< 1 page text): Describe how you assign experimental conditions: how you implement experimental conditions (e.g., branches, feature flags); how you assign control and treatment groups; and a short justification why you chose this implementation/design.  
* **Analysis infrastructure** (\<1 page text): Describe how you analyze the outcome of the experiment. We encourage you to include a screenshot showing the outcome of your experiment.

# Submission Requirements

- **Please tag your code with `G3_Done`**
- Submit a [Zipped PDF report]({filename}/general/report.md) (max. 4 pages of text, including screenshots/tables, etc) via Canvas.
- Include your team's repository link in the report.
- Please name your file using the following format:
    - `<LabCode>_<GroupName>_G3_Report.zip`
    - Example: `D01_m01_G3_Report.zip`
- Meets the formatting requirements in the previous section. Marks may be lost or you may receive a zero if the report is not **easy** to read and professional, or if it does not meet the formatting above.

# Grading Summary

In total, G3 is worth 177 (176 + 1 bonus) points with the following breakdown:

* Continuous Deployment: 60  
* AB Testing: 70  
* Report: 12  
* README: 10  
* Testing Reflection Presentation: 20 (19 + 1 bonus)
* Peer assessment: 5 (assigned individually)

The report is graded based on its presentation, organization, and how clearly things are described. All the items described in the Report section above must appear in the report. The ReadMe is graded based on whether all instructions we need to run things are there or not (Be very explicit. Do not assume we know how to run things)

Each member must assess their team members' contributions on eClass. This is worth 5 points of the total assignment grade and is confidential (results go to the course staff). Note that if we find big discrepancies in contributions or if one team member is negatively rated by all other team members, then we will investigate and regrade team members as needed.

Copyright 2021, 2022 Dr. Sarah Nadi. Copyright 2023, 2024 Dr. Hazel Campbell. All rights reserved.
