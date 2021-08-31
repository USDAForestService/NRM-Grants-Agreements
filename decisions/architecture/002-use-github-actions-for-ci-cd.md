# 2. Use GitHub Actions for CI/CD.

Status: proposed   \
Date: 2 August 2021

## Context

We must select a Continuous Integration / Continuous Delivery platform that is in compliance with the Forest Service's list of approved software, and supports isolated builds that deploy based on whether the build passes. It should support our QASP, including accessibility testing and integration testing an Angular/Lambda stack.

## Decision Proposed

We propose using the Forest Service Jenkins instance for CI/CD.

Additionally, we propose setting up Jenkins to [integrate with the GitHub Checks API](https://github.com/jenkinsci/github-checks-plugin) for this repository, so that failed checks are reported back to GitHub and merges are blocked until checks all pass.

### Positive Consequences

- Meets technical requirements
- Aligns with standard practice in the Forest Service
- Takes advantage of excellent support from Jenkins team
- No cost to use

### Negative Consequences

- Because support from the Jenkins team is necessary for many CI/CD changes, this might occasionally become a blocker to CI/CD changes.
- Access to CI/CD checks for new developers depends on some USDA onboarding, leading to minor initial delays.


## Options Under Consideration

### Jenkins
We considered using the Forest Service Jenkins instance, and researched this option via calls with Chaochung Tsai, Jai Jaiprakash, Matt Reiss, and other members of the Skynet team.

#### Pros
- Authorized for use.
- Jenkins is standard practice for the Forest Service.
- No cost to use.
- Significant "customer support" from the Skynet team.
- Jenkins tasks are written in Groovy, which is a relatively simple language to understand.
- Supports Docker Compose

#### Cons
- Changes to Jenkins almost always require support from the Jenkins team. (**counterargument**: this support comes with significant benefits, and some changes can be made through Pull Requests)
- Jenkins is not set up to isolate application's configuration from one another—since Jenkins tasks are shared Forest Service-wide, others' work on Jenkins could introduce bugs into our workflow, and vice versa.
- Jenkins tasks are very verbose and not style-checked, which creates a longer time and higher effort for reading an understanding a given task. (**counterargument**: Application developers may not need to become highly familiar with Jenkins, due to the FS customer support)
- Jenkins tasks are stored not close to the code, but in a Forest Service repo with task files stored across multiple directories, making it harder to concisely read, edit, and understand.
- Notifications are not as clear or directed (failures are emailed to the entire team, not the individual who checked in the code).

#### Questions
- Can Jenkins talk to the GitHub API (to block merging on failed builds, etc.)?

### GitHub Actions

#### Pros
- Authorized for use.
- Functionally unlimited free usage for our open-source repository.
- [Supports Docker](https://docs.github.com/en/actions/creating-actions/creating-a-docker-container-action) and Docker Compose, which will allow us to test multi-container environments, promising the flexibility to fully test an Angular/Lambda stack.
- The GitHub community has built a library of actions. Even if we don't use these actions directly, we can leverage a significant codebase of open source code, including tasks written in/for TypeScript.
- GitHub Actions tasks can be written using any language, so we could write tasks in TypeScript to eliminate needing to context-switch when working on CI/CD.
- Keeps CI/CD setup within the repository, in one place, close to the code (`.github/workflows`).
- Migration from CircleCI to GitHub Actions is much more straightforward than to any of the other platforms assessed here.
- Can natively block merging and deploys when failed checks occur.
- Clear, targeted messaging & notifications.

#### Cons
- Despite an extensive library, we may need to write our own actions for security hardening purposes. ([counterargument] This need to write our own tasks is also true of Jenkins and Azure DevOps, the other two contenders, and it is arguably easier to do so in GitHub Actions than in the others. Additionally, tasks written for this project may benefit other FS, USDA, and 18F projects using GitHub Actions.)
- No support from a dedicated team external to the application developers.


### Azure DevOps

#### Pros
- Authorized for use.
- Many of the same pros as GitHub Actions.
- Supports 10 parallel jobs with unlimited minutes on Windows, Linux, and macOS for open source projects. (No cost.)

#### Cons
- Mismatch in terms of infrastructure, as this is Azure-first. Deploying to remote infrastructure seems possible, but it's not clear how supported it is. AWS is only mentioned once in the docs, and not as a deployment target.
- Not as integrated with GitHub as a GitHub-built service like GitHub Actions.
- Building a task and task syntax reads as a little more complex than GitHub Actions.

#### Questions
- Has USFS used Azure DevOps before, especially in ways similar to how we would use it?


### Maven, MS Build, jFrog Artifactory Edge

#### Pros
- Authorized for use.

#### Cons
- Does not align with technical stack. (Tools are specifically for Java or Microsoft.)


### CircleCI

#### Pros
- Many of the same pros as GitHub Actions.
- No migration required.

#### Cons
- Not authorized for use at Forest Service.


## Decision Makers

### Accountable
- Heather Busam (System Owner, USFS)
- Hugh Nguyen (ISSO, USFS)

### Responsible
- Adam Shepherd (Tech Lead, USFS)
- Jay Berg (Product Owner, USFS)
- Chris Coppenbarger (Product Manager, USFS)

### Consulted
- Matt Cloyd (Consulting Engineer, 18F)
- Neil Martinsen-Burrell (Project Lead & Consulting Engineer, 18F)
- Matt Reiss (Cloud Solutions Architect @ Skynet, USFS)
- Jai Jaiprakash (Senior Consultant, Forest Service Contractor)

### Informed
- Chaochung Tsai (CI Application Developer, USFS)

## Decision Method

TBD

## Decision History

- Proposed: 2 August 2021
