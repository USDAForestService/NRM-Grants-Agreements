console.log("NODE_ENV: " + process.env.NODE_ENV);
console.log("DATABASE_URL: " + process.env.DATABASE_URL);

import express, { Request, Response, NextFunction } from "express";

import Grant from "./models";

const app = express();
const port = 3000;

/**
 * @todo Set using environment variables for security hardening.
 */
app.use(function (req, res, next) {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "*");
  res.setHeader("Access-Control-Allow-Headers", "*");
  next();
});

const awaitErrorHandlerFactory = (middleware: any) => {
  return async (request: Request, response: Response, next: NextFunction) => {
    try {
      await middleware(request, response, next);
    } catch (err) {
      next(err);
    }
  };
};

/**
 * @todo Set the JSON to be { data: grants } and have Angular read the data
 */
app.get(
  "/grants",
  awaitErrorHandlerFactory(
    async (request: Request, response: Response, next: NextFunction) => {
      let grants: Grant[] = await Grant.findAll({ limit: 10 });
      return response.status(200).json(grants);
    }
  )
);

/**
 * @environment development
 * When deployed, the lambda.js file only uses the exported app and
 * doesn't run app.listen.
 */

if (process.env.NODE_ENV == "development") {
  app.listen(port, () => {
    console.log(`NRM G&A API running on port ${port}.`);
  });
}

module.exports = app;
