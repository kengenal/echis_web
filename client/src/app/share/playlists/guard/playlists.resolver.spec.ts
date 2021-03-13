import { TestBed } from '@angular/core/testing';

import { PlaylistsResolver } from './playlists.resolver';

describe('PlaylistsResolver', () => {
  let resolver: PlaylistsResolver;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    resolver = TestBed.inject(PlaylistsResolver);
  });

  it('should be created', () => {
    expect(resolver).toBeTruthy();
  });
});
