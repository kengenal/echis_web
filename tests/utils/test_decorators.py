from unittest.mock import patch

from echis_web.utils import decorators
from echis_web.utils.decorators import login_required, has_perms, unauthorized
import pytest

SESSION_PATH = "echis_web.utils.decorators.session"


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
        with patch(SESSION_PATH, dict()) as session:
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

class TestUnauthorized:
    def test_user_is_authorized_should_be_return_404(self, abort):
        with patch(SESSION_PATH, dict()) as session:
            session["user"] = {}

            dec = unauthorized(lambda x: x)(1)

            assert dec == 404

    def test_user_not_authorized_should_be_return_function_body(self):
        with patch(SESSION_PATH, dict()) as session:
            dec = unauthorized(lambda x: x)(1)

            assert dec == 1
