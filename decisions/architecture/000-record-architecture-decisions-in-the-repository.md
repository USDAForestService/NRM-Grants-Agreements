# 0. Record architecture decisions in the repository.

Status: proposed   \
Date: 26 July 2021

This file is itself an ADR.


## Decision Proposed

In order to support clear decision-making, enable a smooth vendor transition, arrive at appopriately stable technical decisions, and provide a clear historical record of technical decisions, we are proposing the use of Architectural Decision Records (ADRs).


## Options Under Consideration

### [Option] Don't use ADRs
The "do-nothing" option is to not use ADRs and not document decisions.

#### Pros
- Some time saved not writing ADRs, socializing them, and making decisions explicit.

#### Cons
- Decision-making may continue to be opaque, even to team members.
- Technical stack churn and misalignment is likely to continue. This will more than make up for time saved by not using ADRs.
- Vendor may not have a clear understanding of the rationale for the technical stack and related decisions; could lead to further churn and confusion during transition process.

### [Option] Use ADRs in the repository
We could start to use ADRs to document our technical decisions. This file is an example of an ADR.

Architecture Decision Records are described by Michael Nygard in this article: https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions

#### Process
The typical process might include the following.

When a technical decision (defined below) needs to be made, someone proposes an ADR and writes it up in the [decisions/architecture folder of the GitHub repository for NRM G&A][repo], following the template format.

A "technical decision" means a decision about the technical architecture, especially that with significant consequences for how we build. This includes (but is not limited to) programming language, frameworks or major consequential libraries/packages, hosting infrastructure, resources (e.g. databases, caches, and other backing services), authentication methods, consequential software architecture patterns, and more.

Toward the bottom of the proposed ADR, the author makes a first attempt at identifying the individuals who are [Responsible, Accountable, Consulted, and Informed][raci]. The shared understanding should be that the first few drafts of this list may be incomplete or inaccurate, and commenters should propose amendments without taking incorrect classifications personally.

The author commits the proposal to a new branch and submits a pull request. They also open a [discussion thread][discussion], linking the ADR in the first post.

Adequate time should be given for:
  1. identifying the relevant decision-makers within the organization, so as to increase the likelihood of the decision persisting,
  2. discussing the proposal and researching the options, and
  3. holding decision-making processes.

Once the decision is made, the decision-makers (or a smaller delegation) amend the ADR on the unmerged branch. They fill in the Decision Outcome (accepted or rejected), Positive Consequences, Negative Consequences, Decision History, Status, and Date. Someone else reviews the changes and merges the PR. (To clarify: one PR per ADR, to propose, amend, and merge it.)

[raci]: https://www.planstreetinc.com/raci-chart/
[repo]: https://github.com/USDAForestService/NRM-Grants-Agreements
[discussion]: https://github.com/USDAForestService/NRM-Grants-Agreements/discussions/categories/architectural-decision-records/

#### Pros
- __Socializing a proposal publicly__ leads to better chances of:
  - Identifying all relevant decision-makers and involving them in the process
  - Improving the likelihood of a decision persisting or "sticking"
  - Avoiding churn, extra development effort, and extra cost
  - Sustaining morale across the entire team
- __Making the decision-making process explicit__ leads to better chances of:
  - Team alignment
  - Appropriately vetted decisions
- __Aligns with best practices__ identified by many technical organizations, including [18F](https://18f.gsa.gov/2021/07/06/architecture_decision_records_helpful_now_invaluable_later/), [Cognitect](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions), and others.
- __Using the GitHub repository__ keeps the decisions close to the code, and works around issues of unqueal access to ADRs. 18F cannot use Teams until acquiring a LincPass, Forest Service & USDA cannot natively use Google Docs, but both teams are able to use GitHub.

#### Cons
- May take longer up front to make a decision ([counterargument] but with the benefits of a clearer process, more likelihood for buy-in, and less likelihood of time spent later on re-evaluation, etc.)
- Not a perfect process: does not provide guidance on who is Responsible, Accountable, Consulted, or Informed ([counterargument] but making this as clear as possible in an ADR will be better than not doing this analysis to begin with)
- Setting up an ADR requires some familiarity with GitHub ([counterargument] but this can be done entirely through the GitHub GUI/web interface).


### [Option] Use ADRs stored in other platforms

### Pros
Same as above, except the one about GitHub.

- Team members do not have to be familiar with GitHub to author and submit an ADR ([counterargument] However, the GitHub GUI would facilitate this process, and an ADR template handles nearly all of the Markdown formatting already).

### Cons
Same as above, except the one about Github. In addition:

- Using a platform other than GitHub creates issues of access. 18F and vendor team members may have difficulty and significant delays (weeks or months) in accessing the USFS Teams and Box accounts, and USFS has difficulty commenting & editing in Google Docs. This may not be a one-time issue, either—if a vendor hires a new developer, then that new developer could be delayed in accessing this shared historical record.
- The code and the decisions about the code are separate. Those with access to the repository may be blocked from accessing the ADR record that explains essential attributes of the repository.

## Decision Makers

### Responsible / Accountable
- Jay Berg (Product Owner, USFS)
- Chris Coppenbarger (Product Manager, USFS)
- Adam Shepherd (Tech Lead, USFS)

### Consulted
- Matt Cloyd (Consulting Engineer, 18F)
- Neil Martinsen-Burrell (Project Lead & Consulting Engineer, 18F)
- Magdaline Derosena (Product Manager, 18F)
- Melissa Braxton (UX, Research, and Design, 18F)
- Christine Bath (Product Design, 18F)

### Informed
To do.


## Decision Method
To come. (How the decision was made: by consensus, by vote, etc. Example: The Responsible and Accountable parties came to consensus and agreed to accept this ADR.)


## Decision History

- Proposed: 26 July 2021
