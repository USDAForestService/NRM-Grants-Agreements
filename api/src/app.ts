import { config } from "dotenv";
import { resolve } from "path";

config({ path: resolve(__dirname, "..", ".env") });

import express, { Request, Response, NextFunction } from "express";
import Grant from "./models";

const app = express();

/**
 * List of available, supported API versions.
 */
const apiVersions = [1];

/**
 * The version in the header is namespaced, specified as:
 *   gov.usda.fs.nrm.ga.version={VERSION}
 *
 * As presently written, versions can only be whole integers.
 *
 */
const apiVersionHeader = /gov\.usda\.fs\.nrm\.ga\.api\.version=(\d+)/;

/**
 * This matches the first segment of the request path, formatted as:
 *   v{VERSION}
 *
 * As presently written, versions can only be whole integers.
 *
 */
const apiVersionPath = /^v(\d+)$/;

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
      console.error(err);
      next(err);
    }
  };
};

const versionMessages = {
  200: {
    title: "OK",
    detail: "Everything is fine.",
  },
  400: {
    title: "No API version specified",
    detail: `An API version must be specified, but no version was specified.
        To specify a version, use one of the following approaches:
        (1) Specify the version in the first segment of the path, e.g. \`/v1/grants\`
        (2) Specify the version in the Accept header: \`Accept: application/vnd.api+json; gov.usda.fs.ga.api.version=1\``,
  },
  404: {
    title: "Version not found",
    detail: `The version specified is not an available API version. Please choose from the following available versions: ${apiVersions}`,
  },
  409: {
    title: "Conflicting versions requested",
    detail:
      "The Accept header and the request path each requested different, conflicting versions. Please ensure that only one version is specified. You can set both the path and header to the same version, or you can request a version using only the path or only the header.",
  },
};

/**
 * Adds a `version` property to Express.Request, so we can attach
 * that metadata as we resolve the version.
 */
declare global {
  namespace Express {
    interface Request {
      version: number;
    }
  }
}

app.use(function (request, response, next) {
  let [statusCode, version] = resolveVersions(request);
  if (statusCode == 200) {
    /**
     * If the first segment includes the version,
     * rewrite the path without the version.
     */
    if (request.url.match(/^\/v\d+/)) {
      request.url = `/${request.url.split("/").slice(2).join("/")}`;
    }
    request.version = version;
    next();
  } else {
    return response.status(statusCode).json({
      errors: [
        {
          status: statusCode,
          title: versionMessages[statusCode].title,
          detail: versionMessages[statusCode].detail,
        },
      ],
    });
  }
});

app.get(
  "/grants",
  awaitErrorHandlerFactory(
    async (request: Request, response: Response, next: NextFunction) => {
      switch (request.version) {
        case 1: {
          let grants: Grant[] = await Grant.findAll({ limit: 10 });
          return response.status(200).json({ data: grants });
        }
        default: {
          return response.status(500).json({
            error: {
              title: "Internal Server Error: No version implemented",
              detail: `Missing implementation for v${request.version}.`,
            },
          });
        }
      }
    }
  )
);

/**
 * If no version is given, return 400 Bad Request.
 * If conflicting versions are given, return 409 Conflict.
 * If unavailable versions are given, return 404 Not Found.
 * If a single valid version is given, pass through to the app.
 */
function resolveVersions(request: Request): number[] {
  let headerVersion: number;
  let pathVersion: number;

  let versions: number[] = getVersions(request);
  [headerVersion, pathVersion] = versions;

  if (headerVersion == undefined && pathVersion == undefined) {
    return [400, undefined];
  } else if (
    typeof headerVersion == "number" &&
    typeof pathVersion == "number"
  ) {
    if (headerVersion == pathVersion) {
      return [200, headerVersion];
    } else {
      return [409, undefined];
    }
  } else {
    const version = headerVersion || pathVersion;
    if (apiVersions.includes(version)) {
      return [200, version];
    } else {
      return [404, undefined];
    }
  }
}

function getVersions(request: Request): number[] {
  let headerVersion: number;
  let pathVersion: number;
  let headerVersionMatch;
  let pathVersionMatch;

  if (request.header("Accept")) {
    headerVersionMatch = request.header("Accept").match(apiVersionHeader);
  }
  if (request.path.split("/")[1]) {
    pathVersionMatch = request.path.split("/")[1].match(apiVersionPath);
  }

  if (headerVersionMatch) {
    headerVersion = parseInt(headerVersionMatch[1]);
  }
  if (pathVersionMatch) {
    pathVersion = parseInt(pathVersionMatch[1]);
  }
  return [headerVersion, pathVersion];
}

export { app };
