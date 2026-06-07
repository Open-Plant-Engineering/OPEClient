def test_create_and_get(client):

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
    assert data["2"] == "Plant1"
    assert data["3"] == "Pump"