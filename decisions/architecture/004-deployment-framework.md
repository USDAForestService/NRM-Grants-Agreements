# 004. Decide on deployment framework

Status: proposed
Date: 1 September 2021
Technical Story: [Review & decide on a serverless framework #408](https://github.com/USDAForestService/NRM-Grants-Agreements/issues/408)

## Context

In order to set up deployments to multiple environments and manage configuration, we need a framework to deploy resources to AWS.

## Decision Drivers

- Wanting to have a clear plan for deployment as we set up CI/CD

## Decision Proposed

To come.

### Positive Consequences

- To come

### Negative Consequences

- To come

## Options Under Consideration

### Ansible

#### Pros
- Infrastructure as code
- Able to work with AWS resources ([lambda example](https://docs.ansible.com/ansible/latest/collections/community/aws/lambda_module.html))
- Handles deployment to multiple environment
- Uses idempotence as a foundational concept
- Very mature, flexible technology with rich community of resources

#### Cons
- (Unknown) Need to research limitations and pitfalls in production/at scale.

### Claudia.js
**Not intended as a long-term or production deployment framework.**
Presently used to deploy to sandbox, as a quick & easy short-term solution.

Currently blocked on researching Claudia further. Some [tutorial pages](https://claudiajs.com/tutorials/image-server.html) are not providing the content needed to assess.

#### Pros
- Very quick, easy, straightforward to deploy Express apps to Lambda

#### Cons
- Does not manage frontend deployment. (**counterargument**: Frontend deployment could be managed with another tool such as awscli.)
- Limited and disorganized documentation.

### SAM

#### Pros
- Infrastructure as code
- Directly supported by Amazon, whose infrastructure we're using
- Could handle entire deployment: capable of managing [API Gateway, Lambda](api-lambda-sam), CORS, Domains, and [frontend](frontend)
- Handles environment variables for various environments
- Provides local debugging & testing environments
- Provides [a Jenkins plugin for deployment](https://plugins.jenkins.io/aws-sam/)

[api-lambda-sam]: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html
[frontend]: https://serverless.pub/deploy-frontend-to-s3-and-sar/

#### Cons
- (Unknown) Need to research limitations and pitfalls in production/at scale.
- (Risk) ["Extension of AWS CloudFormation"](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html): could be subject to the same scaling issues described under [**Serverless**][#serverless].

### Serverless

#### Pros
- Infrastructure as code
- Supports AWS infrastructure (as well as others such as Tencent, Google, and more)
- Could handle entire deployment: capable of managing [API Gateway, Lambda, CORS](api-lambda-serverless), [Domains](domain-serverless)
- May support frontend deployment through [serverless-s3-deploy plugin](https://www.serverless.com/plugins/serverless-s3-deploy)
- Handles environment variables for various environments
- Provides local runner

[api-lambda-serverless]: https://www.serverless.com/framework/docs/providers/aws/events/apigateway
[domain-serverless]: https://serverless.com/blog/serverless-api-gateway-domain/

#### Cons
- Serverless had serious trouble scaling on a recent 18F project, and had to be replaced.
  - Serverless leverages CloudFormation, which has a resource limit. Scaling Serverless to provision more than one Lambda at a time caused it to reach resource caps quickly.
  - When vendor team hit this limit, they had to fracture the deployment into multiple Serverless deployment steps, running 30 mins, serially, waiting for multiple timeouts.
  - CF gets into locked states easily, could not get around other than deleting the stack and redeploy—which DOES NOT work in production settings.
- Serverless has a nice local runner, but Docker was often running out of memory.
- No identified Jenkins integration


### Terraform

#### Pros
- 18F switched from Serverless to Terraform for another recent project when Serverless ran into scaling issues.
- Used by Forest Service Cloud Foundation team
- To do

#### Cons
- (Unknown) Need to research limitations and pitfalls in production/at scale. May be good to ask Forest Service about this.

## Decision Makers

### Responsible & Accountable
- [Adam Shepherd](mailto:adam.shepherd@usda.gov) (Tech Lead)
- [Jay Berg](mailto:gerald.berg@usda.gov) (Product Owner)
- [Chris Coppenbarger](mailto:christopher.k.coppenbarger@usda.gov) (Executive Sponsor)

### Consulted
- [Neil Martinsen-Burrell](mailto:neil.martinsen-burrell@gsa.gov) (Consulting Engineer & 18F Project Lead)
- [Matt Cloyd](mailto:matt.cloyd@gsa.gov) (Consulting Engineer)
- [Matt Reiss](mailto:matthew.reiss@usda.gov) (Cloud Solutions Architect)

### Informed
- To come.

## Decision Method

To come.

e.g. The Responsible and Accountable parties came to consensus and agreed to accept this ADR.


## Decision History

- Proposed: 1 September 2021
