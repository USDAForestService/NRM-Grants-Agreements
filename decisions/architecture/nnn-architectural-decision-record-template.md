# NNN. Short title of problem and solution (e.g. Use Postgres as default database)

Status: proposed | rejected | accepted | deprecated | superseded by [ADR-NNN](nnn-example.md)
Date: DD Month YYYY (e.g. 22 July 2021)
Technical Story: description or ticket/issue URL (optional)

## Context

Describe the context and problem statement, e.g., in free form using two to three sentences. You may want to articulate the problem in form of a question.

## Decision Drivers (optional)

- Driver 1, a driving force, a concern, a political consideration, etc.
- Driver 2
- Driver 3

## Decision (Proposed|Outcome)

Description of the decision made, and rationale.

e.g. We have decided to use PostgreSQL across the system and maximize the use of database-agnostic SQL.

- The PostgreSQL Product-as-a-Service (PaaS), being based on an open source platform, is about 1/3 the hourly price of a similar, commercial database PaaS and performs similarly.

- We do not have data on whether or not PostgreSQL is commonly used at the partner agency. By using database-agnostic SQL, we aim to mitigate the risk of introducing a new tool into the partner agency's environment.

### Positive Consequences

- Positive consequence
- Positive consequence

### Negative Consequences

- Negative consequence
- Negative consequence

## Options (Under Consideration | Considered)

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

- Proposed:   10 May 2021
- Accepted:   13 July 2021
- Deprecated: 22 Dec 2022
