import uuid

from echis_web.model.share_model import Playlists


class TestPlaylist:
    URL = "/share/playlists"

    def test_get_playlist_should_be_return_200_and_list_of_playlist(self, client, login, playlists):
        rq = client.get(self.URL)

        assert rq.status_code == 200

    def test_get_with_paginate_page_does_not_exists(self, client, login):
        rq = client.get(f"{self.URL}?page=6")

        assert rq.status_code == 404

    def test_create_new_render_form_test(self, login, client):
        rq = client.get(f"{self.URL}/new")

        assert rq.status_code == 200
        assert b'id="is_active"' in rq.data
        assert b"Add new playlist" in rq.data

    def test_create_new_correct_data_should_be_redirect(self, login, client):
        playlist_id = str(uuid.uuid4())
        rq = client.post(f"{self.URL}/new", data={
            "playlist_id": playlist_id,
            "api": "deezer",
            "is_active": True
        }, follow_redirects=True)

        get = Playlists.objects.get(playlist_id=playlist_id)

        assert len(get) > 0
        assert rq.status_code == 200
        assert b"Playlist has been added"

    def test_create_new_correct_data_should_be_display_errors_in_template(self, login, client):
        rq = client.post(f"{self.URL}/new", data={})

        assert rq.status_code == 200
        assert b'<ul class="errors alert-danger">' in rq.data

    def test_edit_playlist_render_template_with_data_with_data_from_database(self, login, client, playlists):
        rq = client.get(f"{self.URL}/{playlists.playlist_id}/edit")

        assert rq.status_code == 200
        assert b"Edit playlist" in rq.data

    def test_edit_playlist_playlist_not_found_should_be_abord_404(self, login, client):
        rq = client.get(f"{self.URL}/random/edit")

        assert rq.status_code == 404

    def test_edit_playlist_with_correct_data_to_edit_should_be_redirect(self, login, client, playlists):
        playlist_id = str(uuid.uuid4())
        rq = client.post(f"{self.URL}/{playlists.playlist_id}/edit", data={
            "playlist_id": playlist_id,
            "api": playlists.api,
            "is_active": playlists.is_active
        })

        get = Playlists.objects.get(playlist_id=playlist_id)
        assert rq.status_code == 302
        assert len(get) > 0

    def test_delete_playlist_with_exists_playlist_should_be_redirect(self, client, login, playlists):
        rq = client.get(f"{self.URL}/{playlists.playlist_id}/delete")
        get = Playlists.objects(playlist_id=playlists.playlist_id)

        assert rq.status_code == 302
        assert len(get) == 0

    def test_delete_playlist_with_wrong_playlist_id_should_be_return_404(self, login, client, playlists):
        rq = client.get(f"{self.URL}/random/delete")

        assert rq.status_code == 404

