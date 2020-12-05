import pytest
from mongoengine import connect

from echis_web import create_app


@pytest.fixture()
def client():
    app = create_app("test")
    client = app.test_client()

    return client
