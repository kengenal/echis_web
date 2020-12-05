
def test_auth(client):
    rq = client.get("/auth/sadasdasd")

    assert rq.status_code == 200
