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

    def test_update_playlist_should_be_return_200(self, client, login_token_header, playlists):
        payload = {
            "playlist_id": str(uuid.uuid4()),
            "api": "spotify",
            "is_active": False
        }

        rq = client.put(f"/api/share/playlist/{str(playlists.playlist_id)}", json=payload, headers=login_token_header)

        assert rq.status_code == 200
        assert b"playlist_id"

    def test_update_without_data_should_be_return_400(self, client, login_token_header, playlists):
        rq = client.put(f"/api/share/playlist/{playlists.playlist_id}", json={}, headers=login_token_header)

        assert rq.status_code == 400

    def test_update_incorrect_id_should_be_return_400(self, client, login_token_header, playlists):
        payload = {
            "playlist_id": str(uuid.uuid4()),
            "api": "spotify",
            "is_active": False
        }
        rq = client.put(f"/api/share/playlist/{uuid.uuid4()}", json=payload, headers=login_token_header)
        assert rq.status_code == 404

    def test_delete_playlist_correct_playlist_id_should_be_return_204(self, client, login_token_header, playlists):
        rq = client.delete(f"/api/share/playlist/{playlists.playlist_id}", headers=login_token_header)

        assert rq.status_code == 204

    def test_delete_playlist_incorrect_playlist_id_should_be_return_404(self, client, login_token_header, playlists):
        rq = client.delete(f"/api/share/playlist/{str(uuid.uuid4())}", json={}, headers=login_token_header)

        assert rq.status_code == 404


class TestApiSongController:
    def test_get_items_should_be_return_200(self, client, login_token_header, songs):
        rq = client.get("/api/share/songs", headers=login_token_header)

        assert rq.status_code == 200
        assert b"results" in rq.data
        assert b"page" in rq.data
        assert b"songs" in rq.data

    def test_get_playlists_with_pagination_page_not_found_should_be_return_404(self, login_token_header, client, user,
                                                                               songs):
        rq = client.get("/api/share/songs?page=24", headers=login_token_header)

        assert rq.status_code == 404

    def test_delete_song_correct_song_id_should_be_return_204(self, login_token_header, client, user, songs):
        rq = client.delete(f"/api/share/songs/{songs.record_id}", headers=login_token_header)

        assert rq.status_code == 204

    def test_delete_song_incorrect_song_id_should_be_return_404(self, login_token_header, client, user, songs):
        rq = client.delete(f"/api/share/songs/{str(uuid.uuid4())}", headers=login_token_header)

        assert rq.status_code == 404
