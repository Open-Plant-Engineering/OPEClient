class Node:

    def __init__(self, transport, node_id):
        self.transport = transport
        self.node_id = node_id

    def get(self):
        res = self.transport.get(f"/node/{self.node_id}")
        return res["data"]

    def claim(self):
        return self.transport.post("/node/claim", {
            "node_id": self.node_id
        })

    def release(self):
        return self.transport.post("/node/release", {
            "node_id": self.node_id
        })

    def update(self, base_version, changes):
        return self.transport.post("/node/update", {
            "node_id": self.node_id,
            "base_version": base_version,
            "changes": changes
        })

    def delete(self, base_version):
        return self.transport.post("/node/delete", {
            "node_id": self.node_id,
            "base_version": base_version
        })

    def history(self):
        res = self.transport.get(f"/node/{self.node_id}/history")
        return res["history"]

    def rollback(self, target_version, attr_ids=None):
        payload = {
            "node_id": self.node_id,
            "target_version": target_version
        }

        if attr_ids:
            payload["attr_ids"] = attr_ids

        return self.transport.post("/node/rollback", payload)