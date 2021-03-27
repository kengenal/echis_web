import uuid

from tests.base_test_case import BaseTokenSetup


class TestApiController(BaseTokenSetup):
    def test_get_playlists_without_pagination_should_be_return_status_ok(self, playlists):
        rq = self.client.get("/api/share/playlist", headers=self.auth_header)

        assert rq.status_code == 200
        assert b"results" in rq.data
        assert b"page" in rq.data
        assert b"playlists" in rq.data

    def test_get_playlists_with_pagination_page_not_found_should_be_return_404(self, playlists):
        rq = self.client.get("/api/share/playlist/24", headers=self.auth_header)

        assert rq.status_code == 404

    def test_post_create_playlist_correct_data_should_be_return_201(self, playlists):
        payload = {
            "playlist_id": str(uuid.uuid4()),
            "api": "deezer",
            "is_active": True
        }

        rq = self.client.post("/api/share/playlist", json=payload, headers=self.auth_header)
        print(rq.data)
        assert rq.status_code == 201
        assert b"playlist_id" in rq.data

    def test_create_playlist_with_duplicate_key_should_be_return_400_with_message(self, playlists):
        payload = {
            "playlist_id": playlists.playlist_id,
            "api": playlists.api,
            "is_active": playlists.is_active
        }
        rq = self.client.post("/api/share/playlist", json=payload, headers=self.auth_header)

        assert rq.status_code == 400
        assert b'playlist_id' in rq.data

    def test_post_create_playlist_without_playlist_id_should_be_return_400(self, playlists):
        payload = {
            "api": "deezer",
            "is_active": True
        }
        rq = self.client.post("/api/share/playlist", json=payload, headers=self.auth_header)

        assert rq.status_code == 400

    def test_update_playlist_should_be_return_200(self, playlists):
        payload = {
            "is_active": False
        }

        rq = self.client.put(f"/api/share/playlist/{str(playlists.playlist_id)}", json=payload,
                             headers=self.auth_header)

        assert rq.status_code == 200
        assert b"playlist_id"

    def test_update_without_data_should_be_return_400(self, playlists):
        rq = self.client.put(
            f"/api/share/playlist/{str(playlists.playlist_id)}",
            json={},
            headers=self.auth_header
        )
        assert rq.status_code == 400

    def test_update_incorrect_id_should_be_return_400(self, playlists):
        payload = {
            "is_active": False
        }
        rq = self.client.put(f"/api/share/playlist/{uuid.uuid4()}", json=payload, headers=self.auth_header)
        assert rq.status_code == 404

    def test_delete_playlist_correct_playlist_id_should_be_return_204(self, playlists):
        rq = self.client.delete(f"/api/share/playlist/{playlists.playlist_id}", headers=self.auth_header)

        assert rq.status_code == 204

    def test_delete_playlist_incorrect_playlist_id_should_be_return_404(self, playlists):
        rq = self.client.delete(f"/api/share/playlist/{str(uuid.uuid4())}", json={}, headers=self.auth_header)

        assert rq.status_code == 404


class TestApiSongController(BaseTokenSetup):
    def test_get_items_should_be_return_200(self, songs):
        rq = self.client.get("/api/share/songs", headers=self.auth_header)

        assert rq.status_code == 200
        assert b"results" in rq.data
        assert b"page" in rq.data
        assert b"songs" in rq.data

    def test_get_playlists_with_pagination_page_not_found_should_be_return_404(self, songs):
        rq = self.client.get("/api/share/songs/24", headers=self.auth_header)

        assert rq.status_code == 404

    def test_delete_song_correct_song_id_should_be_return_204(self, songs):
        rq = self.client.delete(f"/api/share/songs/{songs.record_id}", headers=self.auth_header)

        assert rq.status_code == 204

    def test_delete_song_incorrect_song_id_should_be_return_404(self, songs):
        rq = self.client.delete(f"/api/share/songs/{str(uuid.uuid4())}", headers=self.auth_header)

        assert rq.status_code == 404
