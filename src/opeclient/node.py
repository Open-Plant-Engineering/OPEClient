class Node:

    def __init__(self, transport, node_id):
        self.transport = transport
        self.node_id = node_id

    # -------------------------
    # GET NODE
    # -------------------------
    def get(self):
        res = self.transport.get(f"/node/{self.node_id}")
        return res["data"]

    # -------------------------
    # UPDATE NODE
    # -------------------------
    def update(self, changes):

        # ✅ fetch latest version
        data = self.transport.get(f"/node/{self.node_id}")
        version = data.get("_version")  # OR adjust based on API

        return self.transport.post(
            "/node/update",
            {
                "node_id": self.node_id,
                "base_version": version,
                "changes": changes
            }
        )

    # -------------------------
    # HISTORY
    # -------------------------
    def history(self):
        res = self.transport.get(f"/node/{self.node_id}/history")
        return res["history"]

    # -------------------------
    # ROLLBACK
    # -------------------------
    def rollback(self, target_version):
        return self.transport.post(
            "/node/rollback",
            {
                "node_id": self.node_id,
                "target_version": target_version
            }
        )