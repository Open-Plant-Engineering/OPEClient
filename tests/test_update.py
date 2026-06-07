def test_update_node(client):

    node = client.create(
        class_id=1,
        attrs={"1": "A", "2": "B", "3": "C"}
    )

    node.claim()

    # get version manually via raw API (for now)
    raw = client.transport.get(f"/node/{node.node_id}")
    version = raw.get("version") or 1  # fallback if not returned

    res = node.update(
        base_version=version,
        changes={"4": 100}
    )

    assert "version" in res

    data = node.get()

    assert data["4"] == 100