import uuid


class TestApiController:
    def test_get_playlists_without_pagination_should_be_return_status_ok(self, login_token_header, client, user,
                                                                         playlists):
        rq = client.get("/api/share/playlist", headers=login_token_header)

        assert rq.status_code == 200
        assert b"results" in rq.data
        assert b"page" in rq.data
        assert b"playlists" in rq.data

    def test_get_playlists_with_pagination_page_not_found_should_be_return_404(self, login_token_header, client, user,
                                                                               playlists):
        rq = client.get("/api/share/playlist?page=24", headers=login_token_header)

        assert rq.status_code == 404

    def test_post_create_playlist_correct_data_should_be_return_201(self, client, login_token_header, playlists):
        payload = {
            "playlist_id": str(uuid.uuid4()),
            "api": "deezer",
            "is_active": True
        }

        rq = client.post("/api/share/playlist", json=payload, headers=login_token_header)
        assert rq.status_code == 201
        assert b"playlist_id" in rq.data

    def test_post_create_playlist_without_playlist_id_should_be_return_400(self, login_token_header, client, playlists):
        payload = {
            "api": "deezer",
            "is_active": True
        }

        rq = client.post("/api/share/playlist", json=payload, headers=login_token_header)

        assert rq.status_code == 400
