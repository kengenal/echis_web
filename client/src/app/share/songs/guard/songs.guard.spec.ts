import { TestBed } from '@angular/core/testing';

import { SongsGuard } from './songs.guard';

describe('SongsGuard', () => {
  let guard: SongsGuard;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    guard = TestBed.inject(SongsGuard);
  });

  it('should be created', () => {
    expect(guard).toBeTruthy();
  });
});
