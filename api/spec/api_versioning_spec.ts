import request from 'supertest';

import { app } from '../src/app'

describe('API', () => {
  /**
   * @todo Add expectations for the version that gets returned,
   *   e.g. expect 'X-API-Version', /1/
   *
   * @todo Ideally, these would not be integration tests (depending
   *   on app response, database queries) and would instead just
   *   test the routing functionality.
   */
  describe('Versioning', () => {

    describe('without a version', () => {
      describe('with JSON:API Content-Type', () => {
        it('Returns a 400 Bad Request', (done) => {
          request(app)
            .get('/grants')
            .set('Accept', 'application/vnd.api+json')
            .expect(400, done);
        });
      });

      describe('without JSON:API Content-Type', () => {
        it('Returns a 400 Bad Request', (done) => {
          request(app)
            .get('/grants')
            .expect(400, done);
        });
      });
    });

    describe('with conflicting versions, regardless of availability', () => {
      it('Returns a 409 Conflict', (done) => {
        request(app)
          .get('/v1/grants')
          .set('Accept', 'application/vnd.api+json; gov.usda.fs.nrm.ga.api.version=2')
          .expect(409, done);
      });
    });

    describe('with an unavailable version', () => {
      describe('using a header', () => {
        it('Returns a 404 Not Found', (done) => {
          request(app)
            .get('/grants')
            .set('Accept', 'application/vnd.api+json; gov.usda.fs.nrm.ga.api.version=999')
            .expect(404, done);
        });
      });
      describe('using a path', () => {
        it('Returns a 404 Not Found', (done) => {
          request(app)
            .get('/v999/grants')
            .set('Accept', 'application/vnd.api+json')
            .expect(404, done);
        });
      });
    });

    describe('with a single available version', () => {
      describe('using a header', () => {
        it('Returns a 200 OK', (done) => {
          request(app)
            .get('/grants')
            .set('Accept', 'application/vnd.api+json; gov.usda.fs.nrm.ga.api.version=1')
            .expect(200, done);
        });
      });

      describe('using a path', () => {
        it('Returns a 200 OK', (done) => {
          request(app)
            .get('/v1/grants')
            .set('Accept', 'application/vnd.api+json')
            .expect(200, done);
        });
      });

      describe('using a header and a path', () => {
        it('Returns a 200 OK', (done) => {
          request(app)
            .get('/v1/grants')
            .set('Accept', 'application/vnd.api+json; gov.usda.fs.nrm.ga.api.version=1')
            .expect(200, done);
        });
      });

      describe('without JSON:API Content-Type, but otherwise valid', () => {
        it('Returns a 200 OK', (done) => {
          request(app)
            .get('/v1/grants')
            .expect(200, done);
        });
      });
    });

  }); // API Version Routing
}); // Server
