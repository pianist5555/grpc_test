1. proto 파일 생성
2. 프로토콜 버퍼 컴파일러를 이용해 코드 생성
2-1. _grpc가 붙으면 gRPC 서비스 클래스를 정의함, 실제로 쓰이는 메서드들 포함 즉 서버와 클라이언트 구현을 위한 코드
2-2. 없으면 메시지 클래스들을 정의함, 직렬화/역직렬화 등

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. my_service.proto

python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. book.proto

python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. helloworld.proto