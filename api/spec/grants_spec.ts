import request from 'supertest';

import { app } from '../src/app'

function hasDataKey(response) {
  if (!('data' in response.body)) throw new Error("missing 'data' key");
}

describe('/grants', () => {
  describe('conforms to JSON:API', () => {
    describe('get', () => {
      it('has a root "data" key', (done) => {
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
