import os

import pytest

from echis_web import create_app
from tests.fatories import PlaylistsFactory, SongsFactory, UserFactory


@pytest.fixture()
def client():
    os.environ["FLASK_ENV"] = "test"
    app = create_app()
    client = app.test_client()

    return client


@pytest.fixture()
def user():
    return UserFactory()


@pytest.fixture()
def playlists():
    return PlaylistsFactory()


@pytest.fixture()
def songs():
    return SongsFactory()
