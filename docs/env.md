python -m grpc_tools.protoc  -I./  --python_out=./src/pyopeclient/grpc  --grpc_python_out=./src/pyopeclient/grpc  Protos/session.proto Protos/claim.proto P
rotos/node.proto Protos/work.proto