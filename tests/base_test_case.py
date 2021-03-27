import pytest

from echis_web.settings import TestConfig
from echis_web.utils.token import create_token


class BaseTokenSetup:
    @pytest.fixture(autouse=True)
    def setup(self, client, user):
        self.client = client
        self.config = TestConfig()
        options = {
            "SECRET_KEY": self.config.SECRET_KEY,
            "TOKEN_ALGORITHM": self.config.TOKEN_ALGORITHM
        }
        payload = {
            "public_id": str(user.public_id)
        }
        self.token = create_token(data=payload, options=options)

        self.auth_header = {"Authorization": f"Bearer {self.token}"}
