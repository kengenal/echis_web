from dataclasses import dataclass

import requests


@dataclass
class Endpoints:
    ip: str = "http://ip-api.com/json/{}"


@dataclass
class Localization:
    city: str
    country: str


class LocalizationManager:
    def __init__(self, addr):
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
