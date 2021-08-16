# 003. Use a single API Gateway and Lambda function

Status: accepted   \
Date: 6 Aug 2021 \
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

We decided to use a single API Gateway to proxy all requests to a single
Lambda function, which will handle requests internally based on path and method
and parameters.

### Positive Consequences

- Minimal downtime for deploys.
- Route configuration takes place near other application configuration.
- Reversible decision: can re-configure the API Gateway later, and/or decompose the Express app into separate Lambda functions as optimization needs require.

### Negative Consequences
(None apparent. Some complexity moves into Express app, but this isn't necessarily a problem.)

## Options Considered

### [Option Chosen] API Gateway proxies to a single Lambda function

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
  function more complex. This is only a downside if the tools for managing
  routing in the programming language-level framework are weaker than those
  available in of API Gateway.


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
- Lambda function handlers can be very slow in cold-start situations. Another
  18F project found that Lambda's shutoff and restart strategy is opaque, so
  less-used endpoints were often slow because they had been shut down. Some
  research online suggests that shutoff times [have been made longer by
  AWS](https://acloudguru.com/blog/engineering/how-long-does-aws-lambda-keep-your-idle-functions-around-before-a-cold-start),
  but startup times for applications with large dependency loads [can be
  longer than one second]( https://mikhail.io/serverless/coldstarts/aws/).
- Route configuration for API Gateway is separate from other
  programming-language level configuration that our application will use.
- Reversing this decision is harder because it means re-implementing the
  routing that we do have in API Gateway into our Lambda function handlers.


## Decision Makers

### Accountable and Responsible
- [Adam Shepherd](mailto:adam.shepherd@usda.gov) (Tech Lead)

### Consulted
- [Neil Martinsen-Burrell](neil.martinsen-burrell@gsa.gov) (Consulting Engineer)
- [[Matt Cloyd](matt.cloyd@gsa.gov) (Consulting Engineer)

### Informed
- [Jay Berg](mailto:gerald.berg@usda.gov) (Product Owner)
- [Chris Coppenbarger](mailto:chris.coppenbarger@usda.gov) (Product Manager)


## Decision Method

Adam approved the ADR via GitHub. [(Link)](https://github.com/USDAForestService/NRM-Grants-Agreements/pull/367#pullrequestreview-724632547)

## Decision History

- Accepted: 6 Aug 2021
- Proposed: 29 July 2021
