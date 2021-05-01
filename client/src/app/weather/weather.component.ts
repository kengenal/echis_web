import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { WeatherResolver } from './guard/weather.resolver';
import { WeatherData } from './weather.model';

@Component({
  selector: 'app-weather',
  templateUrl: './weather.component.html',
  styleUrls: ['./weather.component.scss'],
})
export class WeatherComponent implements OnInit {
  weatherData: WeatherData;
  city: Event | string = '';

  constructor(private route: ActivatedRoute, private cd: ChangeDetectorRef, private router: Router, private resolver: WeatherResolver) {}

  ngOnInit(): void {
    this.weatherData = this.route.snapshot.data as WeatherData;
    this.cd.detectChanges();
  }

  onCityChange(e: Event): void {
    e.preventDefault();

    this.router.navigateByUrl(`/weather/${this.city}`);
    this.resolver.resolve(this.route.snapshot).subscribe(() => setTimeout(() => (this.weatherData = this.route.snapshot.data as WeatherData), 100));
    this.city = '';
  }
}
