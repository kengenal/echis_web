import { ShareRoutingModule } from './share-routing.module';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SongsComponent } from './songs/songs.component';
import { PlaylistsComponent } from './playlists/playlists.component';
import { TableModule } from 'primeng/table';
import { DialogModule } from 'primeng/dialog';
import { ButtonModule } from 'primeng/button';
import { InputTextModule } from 'primeng/inputtext';
import { MultiSelectModule } from 'primeng/multiselect';
import { InputSwitchModule } from 'primeng/inputswitch';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [SongsComponent, PlaylistsComponent],
  imports: [CommonModule, ShareRoutingModule, TableModule, DialogModule, ButtonModule, InputTextModule, MultiSelectModule, InputSwitchModule, FormsModule, ReactiveFormsModule],
})
export class ShareModule {}
