// This file can be replaced during build by using the `fileReplacements` array.
// `ng build` replaces `environment.ts` with `environment.prod.ts`.
// The list of file replacements can be found in `angular.json`.

export const environment = {
  production: false,

  /**
   * @todo Remove `v1` from the URL string and intercept outbound
   * requests to the API to set default headers for Content-Type and
   * version, or implement JSON:API client library.
   *
   * https://angular.io/guide/http#setting-default-headers
   */
  api_root: 'http://localhost:3000/v1',
};

/*
 * For easier debugging in development mode, you can import the following file
 * to ignore zone related error stack frames such as `zone.run`, `zoneDelegate.invokeTask`.
 *
 * This import should be commented out in production mode because it will have a negative impact
 * on performance if an error is thrown.
 */
// import 'zone.js/plugins/zone-error';  // Included with Angular CLI.
