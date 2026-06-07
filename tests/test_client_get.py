def test_client_get_method(client):

    node = client.create(
        class_id=1,
        attrs={"1": "X", "2": "Y", "3": "Z"}
    )

    data = client.get(node.node_id)

    assert data["1"] == "X"