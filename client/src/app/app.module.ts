import { ShareModule } from './share/share.module';
import { NavbarModule } from './components/navbar/navbar.module';
import { HomeModule } from './home/home.module';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NotFoundComponent } from './not-found/not-found.component';

@NgModule({
  declarations: [AppComponent, NotFoundComponent],
  imports: [BrowserAnimationsModule, AppRoutingModule, HomeModule, NavbarModule, ShareModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
