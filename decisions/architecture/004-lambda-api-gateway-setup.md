# 004. Use a single API Gateway and Lambda function

Status: proposed \
Date: 29 July 2021 \
Technical Story: https://github.com/USDAForestService/NRM-Grants-Agreements/issues/349

## Context

When using AWS Lambda as a backend platform, there are different ways to
organize the code. AWS provides API Gateway which handles incoming requests
and can route them to Lambda functions based on the path and method of the
request. Individual Lambda functions can then also handle the requests they
get based on the request path and method.

## Decision Drivers

- Simple architecture that is extensible
- API-first access for enterprise-level data strategy

## Decision (Proposed)

We propose to use a single API Gateway to proxy all requests to a single
Lambda function which will handle requests internally based on path and method
and parameters.

### Positive Consequences

- 
- 

### Negative Consequences

- 
- 

## Options Under Consideration

### [Option] API Gateway proxies to a single Lambda function

API Gateway can be configured to send all requests on a certain path on to a
Lambda function using [Lambda proxy
integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html).
The Lambda function handler uses programming language-level frameworks such as
Express or Flask to handle requests and return the responses back to the API
Gateway.

#### Pros
- Simple API Gateway configuration means minimal downtime for deploys
- Route configuration takes place in the same framework as other application
  configuration
- Reversible decision allows for re-configuring the API Gateway if we do want
  to add a small amount of routing at that layer, say between `/app` and
  `/api`.

#### Cons
- Request handling happens inside of the Lambda handler, possibly making that
  function more complex.


### [Option] Per-path Lambdas configured in API Gateway 

One way to use Lambda is similar to that embodied by the Serverless framework
where routing is configured by path at the API Gateway and each portion of the
API is served by separate Lambda functions which individually handle requests
for a certain type of information.

#### Pros

- Frameworks such as Serverless may be easiest to use this way
- Each lambda function is simpler because it handles one type of request

#### Cons

- Resource limits in CloudFormation mean that this approach is not scalable to
  a large or complex API, because each route in API Gateway means creating
  multiple different AWS resources.
- API Gateway deploys are not zero-downtime, so the more often API Gateway
  configuration changes, the more often that there will be system downtime on
  deploys.
- Individual Lambda function handlers are slower to start on their first
  usage, so after a restart, the application can be very slow and the problem
  is worse with more separate function handlers.
- Route configuration for API Gateway is separate from other
  programming-language level configuration that our application will use.
- Reversing this decision is harder because it means re-implementing the
  routing that we do have in API Gateway into our Lambda function handlers.


## Decision Makers

### Responsible
- [Neil Martinsen-Burrell](neil.martinsen-burrell@gsa.gov) (Consulting Engineer)
- [[Matt Cloyd](matt.cloyd@gsa.gov) (Consulting Engineer)

### Accountable
- [Adam Shepherd](mailto:adam.shepherd@usda.gov) (Tech Lead)

### Consulted
- [Jay Berg](mailto:gerald.berg@usda.gov) (Product Owner)
- [Chris Coppenbarger](mailto:chris.coppenbarger@usda.gov) (Product Manager)

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
