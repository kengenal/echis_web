import pytest

from echis_web.settings import TestConfig
from echis_web.utils.token import create_token


class TestApiAuthController:
    @pytest.fixture(autouse=True)
    def setup(self, client, user):
        self.client = client
        self.config = TestConfig()
        options = {
            "SECRET_KEY": self.config.TOKEN_SECRET,
            "TOKEN_ALGORITHM": self.config.TOKEN_ALGORITHM
        }
        prepare_data = {
            "permissions": "ADMIN|USER",
            "username": "TestName",
            "discord_id": 13456712312323123,
            "avatar": "https://cdn.discordapp.com/widget-avatars/EK8101DeRW0t0Jeze4L3YapbumoaRLCDWs5bV9Ntqf0"
                      "/O7VJsYBxprw5iDc2BUlaItDtc-whuW9HwNy8Jm9qH-eal5gw3LhlSfTeOOqcpH0_JJSCgLWwyP9v-Nei_8kvTW"
                      "-bohSs7JnQyfoUI_-q7osntUmM2H4LsFUPHOma1TCW2VNZqoG0x8xhmA",
        }
        self.token = create_token(data=prepare_data, options=options)
        prepare_data = {
            "permissions": "ADMIN|USER",
            "username": "TestName",
        }
        self.invalid_token = create_token(data=prepare_data, options=options)
        self.invalid_token_header = {"Authorization": f"Bearer {self.invalid_token}"}
        self.auth_header = {"Authorization": f"Bearer {self.token}"}

    def test_get_api_correct_token_should_be_return_jwt_token(self):
        rq = self.client.get(f"/api/auth", headers=self.auth_header)

        assert rq.status_code == 200
        assert b"token" in rq.data
        assert b"user" in rq.data

    def test_bad_payload_data_from_token_should_be_raise_400(self):
        rq = self.client.get(f"/api/auth", headers=self.invalid_token_header)

        assert rq.status_code == 400
        assert b"avatar" in rq.data
        assert b"discord_id" in rq.data

    def test_with_broken_token_should_be_raise_400(self):
        rq = self.client.get("/api/auth", headers={"Authorization": "random"})

        assert rq.status_code == 400
        assert b'{\n  "Error": "Bad token"\n}\n' in rq.data
