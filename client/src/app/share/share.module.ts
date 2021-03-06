import { ShareRoutingModule } from './share-routing.module';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SongsComponent } from './songs/songs.component';
import { PlaylistsComponent } from './playlists/playlists.component';
import { TableModule } from 'primeng/table';

@NgModule({
  declarations: [SongsComponent, PlaylistsComponent],
  imports: [CommonModule, ShareRoutingModule, TableModule],
})
export class ShareModule {}
