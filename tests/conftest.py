import os
from unittest.mock import patch

import pytest
from flask import g

from echis_web import create_app
from echis_web.utils.token import create_token
from tests.fatories import PlaylistsFactory, SongsFactory, UserFactory


@pytest.fixture()
def client():
    os.environ["FLASK_ENV"] = "test"
    app = create_app()
    client = app.test_client()

    return client


@pytest.fixture()
def login(client):
    with client as c:
        with c.session_transaction() as sess:
            sess['user'] = {
                "permissions": "ADMIN|USER",
                "username": "TestName",
                "discord_id": 13456,
                "avatar": "https://cdn.discordapp.com/widget-avatars/EK8101DeRW0t0Jeze4L3YapbumoaRLCDWs5bV9Ntqf0"
                          "/O7VJsYBxprw5iDc2BUlaItDtc-whuW9HwNy8Jm9qH-eal5gw3LhlSfTeOOqcpH0_JJSCgLWwyP9v-Nei_8kvTW"
                          "-bohSs7JnQyfoUI_-q7osntUmM2H4LsFUPHOma1TCW2VNZqoG0x8xhmA",
            }


@pytest.fixture
def token():
    prepare_data = {
        "permissions": "ADMIN|USER",
        "username": "TestName",
        "discord_id": 13456712312323123,
        "avatar": "https://cdn.discordapp.com/widget-avatars/EK8101DeRW0t0Jeze4L3YapbumoaRLCDWs5bV9Ntqf0"
                  "/O7VJsYBxprw5iDc2BUlaItDtc-whuW9HwNy8Jm9qH-eal5gw3LhlSfTeOOqcpH0_JJSCgLWwyP9v-Nei_8kvTW"
                  "-bohSs7JnQyfoUI_-q7osntUmM2H4LsFUPHOma1TCW2VNZqoG0x8xhmA",
    }
    token = create_token(data=prepare_data)
    return token


@pytest.fixture
def token_invalid_payload():
    prepare_data = {
        "permissions": "ADMIN|USER",
        "username": "TestName",
    }
    token = create_token(data=prepare_data)
    return token


@pytest.fixture()
def api_login(client, user):
    def mock(*args, **kwargs):
        g.user = user

    patch("echis_web.utils.decorator.login_required", mock).start()


@pytest.fixture()
def empty_session(client):
    with client as c:
        with c.session_transaction() as sess:
            sess["u"] = {}


@pytest.fixture()
def playlists():
    return PlaylistsFactory()


@pytest.fixture()
def songs():
    return SongsFactory()


@pytest.fixture()
def user():
    return UserFactory()
