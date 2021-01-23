#! ../env/bin/python
# -*- coding: utf-8 -*-
import os

import click
from flask import Flask, render_template, jsonify
from flask_mongoengine import MongoEngineSessionInterface

from echis_web.controllers.api.api_auth_controller import ApiAuthController
from echis_web.controllers.auth_controller import auth
from echis_web.controllers.home_controller import home
from echis_web.controllers.share_controller import share
from echis_web.exception.exceptions import ForbiddenException, UnauthorizedException, BadRequestException
from echis_web.extensions import me
from echis_web.settings import ProdConfig, DevConfig
from echis_web.utils.token import create_token


def create_app():
    app = Flask(__name__, static_url_path="/webstatic")
    env = os.getenv("FLASK_ENV", default="develop")
    object_name = "echis_web.settings.DevConfig"
    if env == "production":
        object_name = "echis_web.settings.ProdConfig"
    elif env == "test":
        object_name = "echis_web.settings.TestConfig"

    app.config.from_object(object_name)

    load_extensions(app)
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, page_not_found)

    app.session_interface = MongoEngineSessionInterface(me)
    app.register_blueprint(auth)
    app.register_blueprint(home)
    app.register_blueprint(share)
    route(app)
    register_exceptions(app)
    load_commands(app)

    return app


def register_exceptions(app):
    app.register_error_handler(UnauthorizedException, handle_invalid_usage)
    app.register_error_handler(ForbiddenException, handle_invalid_usage)
    app.register_error_handler(BadRequestException, handle_invalid_usage)


def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


def load_extensions(app):
    me.init_app(app)


def page_not_found(e):
    return render_template('404.html'), 404


def load_commands(app):
    app.cli.add_command(login_command)


def route(app):
    app.add_url_rule("/api/auth", view_func=ApiAuthController.as_view("auth"))


@click.command("login")
def login_command():
    """ create token to login with dami data """
    if os.getenv("FLASK_ENV") == "prod":
        config = ProdConfig()
    else:
        config = DevConfig()
    prepare_data = {
        "permissions": "ADMIN|USER",
        "username": "TestName",
        "discord_id": 13456,
        "avatar": "https://cdn.discordapp.com/widget-avatars/EK8101DeRW0t0Jeze4L3YapbumoaRLCDWs5bV9Ntqf0"
                  "/O7VJsYBxprw5iDc2BUlaItDtc-whuW9HwNy8Jm9qH-eal5gw3LhlSfTeOOqcpH0_JJSCgLWwyP9v-Nei_8kvTW"
                  "-bohSs7JnQyfoUI_-q7osntUmM2H4LsFUPHOma1TCW2VNZqoG0x8xhmA",
    }
    token = create_token(data=prepare_data, options={
        "TOKEN_SECRET": config.TOKEN_SECRET,
        "TOKEN_ALGORITHM": config.TOKEN_ALGORITHM
    })
    click.echo(f"http://discord.docker.localhost:5000/api/auth/{token}")
