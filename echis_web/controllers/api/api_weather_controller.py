import os

from echis_web.utils.decorators import has_perm_api, login_required_api
from flask import jsonify, request
from flask.views import MethodView

from echis_web.utils.weather import LocalizationManager, Localization, Weather


class ApiWeatherController(MethodView):
    has_perm_for_methods = ["POST", "PUT", "DELETE"]
    decorators = [has_perm_api(permissions=["ADMIN"], methods=has_perm_for_methods), login_required_api]

    def __init__(self):
        self.city = None
        self.weather = None

    def get(self, city=None):
        """
        file: docs/playlists/get_playlists_items.yaml
        """
        self.city = Localization(city=city, country="")
        token = os.getenv("OPEN_WEATHER_TOKEN")
        if not token:
            return jsonify({"Error": "api is unavailable"}), 404
        if not self.city:
            self._set_city()
        self._get_weather(token)
        if not self.weather:
            return jsonify({"Error": "City not exists"}), 400
        return jsonify(self.weather), 200

    def _set_city(self):
        locale = LocalizationManager(request.environ.get('HTTP_X_REAL_IP', request.remote_addr) )
        locale.get_localization()

        self.city = locale.data.city

    def _get_weather(self, token):
        weather = Weather(token, self.city)
        weather.get_current()

        self.weather = weather.data
