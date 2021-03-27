import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeGuard } from './guard/home.guard';
import { HomeComponent } from './home.component';

const routes: Routes = [
  {
    path: ':id',
    component: HomeComponent,
    canActivate: [HomeGuard],
  },
  {
    path: '',
    component: HomeComponent,
    canActivate: [HomeGuard],
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class HomeRoutingModule {}
