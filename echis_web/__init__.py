#! ../env/bin/python
# -*- coding: utf-8 -*-
import os

import click
from flasgger import Swagger
from flask import Flask, render_template, jsonify
from flask_mongoengine import MongoEngineSessionInterface

from echis_web.controllers.api.api_auth_controller import ApiAuthController, ApiLogoutController
from echis_web.controllers.api.api_share_controller import ApiPlaylistController, ApiSongController
from echis_web.controllers.auth_controller import auth
from echis_web.controllers.home_controller import home
from echis_web.controllers.share_controller import share
from echis_web.exception.exceptions import (
    ForbiddenException,
    UnauthorizedException,
    BadRequestException,
    NotFoundException
)
from echis_web.extensions import me
from echis_web.utils.token import create_token, generate_fake_discord_token


def create_app():
    app = Flask(__name__, static_url_path="/webstatic")
    env = os.getenv("FLASK_ENV", default="develop")
    object_name = "echis_web.settings.DevConfig"
    if env == "production":
        object_name = "echis_web.settings.ProdConfig"
    elif env == "test":
        object_name = "echis_web.settings.TestConfig"

    app.config.from_object(object_name)
    load_extensions(app, env)

    app.session_interface = MongoEngineSessionInterface(me)
    app.register_blueprint(auth)
    app.register_blueprint(home)
    app.register_blueprint(share)
    register_exceptions(app)

    route(app)

    load_commands(app)

    return app


def register_exceptions(app):
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, page_not_found)
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
        Swagger(app, template=app.config["SWAGGER_TEMPLATE"], config=app.config["SWAGGER_CONFIG"])
    me.init_app(app)


def page_not_found(e):
    return render_template('404.html'), 404


def load_commands(app):
    app.cli.add_command(login_command)


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
        "/api/share/playlist/<playlist_id>",
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
        "/api/share/songs/<record_id>",
        view_func=ApiSongController.as_view("share_songs_parameter"),
        methods=["DELETE"]
    )


@click.command("login")
def login_command():
    """ create token to login with dami data """
    token = generate_fake_discord_token()
    click.echo(f"http://discord.docker.localhost:5000/api/auth/{token}")
