import { WeatherComponent } from './weather.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WeatherGuard } from './guard/weather.guard';

const routes: Routes = [
  {
    path: '',
    component: WeatherComponent,
    canActivate: [WeatherGuard],
  },
  {
    path: ':city',
    component: WeatherComponent,
    canActivate: [WeatherGuard],
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class WeatherRoutingModule {}
