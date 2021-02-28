import { ShareRoutingModule } from './share-routing.module';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SongsComponent } from './songs/songs.component';
import { PlaylistsComponent } from './playlists/playlists.component';

@NgModule({
  declarations: [SongsComponent, PlaylistsComponent],
  imports: [CommonModule, ShareRoutingModule],
})
export class ShareModule {}
