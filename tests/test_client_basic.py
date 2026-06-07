from opeclient.client import Client
import requests

BASE_URL = "http://localhost:8000"


def get_token(user):
    res = requests.post(
        f"{BASE_URL}/auth/login",
        json={"user": user}
    )

    assert res.status_code == 200
    return res.json()["access_token"]


def test_client_create_and_get():

    token = get_token("user1")

    client = Client(
        base_url=BASE_URL,
        project="opecore_test1",
        token=token
    )

    node = client.create(
        class_id=1,
        attrs={
            "1": "PumpA",
            "2": "Plant1",
            "3": "Pump"
        }
    )

    data = node.get()

    assert data["1"] == "PumpA"
