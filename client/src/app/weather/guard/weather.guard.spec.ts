import { TestBed } from '@angular/core/testing';

import { WeatherGuard } from './weather.guard';

describe('WeatherGuard', () => {
  let guard: WeatherGuard;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    guard = TestBed.inject(WeatherGuard);
  });

  it('should be created', () => {
    expect(guard).toBeTruthy();
  });
});
