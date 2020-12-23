class TestHomeController:
    def test_index_controller(self, client, login):
        rq = client.get("/home")

        assert rq.status_code == 200

    def test_index_controller_without_session_should_be_get_404(self, client, empty_session):
        rq = client.get("/home")

        assert rq.status_code == 404
