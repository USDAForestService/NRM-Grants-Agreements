# 3. Use NodeJS on Lambda and Angular as a tech stack

Status: proposed   \
Date: 29 July 2021


## Context

Describe the context and problem statement, e.g., in free form using two to
three sentences. You may want to articulate the problem in form of a question.


## Decision Drivers (optional)

- Beginning to develop "for production", making a product intended to be
  handed off to the vendor
- Needing alignment with FS CIO technology modernization vision/plan


## Decision Proposed

Use the Angular framework programmed in TypeScript as a front-end application,
and AWS Lambda with a NodeJS runtime as the backend server. 

In order to reduce the cost associated with context switching between multiple
languages, we propose using TypeScript on the NodeJS/Lambda backend, for an
all-TypeScript stack.

### Positive Consequences

(To do.)

### Negative Consequences

(To do.)


## Options Under Consideration

### Angular & NodeJS on Lambda

#### Pros
- Aligns with the Forest Service technology modernization vision.
- Assuming the modernization vision does not change, it helps the Forest
  Service consolidate many applications onto a common tech stack.

#### Cons
- This complete stack has not been used in the Forest Service previously.
- Migrating legacy apps to this stack has never been done before, and the
  process has not been experimented with enough to know how difficult it will
  be.
- Tools for deploying and managing applications on Lambda are much less mature
  than on other AWS platform-as-a-service offerings such as Elastic Beanstalk.
- There are significant "unknown unknowns" with this stack, including:
  - integration testing
  - scaling (scaling Lambda functions are easy but scaling any attached
    resources is harder)
  - zero-downtime deployments
  - DevOps engineering needs
- Based on our research, this stack is significantly more complicated than
  other stacks that could meet the needs of this application.


### Angular & Python on Lambda

Using the same Angular/TypeScript front-end, we could use a different
programming language runtime on the Lambda backend. Python is one of the
first-class languages available on Lambda and an extremely popular and mature
for web application development.

#### Pros
- Speeds up application development on Grants and Agreements by leveraging
  existing Python-language development work.
- Lowers risk at the vendor transition by allowing 18F's engineering team to
  make more progress by using a more familiar programming language.

#### Cons
- Introduces a new programming language to Forest Service, requiring
  contractors with Python skills to develop and maintain the application.


### Angular & Java Spring

Utilizing the flexibility of the Angular/Lambda architecture, we could use a
Java runtime on Lambda with the Spring Data framework to build the API
backend.

#### Pros
- Matches the technology architecture described in the NRM Modernization
  solicitation that is being awarded.

#### Cons
- Java packaging, deployment, and runtimes are famously resource-intensive and
  Lambda charges increase with the time and resources that an application
  needs.


### Server-side Python application

#### Pros

- A server-side application is the most appropriate level of "innovative": it
  is perhaps the safest, most boring technology choice that would meet the
  needs of the G&A application.
- Allows for rapid progress on this application, leveraging existing
  prototype development work.
- Server-side applications are much easier to get approved for cybersecurity
  compliance because the security risks are more easily understood.
- There are very few unknown unknowns: the "failure modes" of Python are well-known
  and solved, both with unit testing and integration testing
- Django is the #1 web framework for Python, which is by some metrics the 3rd most
  popular computer language in the world.
- Python developers/vendors are common and highly available.
- Aligns with the Forest Service CIO vision to have API access to data. Python
  libraries make the development of REST APIs straightforward.

#### Cons
- Introduces a new programming language to the Forest Service.


## Decision Makers

### Responsible
- [First Last](mailto:first.last@usda.gov) (Role)

### Accountable
- [First Last](mailto:first.last@usda.gov) (Role)
- [First Last](mailto:first.last@usda.gov) (Role)

### Consulted
- [First Last](mailto:first.last@usda.gov) (Role)
- [First Last](mailto:first.last@usda.gov) (Role)

### Informed
- [First Last](mailto:first.last@usda.gov) (Role)
- [First Last](mailto:first.last@usda.gov) (Role)
- [First Last](mailto:first.last@usda.gov) (Role)
- [First Last](mailto:first.last@usda.gov) (Role)


## Decision Method

How the decision was made: by consensus, by vote, etc.

e.g. The Responsible and Accountable parties came to consensus and agreed to accept this ADR.


## Decision History

- Proposed:   29 July 2021
