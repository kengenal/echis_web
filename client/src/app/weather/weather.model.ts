export interface WeatherData {
  clouds: {
    all: number;
  };
  cod: number;
  dt: number;
  id: number;
  main: {
    feels_like: number;
    humidity: number;
    pressure: number;
    temp: number;
    temp_max: number;
    temp_min: number;
  };
  name: string;
  rain: {
    '1h': number;
  };
  sys: {
    country: string;
    id: number;
    sunrise: number;
    sunset: number;
    type: number;
  };
  timezone: number;
  visibility: number;
  weather: [
    {
      description: string;
      icon: string;
      id: number;
      main: string;
    }
  ];
  wind: {
    deg: number;
    speed: number;
  };
}
