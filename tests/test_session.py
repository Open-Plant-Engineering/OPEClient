from pyopeclient.grpc.Protos import session_pb2


def test_start_session(session_client):
    res = session_client.StartSession(
        session_pb2.StartSessionRequest(userId="test-user")
    )

    assert res.sessionId is not None
    assert len(res.sessionId) > 0


def test_close_session(session_client):
    start = session_client.StartSession(
        session_pb2.StartSessionRequest(userId="test-user")
    )

    res = session_client.CloseSession(
        session_pb2.CloseSessionRequest(sessionId=start.sessionId)
    )

    assert res.success is True