#! ../env/bin/python
# -*- coding: utf-8 -*-

from flask import Flask

from echis_web.commands import login_command
from echis_web.controllers.auth_controller import auth
from echis_web.extensions import me


def create_app(env):
    app = Flask(__name__)
    if env == "prod":
        object_name = "echis_web.settings.ProdConfig"
    elif env == "test":
        object_name = "echis_web.settings.TestConfig"
    else:
        object_name = "echis_web.settings.DevConfig"

    app.config.from_object(object_name)

    load_extensions(app)
    app.register_blueprint(auth)
    load_commands(app)

    return app


def load_extensions(app):
    me.init_app(app)


def load_commands(app):
    app.cli.add_command(login_command)


