import pytest
import grpc

from pyopeclient.grpc.Protos import session_pb2_grpc


@pytest.fixture(scope="session")
def channel():
    return grpc.insecure_channel("localhost:5217")


@pytest.fixture(scope="session")
def session_client(channel):
    return session_pb2_grpc.SessionServiceStub(channel)