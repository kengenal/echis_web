import { SongsResolver } from './guard/songs.resolver';
import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import ResponseSongsData from './songs.model';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-songs',
  templateUrl: './songs.component.html',
  styleUrls: ['./songs.component.scss'],
})
export class SongsComponent implements OnInit {
  songstData: ResponseSongsData;

  constructor(private route: ActivatedRoute, private router: Router, private resolver: SongsResolver, private cd: ChangeDetectorRef, private http: HttpClient) {}

  ngOnInit(): void {
    this.songstData = this.route.snapshot.data as ResponseSongsData;
    this.cd.detectChanges();
  }

  isNumber(timestamp: number | string): boolean {
    return typeof timestamp === 'number';
  }

  deleteItem(recordID: string): void {
    const token = localStorage.getItem(environment.USER_TOKEN_NAME);

    this.http
      .delete(`${environment.API_URL}/share/songs/${recordID}`, {
        headers: {
          Authorization: `Bearer ${token}`,
          accept: 'application/json',
        },
      })
      .subscribe(() => {
        this.resolver.resolve(this.route.snapshot).subscribe(() =>
          setTimeout(() => {
            this.songstData = this.route.snapshot.data as ResponseSongsData;
            this.cd.detectChanges();
          }, 100)
        );
      });
  }

  onPage({ first }: { first: number }): void {
    const page = first / 10 + 1;
    this.router.navigateByUrl(`/share/songs/${page}`);
    this.resolver.resolve(this.route.snapshot).subscribe(() => setTimeout(() => (this.songstData = this.route.snapshot.data as ResponseSongsData), 100));
  }
}
