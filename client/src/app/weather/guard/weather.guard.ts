import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot } from '@angular/router';
import { Observable } from 'rxjs';

import { map } from 'rxjs/operators';
import { WeatherResolver } from './weather.resolver';

@Injectable({
  providedIn: 'root',
})
export class WeatherGuard implements CanActivate {
  constructor(private resolver: WeatherResolver) {}

  canActivate(route: ActivatedRouteSnapshot): Observable<boolean> {
    return this.resolver.resolve(route).pipe(map((resolve) => resolve));
  }
}
