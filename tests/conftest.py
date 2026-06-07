import pytest
import requests
from opeclient.client import Client

BASE_URL = "http://localhost:8000"
DB = "opecore_test1"


def get_token(user):
    res = requests.post(
        f"{BASE_URL}/auth/login",
        json={"user": user}
    )
    assert res.status_code == 200
    return res.json()["access_token"]


@pytest.fixture
def client():
    token = get_token("user1")

    return Client(
        base_url=BASE_URL,
        project=DB,
        token=token
    )

@pytest.fixture
def tokens():
    return {
        "user1": get_token("user1"),
        "user2": get_token("user2")
    }