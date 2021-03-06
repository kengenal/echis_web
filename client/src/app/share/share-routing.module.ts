import { PlaylistsGuard } from './playlists/guard/playlists.guard';
import { PlaylistsComponent } from './playlists/playlists.component';
import { SongsComponent } from './songs/songs.component';

import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SongsGuard } from './songs/guard/songs.guard';

const routes: Routes = [
  {
    path: 'playlists/:page',
    component: PlaylistsComponent,
    canActivate: [PlaylistsGuard],
  },
  {
    path: 'songs/:page',
    component: SongsComponent,
    canActivate: [SongsGuard],
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class ShareRoutingModule {}
