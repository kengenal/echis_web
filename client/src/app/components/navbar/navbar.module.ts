import { NavbarComponent } from './navbar.component';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MenubarModule } from 'primeng/menubar';
import { ButtonModule } from 'primeng/button';
import { SharedModule } from 'primeng/api';

@NgModule({
  declarations: [NavbarComponent],
  imports: [CommonModule, SharedModule, MenubarModule, ButtonModule],
  exports: [NavbarComponent],
})
export class NavbarModule {}
