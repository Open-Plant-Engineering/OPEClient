import uuid
from pyopeclient.grpc.Protos import session_pb2


def test_start_session(session_client):
    res = session_client.StartSession(
        session_pb2.StartSessionRequest(userId="test-user")
    )

    assert res.success is True
    assert res.sessionId is not None


def test_close_session(session_client):
    start = session_client.StartSession(
        session_pb2.StartSessionRequest(userId="test-user")
    )

    res = session_client.CloseSession(
        session_pb2.CloseSessionRequest(sessionId=start.sessionId)
    )

    assert res.success is True


def test_close_session_twice(session_client):
    start = session_client.StartSession(
        session_pb2.StartSessionRequest(userId="test-user")
    )

    # First close ✅
    res1 = session_client.CloseSession(
        session_pb2.CloseSessionRequest(sessionId=start.sessionId)
    )

    assert res1.success is True

    # Second close ❌
    res2 = session_client.CloseSession(
        session_pb2.CloseSessionRequest(sessionId=start.sessionId)
    )

    assert res2.success is False
    assert res2.message is not None


def test_close_invalid_session(session_client):
    res = session_client.CloseSession(
        session_pb2.CloseSessionRequest(sessionId="not-a-guid")
    )

    assert res.success is False
    assert res.message is not None
