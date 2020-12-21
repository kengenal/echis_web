import pytest

from echis_web import create_app
from tests.fatories import PlaylistsFactory, SongsFactory


@pytest.fixture()
def client():
    app = create_app("test")
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
