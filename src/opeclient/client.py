from .transport import Transport
from .node import Node


class Client:

    def __init__(self, base_url, project, token=None):
        self.transport = Transport(base_url, project, token)

    # -------------------------
    # CREATE NODE
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
