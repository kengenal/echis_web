import { Component, OnInit } from '@angular/core';
import { MenuItem } from 'primeng/api';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss'],
})
export class NavbarComponent implements OnInit {
  items: MenuItem[] = [];

  constructor() {}

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
}
