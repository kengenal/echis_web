import { TestBed } from '@angular/core/testing';

import { SongsResolver } from './songs.resolver';

describe('SongsResolver', () => {
  let resolver: SongsResolver;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    resolver = TestBed.inject(SongsResolver);
  });

  it('should be created', () => {
    expect(resolver).toBeTruthy();
  });
});
