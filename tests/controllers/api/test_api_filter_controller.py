import pytest

from tests.base_test_case import BaseTokenSetup
from tests.fatories import FilterFactory


class TestFilterController(BaseTokenSetup):
    @pytest.fixture(autouse=True)
    def load_filter(self, client):
        self.url = "/api/filter/words"
        self.filter_module = FilterFactory()
        self.client = client

    def test_get_all_words_should_be_return_status_ok(self):
        rq = self.client.get(self.url, headers=self.auth_header)

        assert rq.status_code == 200

    def test_add_new_word_to_filter_with_correct_data_should_be_return_status_ok(self):
        rq = self.client.post(self.url, headers=self.auth_header, json={
            "words": ["random", "rand"],
        })

        assert rq.status_code == 201

    def test_add_new_world_with_empty_data_should_be_return_bad_request(self):
        rq = self.client.post(self.url, headers=self.auth_header, json={})

        assert rq.status_code == 400

    def test_add_new_world_with_empty_words_should_be_return_bad_request(self):
        rq = self.client.post(self.url, headers=self.auth_header, json={"words": []})

        assert rq.status_code == 400

    def test_delete_world_with_correct_id(self):

        rq = self.client.delete(self.url + f"/{self.filter_module.pk}", headers=self.auth_header)

        assert rq.status_code == 204

    def test_delete_word_with_incorrect_id(self):
        rq = self.client.delete(self.url + f"/2", headers=self.auth_header)

        assert rq.status_code == 404
