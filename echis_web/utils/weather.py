from dataclasses import dataclass

import requests


@dataclass
class Endpoints:
    ip: str = "http://ip-api.com/json/{}"
    weather: str = "https://api.openweathermap.org/data/2.5/weather?appid={}&units" \
                   "=metric&q={}"


@dataclass
class Localization:
    city: str
    country: str


class LocalizationManager:
    def __init__(self, addr):
        """
        :param addr:
        """
        self.addr = addr
        self.data = None

    def get_localization(self):
        data = self._request()
        self.data = Localization(city=data.get("city"), country=data.get("country"))

    def _request(self):
        url = Endpoints.ip.format(self.addr)
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        return {}


class Weather:
    def __init__(self, token, locale):
        """

        :param token: string
        :param locale: Localization
        """
        self.token = token
        self.locale = locale
        self.data = {}

    def get_current(self):
        data = self._request()
        data.pop("coord") if "coord" in data else None
        data.pop("base") if "base" in data else None
        self.data = data

    def _request(self):
        url = Endpoints.weather.format(self.token, self.locale.city)
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        return {}
