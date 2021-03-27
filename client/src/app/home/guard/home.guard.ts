import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, UrlTree, Router } from '@angular/router';
import { Observable, of, Subscription } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import ResponseUserData from '../home.model';
import { catchError, map } from 'rxjs/operators';
@Injectable({
  providedIn: 'root',
})
export class HomeGuard implements CanActivate {
  constructor(private http: HttpClient, private router: Router) {}

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<boolean> {
    const { id } = route.params;

    if (!id) {
      this.router.navigate(['/404']);
      return of(false);
    }

    return this.http
      .get<ResponseUserData>(`${environment.API_URL}/auth`, {
        headers: {
          Authorization: `Bearer ${id}`,
          accept: 'application/json',
        },
      })
      .pipe(
        map((response) => {
          localStorage.setItem(environment.USER_TOKEN_NAME, response?.token ?? '');
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
