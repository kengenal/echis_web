import pytest

from echis_web.utils.token import create_token


@pytest.fixture
def token():
    prepare_data = {
        "permissions": "ADMIN|USER",
        "username": "TestName",
        "discord_id": 13456,
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


class TestAuth:
    def test_auth_validate_data_should_be_redirect_to_home(self, client, token):
        rq = client.get(f"/auth/{token}")

        assert rq.status_code == 302

    def test_auth_invalid_token_should_be_return_404(self, client, token):
        rq = client.get(f"/auth/{token}asdasdasd")

        assert rq.status_code == 404

    def test_invalid_payload_missing_data_should_be_return_404(self, client, token_invalid_payload):
        rq = client.get(f"/auth/{token}")

        assert rq.status_code == 404
