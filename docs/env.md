unset GITHUB_TOKEN
gh auth login
gh auth setup-git

python -m grpc_tools.protoc  -I./  --python_out=./src/pyopeclient/grpc  --grpc_python_out=./src/pyopeclient/grpc  Protos/session.proto Protos/claim.proto Protos/node.proto Protos/work.proto