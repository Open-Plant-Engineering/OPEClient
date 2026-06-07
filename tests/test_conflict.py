from opeclient.client import Client

import requests

BASE_URL = "http://localhost:8000"
DB = "opecore_test1"

def get_token(user):
    res = requests.post(
        f"{BASE_URL}/auth/login",
        json={"user": user}
    )
    assert res.status_code == 200
    return res.json()["access_token"]


def test_update_conflict(tokens):

    client1 = Client(BASE_URL, DB, token=tokens["user1"])
    client2 = Client(BASE_URL, DB, token=tokens["user2"])

    node = client1.create(
        class_id=1,
        attrs={"1": "A", "2": "B", "3": "C"}
    )

    node.claim()

    raw = client1.transport.get(f"/node/{node.node_id}")
    v1 = raw["version"]

    # user1 update
    client1.update(node.node_id, v1, {"4": 10})

    # user2 tries stale update
    try:
        client2.update(node.node_id, v1, {"4": 20})
        assert False, "Expected conflict"
    except Exception:
        assert True
