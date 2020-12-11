def test_index_controller(client):
    rq = client.get("/home")

    assert rq.status_code == 200
