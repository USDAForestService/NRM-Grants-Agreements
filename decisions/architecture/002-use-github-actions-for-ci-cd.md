# 2. Use GitHub Actions for CI/CD.

Status: proposed   \
Date: 2 August 2021

## Context

We must select a Continuous Integration / Continuous Delivery platform that is in compliance with the Forest Service's list of approved software, and supports isolated builds that deploy based on whether the build passes. It should support our QASP, including accessibility testing and integration testing an Angular/Lambda stack.

## Decision Proposed

We propose using GitHub (ZenHub?) Actions for our CI/CD platform.

### Positive Consequences

- GitHub Actions meets our compliance and technical requirements, and will support the proposed technical stack.
- In concert with an open-source repository, GitHub Actions will add no cost to the project.
- The CI/CD configuration and tasks will be kept close to the code, in the repository itself, making it accessible to G&A developers.
- GitHub Actions will be easier to read, understand, and maintain, compared to other options.

### Negative Consequences
(None apparent.)


## Options Under Consideration

### Jenkins
We considered using the Forest Service Jenkins instance, and researched this option via calls with Chaochung Tsai and Jai Jaiprakash.

#### Pros
- Authorized for use.
- Jenkins is standard for the Forest Service.
- There is evidence of good customer support from the team (including Matt Reiss and Chaochung Tsai).
- Jenkins tasks are written in Groovy, which is a relatively simple language to understand.

#### Cons
- The lift required to support an Angular/Lambda technical stack is unclear and potentially risky (time-consuming/costly without guaranteed payoff).
- Jenkins does not support isolated builds: for example, pa11y is not run against a test server, but against live URLs already deployed elsewhere. This method does not properly indicate whether tests are passing in the current build. This is guaranteed to be a source of Section 508/WCAG compliance issues, deployment difficulty, and confusion.
- Changes to Jenkins come with high overhead, requiring support from the Jenkins team. The time to iterate on CI/CD is likely to be extremely high, because of a lack of automation, isolation, and ability for developers to make changes without support.
- Jenkins is not set up to isolate application's configuration from one another—since Jenkins tasks are shared Forest Service-wide, others' work on Jenkins could introduce bugs into our workflow, and vice versa.
- From conversations with folks working on Jenkins, it seems __unlikely__ that Jenkins will be able to support technical/QASP needs such as integration testing a Lambda-based stack or running Pa11y for accessibility testing.
- pa11y testing is not supported and therefore does not meet our QASP requirements. (While there is a `run_pa11y` task in Jenkins, the task runs against already-deployed code, not a running server within an isolated build. It is not clear whether a proper run is possible on Jenkins; at the minimum, it has not been set up before)
- Jenkins tasks are very verbose and not style-checked, which creates a longer time and higher effort for reading an understanding a given task.
- Jenkins tasks are stored not close to the code, but in a Forest Service repo with task files stored across multiple directories, making it harder to concisely read, edit, and understand.

It is possible that Docker on Jenkins might support more of our needs. However:

- In order to determine if Docker on Jenkins is feasible, it requires contacting two individuals at FS who *may* have experience in Docker, working with them to set up a container via a Jenkins task, and getting onboarded to the FS/USDA private Docker repository to host our image. (They have not yet responded to a request for a meeting.)
- We might be able to use Docker for pa11y testing, but it is not clear if Docker or Docker Compose are supported.
- Without clear support for container orchestration, it's unlikely that Jenkins could support integration testing of a serverless stack.


### GitHub Actions

#### Pros
- Authorized for use.
- Functionally unlimited free usage for our open-source repository.
- [Supports Docker](https://docs.github.com/en/actions/creating-actions/creating-a-docker-container-action) and Docker Compose, which will allow us to test multi-container environments, promising the flexibility to fully test an Angular/Lambda stack.
- The GitHub community has built a library of actions. Even if we don't use these actions directly, we can leverage a significant codebase of open source code, including tasks written in/for TypeScript.
- GitHub Actions tasks can be written using any language, so we could write tasks in TypeScript to eliminate needing to context-switch when working on CI/CD.
- Keeps CI/CD setup within the repository, in one place, close to the code (`.github/workflows`).
- Migration from CircleCI to GitHub Actions is much more straightforward than to any of the other platforms assessed here.

#### Cons
- Despite an extensive library, we may need to write our own actions for security hardening purposes. ([counterargument] This need to write our own tasks is also true of Jenkins and Azure DevOps, the other two contenders, and it is arguably easier to do so in GitHub Actions than in the others. Additionally, tasks written for this project may benefit other FS, USDA, and 18F projects using GitHub Actions.)


### Azure DevOps

#### Pros
- Authorized for use.
- Many of the same pros as GitHub Actions.
- Supports 10 parallel jobs with unlimited minutes on Windows, Linux, and macOS for open source projects. (No cost.)

#### Cons
- Mismatch in terms of infrastructure, as this is Azure-first. Deploying to remote infrastructure seems possible, but it's not clear how supported it is. AWS is only mentioned once in the docs.
- Not as integrated with GitHub as a GitHub-built service like GitHub Actions.
- Building a task and task syntax reads as a little more complex than GitHub Actions.
- [question] Has USFS used Azure DevOps before, especially in ways similar to how we would use it?


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
- Jai Jaiprakash (Senior Consultant, Forest Service Contractor)

### Informed
- Matt Reiss (Cloud Solutions Architect @ Skynet, USFS)
- Chaochung Tsai (CI Application Developer, USFS)

## Decision Method

TBD

## Decision History

- Proposed: 2 August 2021
