import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { WeatherComponent } from './weather.component';
import { WeatherRoutingModule } from './weather-routing.module';
import { InputTextModule } from 'primeng/inputtext';
import { ButtonModule } from 'primeng/button';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [WeatherComponent],
  imports: [CommonModule, WeatherRoutingModule, InputTextModule, ButtonModule, FormsModule, ReactiveFormsModule],
})
export class WeatherModule {}
