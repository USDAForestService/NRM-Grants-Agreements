# Default database

Status: accepted
Date: 13 July 2021

## Context

We will likely need several relational database cluster instances (and likely per-state logical databases) in order to provide good data isolation within the system. However, usage within an individual database is expected to be fairly basic and undemanding.


## Decision

We have decided to use PostgreSQL across the system and maximize the use of database-agnostic SQL.


## Consequences

- The PostgreSQL Product-as-a-Service (PaaS), being based on an open source platform, is about 1/3 the hourly price of a similar, commercial database PaaS.

- We do not have data on whether or not PostgreSQL is commonly used at the partner agency. By using database-agnostic SQL, we aim to mitigate the risk of introducing a new tool into the partner agency's environment.

- PostgreSQL is 18F's default datastore – this eases engineering onboarding during the engagement.


## Options

### MySQL
We considered a MySQL database, which is the deafult on the original product.

#### Pros
- A pro
- Another pro

#### Cons
- A con
- Another con

### Neo4j
We considered using a graph database like Neo4j, but ultimately decided against it because it doesn't make sense to use a graph-based schema for something this simple.

#### Pros
- A pro
- Another pro

#### Cons
- A con
- Another con


## People Involved

### Responsible
- [A. Person](mailto:anne.person@usda.gov)

### Accountable
- [Some Person](mailto:some.person@usda.gov)

### Consulted
- [Neil Martinsen-Burrell](mailto:neil.mb@gsa.gov)
- [Matt Cloyd](mailto:matt.c@gsa.gov)

### Informed
- [Some peeps](mailto:some.peeps@usda.gov)
- [Another peep](mailto:another.peep@gsa.gov)

## History

- Proposed: 10 May 2021
- Accepted: 13 July 2021
