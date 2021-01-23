from uuid import uuid4

import pytest

from echis_web.exception.exceptions import UnauthorizedException
from echis_web.model.user_model import User


class TestUser:
    def test_get_user_or_rise_404_correct_public_id_should_be_return_user_object(self, client, user):
        u = User.get_user_or_rise_exception(public_id=user.public_id)

        assert isinstance(u, User)
        assert u.username == user.username

    def test_if_user_not_exists_should_be_raise_exception(self, client, user):
        with pytest.raises(UnauthorizedException) as err:
            User.get_user_or_rise_exception(public_id=uuid4())

            assert err.status_code == 401


class TestUserPerms:
    @pytest.mark.parametrize("perm, expect", [
        ["admin", True],
        ["ramdom", False],
    ])
    def test_user_has_permission_user_has_perm_should_be_return_true(self, client, user, perm, expect):
        assert user.has_perm(perm) == expect
