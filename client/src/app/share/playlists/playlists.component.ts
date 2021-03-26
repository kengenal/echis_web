import { HttpClient } from '@angular/common/http';
import { ChangeDetectionStrategy, ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { environment } from 'src/environments/environment';
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
  displayModal = false;
  createdForm: Record<string, string | boolean> = {
    api: '',
    playlist_id: '',
    is_active: false,
  };

  constructor(private route: ActivatedRoute, private router: Router, private resolver: PlaylistsResolver, private cd: ChangeDetectorRef, private http: HttpClient) {}

  ngOnInit(): void {
    this.playlistData = this.route.snapshot.data as ResponsePlaylistData;
    this.cd.detectChanges();
  }

  isNumber(timestamp: number | string): boolean {
    return typeof timestamp === 'number';
  }

  showDialog() {
    this.displayModal = true;
  }

  updateData(target: any) {
    const name = target.name as string;
    const value = target.value as string | boolean;

    this.createdForm[name] = value;
  }

  onSubmit(e: Event) {
    e.preventDefault();
    const token = localStorage.getItem(environment.USER_TOKEN_NAME);

    this.http
      .post(
        `${environment.API_URL}/share/playlist`,
        {
          ...this.createdForm,
        },
        {
          headers: {
            Authorization: `Bearer ${token}`,
            accept: 'application/json',
          },
        }
      )
      .subscribe((response: any) => {
        this.playlistData.playlists.push(JSON.parse(response));
        this.displayModal = false;
        this.cd.detectChanges();
      });
  }

  deleteItem(playlistID: string) {
    const token = localStorage.getItem(environment.USER_TOKEN_NAME);

    this.http
      .delete(`${environment.API_URL}/share/playlist/${playlistID}`, {
        headers: {
          Authorization: `Bearer ${token}`,
          accept: 'application/json',
        },
      })
      .subscribe(() => {
        this.resolver.resolve(this.route.snapshot).subscribe(() =>
          setTimeout(() => {
            this.playlistData = this.route.snapshot.data as ResponsePlaylistData;
            this.cd.detectChanges();
          }, 100)
        );
      });
  }

  onPage({ first }: { first: number }): void {
    const page = first / 10 + 1;
    this.router.navigateByUrl(`/share/songs/${page}`);
    this.resolver.resolve(this.route.snapshot).subscribe(() => setTimeout(() => (this.playlistData = this.route.snapshot.data as ResponsePlaylistData), 100));
  }
}
