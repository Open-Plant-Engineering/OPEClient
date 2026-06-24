from pyopeclient.grpc.Protos import claim_pb2, session_pb2
import uuid

def test_claim_node(channel, session_client):
    claim_client = __import__(
        "pyopeclient.grpc.Protos.claim_pb2_grpc", fromlist=["ClaimServiceStub"]
    ).ClaimServiceStub(channel)

    # ✅ create session
    session = session_client.StartSession(
        session_pb2.StartSessionRequest(userId="test")
    )

    session_id = session.sessionId
    node_id = str(uuid.uuid4())

    def gen():
        yield claim_pb2.ClaimNodeRequest(
            nodeId=node_id,
            sessionId=session_id
        )

    responses = claim_client.StreamClaimNodes(gen())

    res = next(responses)

    assert res.success is True
