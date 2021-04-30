#! ../env/bin/python
# -*- coding: utf-8 -*-
import os
from pathlib import Path

from flask import Flask, jsonify

from echis_web.controllers.api.api_auth_controller import ApiAuthController, ApiLogoutController
from echis_web.controllers.api.api_share_controller import ApiPlaylistController, ApiSongController
from echis_web.controllers.api.api_weather_controller import ApiWeatherController
from echis_web.controllers.api.api_filter_controller import ApiFilterController
from echis_web.exception.exceptions import (
    ForbiddenException,
    UnauthorizedException,
    BadRequestException,
    NotFoundException, InternalServerException
)
from echis_web.extensions import me
from echis_web.utils.token import create_token, generate_fake_discord_token

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent


def create_app():
    env = os.getenv("FLASK_ENV", default="develop")
    object_name = "echis_web.settings.DevConfig"
    static_url = '/webstatic'
    if env == "production":
        object_name = "echis_web.settings.ProdConfig"
        static_url = '/static/'
    elif env == "test":
        object_name = "echis_web.settings.TestConfig"
    path = os.path.join(ROOT_DIR / 'client/dist/client')
    app = Flask(__name__, static_url_path=static_url, static_folder=path, template_folder=path)
    app.config.from_object(object_name)
    load_extensions(app, env)
    register_exceptions(app, path)
    route(app)

    load_commands(app)

    return app


def register_exceptions(app, path=None):
    app.register_error_handler(
        404,
        lambda x: (app.send_static_file("index.html") if os.path.exists(path=path) else jsonify(
            {"Error": "page not foud"}), 404
                   )
    )
    app.register_error_handler(InternalServerException, handle_invalid_usage)
    app.register_error_handler(UnauthorizedException, handle_invalid_usage)
    app.register_error_handler(ForbiddenException, handle_invalid_usage)
    app.register_error_handler(BadRequestException, handle_invalid_usage)
    app.register_error_handler(NotFoundException, handle_invalid_usage)


def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


def load_extensions(app, env):
    if env == "develop":
        """ extensions only for development """
        from flasgger import Swagger
        Swagger(app, template=app.config["SWAGGER_TEMPLATE"], config=app.config["SWAGGER_CONFIG"])
    me.init_app(app)


def load_commands(app):
    pass


def route(app):
    # AUTH
    app.add_url_rule("/api/auth", view_func=ApiAuthController.as_view("api_auth"))
    app.add_url_rule("/api/logout", view_func=ApiLogoutController.as_view("api_logout"))

    # PLAYLIST
    app.add_url_rule(
        "/api/share/playlist",
        view_func=ApiPlaylistController.as_view("share_playlist"),
        methods=["GET", "POST"]
    )
    app.add_url_rule(
        "/api/share/playlist/<int:page>",
        view_func=ApiPlaylistController.as_view("share_playlist_pag"),
        methods=["GET"]
    )
    app.add_url_rule(
        "/api/share/playlist/<string:playlist_id>",
        view_func=ApiPlaylistController.as_view("share_playlist_parameter"),
        methods=["PUT", "DELETE"]
    )

    # SONGS
    app.add_url_rule(
        "/api/share/songs",
        view_func=ApiSongController.as_view("share_songs"),
        methods=["GET"]
    )
    app.add_url_rule(
        "/api/share/songs/<int:page>",
        view_func=ApiSongController.as_view("share_songs_pagination"),
        methods=["GET"]
    )
    app.add_url_rule(
        "/api/share/songs/<string:record_id>",
        view_func=ApiSongController.as_view("share_songs_parameter"),
        methods=["DELETE"]
    )

    # FILTERApiPlaylistController
    app.add_url_rule("/api/filter/words", view_func=ApiFilterController.as_view("filter_module"),
                     methods=["GET", "POST"])
    app.add_url_rule("/api/filter/words/<string:word_id>", view_func=ApiFilterController.as_view("filter_module_remove"),
                     methods=["DELETE"])

    # weather
    app.add_url_rule("/api/weather", view_func=ApiWeatherController.as_view("weather"),
                     methods=["GET"])
    app.add_url_rule("/api/weather/<string:city>",
                     view_func=ApiWeatherController.as_view("weather_with_city"),
                     methods=["GET"])


