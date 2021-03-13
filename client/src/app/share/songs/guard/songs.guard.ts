import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';
import { Observable } from 'rxjs';

import { map } from 'rxjs/operators';
import { SongsResolver } from './songs.resolver';
@Injectable({
  providedIn: 'root',
})
export class SongsGuard implements CanActivate {
  constructor(private resolver: SongsResolver) {}

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<boolean> {
    return this.resolver.resolve(route).pipe(map((resolve) => resolve));
  }
}
