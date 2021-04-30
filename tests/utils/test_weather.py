import requests

from echis_web.utils.weather import LocalizationManager, Weather, Localization


class MockRequests:
    status_code = 200

    @staticmethod
    def json():
        return {
            "status": "success", "country": "Poland", "countryCode": "PL", "region": "24", "regionName": "Test",
            "city": "Warsaw", "zip": "88-88", "lat": 25.0000, "lon": 25.0000, "timezone": "Europe/Warsaw",
            "isp": "osiem", "org": "123", "as": "123",
            "query": "127.0.0.1"
        }


def mock_locale(*args, **kwargs):
    return MockRequests()


def mock_locale_status_400(*args, **kwargs):
    cll = MockRequests()
    cll.status_code = 400
    return cll


class MockWeatherData:
    status_code = 200

    @staticmethod
    def json():
        return {
            "coord": {
                "lon": 21.0118, "lat": 52.2298
            },
            "weather": [
                {"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"}
            ],
            "base": "stations",
            "main": {
                "temp": 9.31, "feels_like": 6.67, "temp_min": 7.78, "temp_max": 11.11, "pressure": 1019,
                "humidity": 39},
            "visibility": 10000,
            "wind": {"speed": 5.14, "deg": 310},
            "clouds": {"all": 0},
            "dt": 1619354763,
            "sys": {
                "type": 1, "id": 1713, "country": "PL", "sunrise": 1619320630, "sunset": 1619373019
            },
            "timezone": 7200,
            "id": 756135,
            "name": "Warsaw",
            "cod": 200
        }


def mock_weather(*args, **kwargs):
    return MockWeatherData()


def mock_weather_status400(*args, **kwargs):
    cll = MockWeatherData()
    cll.status_code = 400
    return cll


class TestLocalizationManager:
    def test_get_by_ip_should_be_return_result(self, monkeypatch):
        monkeypatch.setattr(requests, "get", mock_locale)
        locale = LocalizationManager("127.0.0.1")
        locale.get_localization()

        assert locale.data.city == "Warsaw"
        assert locale.data.country == "Poland"

    def test_get_locale_addr_not_found_should_be_return_empty_object(self, monkeypatch):
        monkeypatch.setattr(requests, "get", mock_locale_status_400)
        locale = LocalizationManager("127.0.0.1")
        locale.get_localization()

        assert locale.data.city is None
        assert locale.data.country is None


class TestWeather:
    def test_get_with_correct_token_should_be_return_data(self, monkeypatch):
        monkeypatch.setattr(requests, "get", mock_weather)
        weather = Weather("123", Localization(city="Warsaw", country="Poland"))
        weather.get_current()

        assert "weather" in weather.data
        assert "coord" not in weather.data
        assert "base" not in weather.data

    def test_get_with_correct_token_should_be_return_empty_dict(self, monkeypatch):
        monkeypatch.setattr(requests, "get", mock_weather_status400)
        weather = Weather("123", Localization(city="Warsaw", country="Poland"))
        weather.get_current()

        assert weather.data == {}
