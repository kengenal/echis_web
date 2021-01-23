class TestApiAuthController:
    def test_get_api_correct_token_should_be_return_jwt_token(self, client, token, user):
        rq = client.get(f"/api/auth", headers={"Authorization": f"Barer {token}"})

        assert rq.status_code == 200
        assert b"token" in rq.data
        assert b"user" in rq.data

    def test_bad_payload_data_from_token_should_be_raise_400(self, token_invalid_payload, client, user):
        rq = client.get(f"/api/auth", headers={"Authorization": f"Barer {token_invalid_payload}"})

        assert rq.status_code == 400
        assert b"avatar" in rq.data
        assert b"discord_id" in rq.data

    def test_with_broken_token_should_be_raise_400(self, client, user):
        rq = client.get("/api/auth", headers={"Authorization": "random"})

        assert rq.status_code == 400
        assert b'{\n  "Error": "Bad token"\n}\n' in rq.data
