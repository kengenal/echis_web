import { PlaylistsResolver } from './playlists.resolver';
import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot } from '@angular/router';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root',
})
export class PlaylistsGuard implements CanActivate {
  constructor(private resolver: PlaylistsResolver) {}

  canActivate(route: ActivatedRouteSnapshot): Observable<boolean> {
    return this.resolver.resolve(route).pipe(map((resolve) => resolve));
  }
}
