import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router, Resolve, RouterStateSnapshot, ActivatedRouteSnapshot } from '@angular/router';
import { Observable, of } from 'rxjs';
import { map, catchError } from 'rxjs/operators';
import { environment } from 'src/environments/environment';
import ResponseSongsData from '../songs.model';

@Injectable({
  providedIn: 'root',
})
export class SongsResolver implements Resolve<boolean> {
  constructor(private http: HttpClient, private router: Router) {}

  resolve(route: ActivatedRouteSnapshot): Observable<boolean> {
    const token = localStorage.getItem(environment.USER_TOKEN_NAME);
    const page = route.params.page;

    return this.http
      .get<ResponseSongsData>(`${environment.API_URL}/share/songs/${page}`, {
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
          this.router.navigate(['/404']);
          return of(false);
        })
      );
  }
}
