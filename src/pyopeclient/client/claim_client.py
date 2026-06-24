import grpc
from pyopeclient.grpc.Protos import claim_pb2, claim_pb2_grpc


class ClaimClient:
    def __init__(self, host="localhost:5217"):
        self.channel = grpc.insecure_channel(host)
        self.client = claim_pb2_grpc.ClaimServiceStub(self.channel)

    def claim(self, session_id: str, node_id: str):
        def generate():
            yield claim_pb2.ClaimNodeRequest(
                nodeId=node_id,
                sessionId=session_id
            )

        responses = self.client.StreamClaimNodes(generate())

        for res in responses:
            return res.success, res.message
