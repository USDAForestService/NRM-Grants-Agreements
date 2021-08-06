import { TestBed } from '@angular/core/testing';
import { GrantService } from './grant.service';

describe('GrantService', () => {
  let service: GrantService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GrantService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
