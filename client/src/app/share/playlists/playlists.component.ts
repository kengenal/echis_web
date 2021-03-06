import { ChangeDetectionStrategy, ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { PlaylistsResolver } from './guard/playlists.resolver';
import ResponsePlaylistData from './playlists.model';

@Component({
  selector: 'app-playlists',
  templateUrl: './playlists.component.html',
  styleUrls: ['./playlists.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class PlaylistsComponent implements OnInit {
  playlistData: ResponsePlaylistData;

  constructor(private route: ActivatedRoute, private router: Router, private resolver: PlaylistsResolver, private cd: ChangeDetectorRef) {}

  ngOnInit(): void {
    this.playlistData = this.route.snapshot.data as ResponsePlaylistData;
    this.cd.detectChanges();
  }

  isNumber(timestamp: number | string): boolean {
    return typeof timestamp === 'number';
  }

  onPage({ first }: { first: number }): void {
    const page = first / 10 + 1;
    this.router.navigateByUrl(`/share/songs/${page}`);
    this.resolver.resolve(this.route.snapshot).subscribe(() => setTimeout(() => (this.playlistData = this.route.snapshot.data as ResponsePlaylistData), 100));
  }
}
