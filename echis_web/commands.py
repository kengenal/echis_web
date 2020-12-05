import os

import click
from flask import current_app

from echis_web.settings import DevConfig, ProdConfig
from echis_web.utils.token import create_token


@click.command("login")
def login_command():
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
    click.echo(token)
