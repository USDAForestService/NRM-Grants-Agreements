import request from 'supertest';

import { app } from '../src/app'

function hasDataKey(response) {
  if (!('data' in response.body)) throw new Error("missing 'data' key");
}

describe('Grants', () => {
  describe('without a version', () => {
    describe('with JSON:API Content-Type', () => {
      it('Returns a 400 Bad Request', (done) => {
        request(app)
          .get('/grants')
          .set('Accept', 'application/vnd.api+json; gov.usda.fs.nrm.ga.api.version=1')
          .expect(200)
          .expect(hasDataKey)
          .end(done);
      });
    });
  });
});
