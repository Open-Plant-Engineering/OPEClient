from pyopeclient.client.session_client import SessionClient
from pyopeclient.client.claim_client import ClaimClient


class WorkflowClient:
    def __init__(self):
        self.session = SessionClient()
        self.claim = ClaimClient()

    def run(self):
        # ✅ Start session
        session_id = self.session.start("atul")
        print("Session:", session_id)

        node_id = "test-node-1"

        # ✅ Claim node
        success, message = self.claim.claim(session_id, node_id)
        print("Claim:", success, message)
