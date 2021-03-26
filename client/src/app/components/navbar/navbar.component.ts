import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { MenuItem } from 'primeng/api';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss'],
})
export class NavbarComponent implements OnInit {
  items: MenuItem[] = [];

  constructor(private router: Router) {}

  ngOnInit(): void {
    this.items = [
      {
        label: 'Share',
        items: [
          {
            label: 'Playlist',
            icon: 'pi pi-fw pi-plus',
            routerLink: '/share/playlists/1',
          },
          {
            label: 'Songs',
            icon: 'pi pi-fw pi-plus',
            routerLink: '/share/songs/1',
          },
        ],
      },
    ];
  }

  logout(): void {
    console.log('test');
    localStorage.removeItem(environment.USER_TOKEN_NAME);
    this.router.navigateByUrl('/404');
  }
}
