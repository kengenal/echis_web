import os
import pytest

from echis_web.utils.weather import Weather, LocalizationManager
from tests.base_test_case import BaseTokenSetup
from tests.utils.test_weather import MockWeatherData, MockRequests


def mock_weather(*args, **kwargs):
    return MockWeatherData.json()


def mock_localization(*args, **kwargs):
    return MockRequests.json()


def mock_bad_requests(*args, **kwargs):
    return {}


class TestApiWeatherController(BaseTokenSetup):
    @pytest.fixture(autouse=True)
    def environ(self):
        os.environ["OPEN_WEATHER_TOKEN"] = "123"

    def test_get_with_country_location(self, monkeypatch):
        monkeypatch.setattr(Weather, "_request", mock_weather)
        rq = self.client.get("/api/weather/warsaw", headers=self.auth_header)

        assert rq.status_code == 200
        assert b'clouds' in rq.data

    def test_get_without_specify_city_name_should_be_return_200_and_data(self, monkeypatch):
        monkeypatch.setattr(Weather, "_request", mock_weather)
        monkeypatch.setattr(LocalizationManager, "_request", mock_weather)
        rq = self.client.get("/api/weather", headers=self.auth_header)

        assert rq.status_code == 200
        assert b'clouds' in rq.data

    def test_get_with_empty_list_should_be_return_400_with_error(self, monkeypatch):
        monkeypatch.setattr(Weather, "_request", mock_bad_requests)
        rq = self.client.get("/api/weather/warsaw", headers=self.auth_header)

        assert rq.status_code == 400
        assert b'{\n  "Error": "City not exists"\n}\n' in rq.data

    def test_get_empty_localization_should_be_return_400_with_error(self, monkeypatch):
        monkeypatch.setattr(Weather, "_request", mock_bad_requests)
        monkeypatch.setattr(LocalizationManager, "_request", mock_bad_requests)
        rq = self.client.get("/api/weather", headers=self.auth_header)

        assert rq.status_code == 400
        assert b'{\n  "Error": "City not exists"\n}\n' in rq.data
