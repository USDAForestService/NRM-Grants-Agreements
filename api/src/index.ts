import express, { Request, Response, NextFunction } from 'express';

const app  = express();
const port = 3000;

/**
 * @todo Set using environment variables for security hardening.
 */
app.use(function(req, res, next) {
  res.setHeader('Access-Control-Allow-Origin',  '*')
  res.setHeader('Access-Control-Allow-Methods', '*')
  res.setHeader('Access-Control-Allow-Headers', '*')
  next();
});

enum Status {
  None = "---",
  One = "01",
  Two = "02",
}

enum AppSubmissionType {
  New = 'NEW',
  Application = 'Application',
  Preapplication = 'Preapplication',
  NonConstructionApplication = 'NON-CONSTRUCTION APPLICATION',
  NonConstructionPreApplication = 'NON-CONSTRUCTION PRE-APPLICATION',
}

interface Grant {
  cn: string;
  projTitle: string;
  projStatus: Status;
  appSubmissionType: AppSubmissionType;
}

const getGrants = (
  request: Request,
  response: Response,
  next: NextFunction
) => {
  let grants: Grant[] = [
    {
      cn: '100X100X100X',
      projTitle: 'Forest Service Project',
      projStatus: Status.None,
      appSubmissionType: AppSubmissionType.New
    },
    {
      cn: '101AB101AB101AB',
      projTitle: 'Timber Project',
      projStatus: Status.One,
      appSubmissionType: AppSubmissionType.Application
    },
    {
      cn: '202C202C202C',
      projTitle: 'Swales & Marshes',
      projStatus: Status.One,
      appSubmissionType: AppSubmissionType.Preapplication
    },
    {
      cn: '020D020D020D',
      projTitle: 'Pasture Land',
      projStatus: Status.Two,
      appSubmissionType: AppSubmissionType.NonConstructionApplication
    }
  ];

  response.status(200).json(grants);
}

app.get('/grants', getGrants);

/**
 * @environment development
 * When deployed, the lambda.js file only uses the exported app and
 * doesn't run app.listen.
 */
app.listen(port, () => {
  console.log(`NRM G&A API running on port ${port}.`)
});

module.exports = app;
