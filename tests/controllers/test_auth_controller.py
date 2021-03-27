class TestAuth:
    # def test_auth_validate_data_should_be_redirect_to_home(self, client, token):
    #     rq = client.get(f"/auth/{token}")
    #
    #     assert rq.status_code == 302

    def test_auth_invalid_token_should_be_return_404(self, client, token):
        rq = client.get(f"/auth/{token}asdasdasd")

        assert rq.status_code == 404

    def test_invalid_payload_missing_data_should_be_return_404(self, client, token_invalid_payload):
        rq = client.get(f"/auth/{token_invalid_payload}")

        assert rq.status_code == 404
