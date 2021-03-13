import { ShareModule } from './share/share.module';
import { NavbarModule } from './components/navbar/navbar.module';
import { HomeModule } from './home/home.module';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NotFoundComponent } from './not-found/not-found.component';

@NgModule({
  declarations: [AppComponent, NotFoundComponent],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HomeModule,
    NavbarModule,
    ShareModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
