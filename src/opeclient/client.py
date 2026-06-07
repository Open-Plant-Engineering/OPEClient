from .transport import Transport
from .node import Node


class Client:

    def __init__(self, base_url, project, token=None):
        self.transport = Transport(base_url, project, token)

    # -------------------------
    # CREATE
    # -------------------------
    def create(self, class_id, attrs):
        res = self.transport.post(
            "/node/create",
            {
                "class_id": class_id,
                "attrs": attrs
            }
        )

        return Node(self.transport, res["node_id"])

    # -------------------------
    # GET
    # -------------------------
    def get(self, node_id):
        res = self.transport.get(f"/node/{node_id}")
        return res["data"]

    # -------------------------
    # UPDATE
    # -------------------------
    def update(self, node_id, base_version, changes):
        return self.transport.post(
            "/node/update",
            {
                "node_id": node_id,
                "base_version": base_version,
                "changes": changes
            }
        )

    # -------------------------
    # DELETE NODE
    # -------------------------
    def delete(self, node_id, base_version):
        return self.transport.post(
            "/node/delete",
            {
                "node_id": node_id,
                "base_version": base_version
            }
        )

    # -------------------------
    # DELETE ATTR
    # -------------------------
    def delete_attr(self, node_id, base_version, attr_id):
        return self.transport.post(
            "/node/delete-attr",
            {
                "node_id": node_id,
                "base_version": base_version,
                "attr_id": attr_id
            }
        )

    # -------------------------
    # CLAIM
    # -------------------------
    def claim(self, node_id):
        return self.transport.post(
            "/node/claim",
            {"node_id": node_id}
        )

    # -------------------------
    # RELEASE
    # -------------------------
    def release(self, node_id):
        return self.transport.post(
            "/node/release",
            {"node_id": node_id}
        )

    # -------------------------
    # BULK
    # -------------------------
    def bulk(self, operations):
        return self.transport.post(
            "/node/bulk",
            {"operations": operations}
        )

    # -------------------------
    # HISTORY
    # -------------------------
    def history(self, node_id, page=1, limit=20, user=None, attr_id=None):
        query = f"?page={page}&limit={limit}"

        if user:
            query += f"&user={user}"

        if attr_id:
            query += f"&attr_id={attr_id}"

        res = self.transport.get(f"/node/{node_id}/history{query}")
        return res

    # -------------------------
    # ROLLBACK
    # -------------------------
    def rollback(self, node_id, target_version, attr_ids=None):
        payload = {
            "node_id": node_id,
            "target_version": target_version
        }

        if attr_ids:
            payload["attr_ids"] = attr_ids

        return self.transport.post("/node/rollback", payload)

    # -------------------------
    # ROLLBACK PREVIEW
    # -------------------------
    def rollback_preview(self, node_id, target_version, attr_ids=None):
        payload = {
            "node_id": node_id,
            "target_version": target_version
        }

        if attr_ids:
            payload["attr_ids"] = attr_ids

        return self.transport.post("/node/rollback-preview", payload)