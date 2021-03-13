import { SongsResolver } from './guard/songs.resolver';
import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import ResponseSongsData from './songs.model';

@Component({
  selector: 'app-songs',
  templateUrl: './songs.component.html',
  styleUrls: ['./songs.component.scss'],
})
export class SongsComponent implements OnInit {
  songstData: ResponseSongsData;

  constructor(private route: ActivatedRoute, private router: Router, private resolver: SongsResolver, private cd: ChangeDetectorRef) {}

  ngOnInit(): void {
    this.songstData = this.route.snapshot.data as ResponseSongsData;
    this.cd.detectChanges();
  }

  isNumber(timestamp: number | string): boolean {
    return typeof timestamp === 'number';
  }

  onPage({ first }: { first: number }): void {
    const page = first / 10 + 1;
    this.router.navigateByUrl(`/share/songs/${page}`);
    this.resolver.resolve(this.route.snapshot).subscribe(() => setTimeout(() => (this.songstData = this.route.snapshot.data as ResponseSongsData), 100));
  }
}
