import { TestBed } from '@angular/core/testing';
import { GrantService } from './grant.service';

describe('GrantService', () => {
  let service: GrantService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GrantService);
  });

  /**
   * @todo Set up a test to see what happens if there's type
   * mismatches in the data for #getGrants. For example,
   * if an applicationType value doesn't fall in the type range,
   * what happens (null, runtime error, etc.)?
   */

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
