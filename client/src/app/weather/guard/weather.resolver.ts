import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router, Resolve, ActivatedRouteSnapshot } from '@angular/router';
import { Observable, of } from 'rxjs';
import { map, catchError } from 'rxjs/operators';
import { environment } from 'src/environments/environment';
import { WeatherData } from '../weather.model';

@Injectable({
  providedIn: 'root',
})
export class WeatherResolver implements Resolve<boolean> {
  constructor(private http: HttpClient, private router: Router) {}

  resolve(route: ActivatedRouteSnapshot): Observable<boolean> {
    const token = localStorage.getItem(environment.USER_TOKEN_NAME);
    const city = route.params.city ?? 'warszawa';

    return this.http
      .get<WeatherData>(`${environment.API_URL}/weather/${city}`, {
        headers: {
          Authorization: `Bearer ${token}`,
          accept: 'application/json',
        },
      })
      .pipe(
        map((response) => {
          route.data = response;
          return true;
        }),
        catchError(() => {
          return of(false);
        })
      );
  }
}
