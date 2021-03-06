import { TestBed } from '@angular/core/testing';

import { PlaylistsGuard } from './playlists.guard';

describe('PlaylistsGuard', () => {
  let guard: PlaylistsGuard;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    guard = TestBed.inject(PlaylistsGuard);
  });

  it('should be created', () => {
    expect(guard).toBeTruthy();
  });
});
