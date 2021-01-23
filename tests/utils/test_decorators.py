from unittest.mock import patch
from uuid import uuid4

import pytest

from echis_web.exception.exceptions import UnauthorizedException, ForbiddenException
from echis_web.utils import decorators
from echis_web.utils.decorators import (
    login_required,
    has_perms,
    unauthorized,
    login_required_api,
    has_perm_api
)
from echis_web.utils.token import create_token

SESSION_PATH = "echis_web.utils.decorators.session"
REQUEST_PATH = "echis_web.utils.decorators.request"
G_OBJECT_PATH = "echis_web.utils.decorators.g"


# TEST LOGIN REQUIRED
def mock_abort(*args, **kwargs):
    return 404


def mock_redirect(*args, **kwargs):
    return 302


@pytest.fixture
def abort(monkeypatch):
    monkeypatch.setattr(decorators, "get_404", mock_abort)
    monkeypatch.setattr(decorators, "get_redirect", mock_redirect)


class TestLoginRequired:
    def test_login_required_should_be_return_404(self, abort):
        with patch(SESSION_PATH, dict()):
            dec = login_required(lambda x: x)(1)

            assert dec == 404

    def test_login_required_should_be_return_func(self):
        with patch(SESSION_PATH, dict()) as session:
            session["user"] = "test"
            dec = login_required(lambda x: x)(1)

            assert dec == 1


# TEST HAS PERMISSIONS

@has_perms("ADMIN")
def decor():
    return 1


@has_perms("ADMIN", rd="/test")
def decor_with_redirect():
    return 1


class TestHasPerms:
    def test_user_dont_have_permission_to_see_func_should_be_return_1(self, abort):
        with patch(SESSION_PATH, dict()) as session:
            session["user"] = {"permissions": "ADMIN|USER"}
            dec = decor()

            assert dec == 1

    def test_user_dont_have_permissions_to_see_func_should_be_return_404(self, abort):
        with patch(SESSION_PATH, dict()) as session:
            session["user"] = {"permissions": "USER"}
            dec = decor()

            assert dec == 404

    def test_empty_session(self, abort):
        with patch(SESSION_PATH, dict()):
            dec = decor()

            assert dec == 404

    def test_with_redirect_parameter(self, abort):
        with patch(SESSION_PATH, dict()) as session:
            session["user"] = {"permissions": "USER"}
            dec = decor_with_redirect()

            assert dec == 302


# Test Unauthorized

class FakeRequest:
    headers = {}


class TestUnauthorized:
    def test_user_is_authorized_should_be_return_404(self, abort):
        with patch(SESSION_PATH, dict()) as session:
            session["user"] = {}

            dec = unauthorized(lambda x: x)(1)

            assert dec == 404

    def test_user_not_authorized_should_be_return_function_body(self):
        with patch(SESSION_PATH, dict()):
            dec = unauthorized(lambda x: x)(1)

            assert dec == 1

    def test_api_user_is_authorized_should_be_return_200(self, client, user):
        token = create_token({"public_id": str(user.public_id)})
        with patch(REQUEST_PATH, FakeRequest) as r:
            with patch(G_OBJECT_PATH, dict()):
                r.headers["Authorization"] = f"Barer {token}"
                dec = login_required_api(lambda x: x)(1)
                assert dec == 1

    def test_api_user_is_unauthorized_should_be_return_401(self):
        with patch(REQUEST_PATH, FakeRequest) as r:
            with patch(G_OBJECT_PATH, dict()):
                with pytest.raises(UnauthorizedException) as err:
                    r.headers["Authorization"] = "test"
                    login_required_api(lambda x: x)(1)
                    assert err.status_code == 401

    def test_api_user_not_exist_should_be_return_401(self, client, user):
        token = create_token({"public_id": str(uuid4())})
        with patch(REQUEST_PATH, FakeRequest) as r:
            with patch(G_OBJECT_PATH, dict()):
                with pytest.raises(UnauthorizedException) as err:
                    r.headers["Authorization"] = f"Barer {token}"
                    login_required_api(lambda x: x)(1)
                    assert err.status_code == 401


class TestHasPermission:
    def test_user_has_permission(self, client, user):
        with patch(G_OBJECT_PATH, dict()) as g:
            @has_perm_api(["admin"])
            def t():
                return 1

            g["user"] = user

            dec = t()
            assert dec == 1

    def test_user_dont_have_permission_should_be_raise_exception(self, client, user):
        with pytest.raises(ForbiddenException) as err:
            with patch(G_OBJECT_PATH, dict()) as g:
                @has_perm_api(["random_permission"])
                def t():
                    return 1

                g["user"] = user
                t()
                assert err.status_code == 403
