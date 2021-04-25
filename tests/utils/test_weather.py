import requests

from echis_web.utils.weather import LocalizationManager


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
