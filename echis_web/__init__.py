#! ../env/bin/python
# -*- coding: utf-8 -*-
import os
from pathlib import Path
from flask import Flask, jsonify

from echis_web.exception.exceptions import (
    ForbiddenException,
    UnauthorizedException,
    BadRequestException,
    NotFoundException, InternalServerException
)
from echis_web.extensions import me
from echis_web.routes import route
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
    from echis_web.commands import import_words_from_csv_command

    app.cli.add_command(import_words_from_csv_command)
