import grpc
from pyopeclient.grpc.Protos import session_pb2, session_pb2_grpc


class SessionClient:
    def __init__(self, host="localhost:5217"):
        self.channel = grpc.insecure_channel(host)
        self.client = session_pb2_grpc.SessionServiceStub(self.channel)

    def start(self, user_id: str) -> str:
        res = self.client.StartSession(
            session_pb2.StartSessionRequest(userId=user_id)
        )
        return res.sessionId

    def close(self, session_id: str):
        res = self.client.CloseSession(
            session_pb2.CloseSessionRequest(sessionId=session_id)
        )
        return res.success