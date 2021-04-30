from unittest.mock import patch
from uuid import uuid4

import pytest

from echis_web.exception.exceptions import ForbiddenException
from echis_web.utils import decorators
from echis_web.utils.decorators import (
    has_perm_api
)
from echis_web.utils.token import create_token
from tests.base_test_case import BaseTokenSetup

SESSION_PATH = "echis_web.utils.decorators.session"
REQUEST_PATH = "echis_web.utils.decorators.request"
G_OBJECT_PATH = "echis_web.utils.decorators.g"


class FakeRequest:
    headers = {}
    method = "POST"


class GObject:
    user = None


# TEST LOGIN REQUIRED
def mock_abort(*args, **kwargs):
    return 404


def mock_redirect(*args, **kwargs):
    return 302


@pytest.fixture
def abort(monkeypatch):
    monkeypatch.setattr(decorators, "get_404", mock_abort)
    monkeypatch.setattr(decorators, "get_redirect", mock_redirect)


class TestLoginRequired(BaseTokenSetup):
    def test_api_user_is_authorized_should_be_return_200(self):
        rq = self.client.get("/api/share/playlist", headers=self.auth_header)

        assert rq.status_code != 401

    def test_api_user_is_unauthorized_without_headers_should_be_return_401(self):
        rq = self.client.get("/api/share/playlist", headers={})

        assert rq.status_code == 401

    def test_api_user_not_exist_should_be_return_401(self):
        token = create_token({"public_id": str(uuid4())}, options={
            "SECRET_KEY": self.config.SECRET_KEY,
            "TOKEN_ALGORITHM": self.config.TOKEN_ALGORITHM
        })
        auth_header = {"Authorization": f"Bearer {token}"}
        rq = self.client.get("/api/share/playlist", headers=auth_header)

        assert rq.status_code == 401


# TEST HAS PERMISSIONS

class TestHasPermissionApi:
    def test_user_has_permission(self, client, user):
        with patch(G_OBJECT_PATH, GObject) as g:
            with patch(REQUEST_PATH, FakeRequest):
                @has_perm_api(["admin"], methods=["POST"])
                def t():
                    return 1

                g.user = user
                dec = t()

                assert dec == 1

    def test_user_has_permission_without_set_http_method(self, client, user):
        with patch(G_OBJECT_PATH, GObject) as g:
            with patch(REQUEST_PATH, FakeRequest):
                @has_perm_api(["admin"])
                def t():
                    return 1

                g.user = user
                dec = t()

                assert dec == 1

    def test_user_dont_have_permission_should_be_raise_exception(self, client, user):
        with pytest.raises(ForbiddenException) as err:
            with patch(G_OBJECT_PATH, GObject) as g:
                with patch(REQUEST_PATH, FakeRequest):
                    @has_perm_api(["random_permission"], methods=["POST"])
                    def t():
                        return 1

                    g.user = user
                    t()
                    assert err.status_code == 403
