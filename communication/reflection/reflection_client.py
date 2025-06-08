# 서버에서 제공하는 서비스/메서드를 확인하는 클라이언트 코드

import grpc
from grpc_reflection.v1alpha import reflection_pb2, reflection_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = reflection_pb2_grpc.ServerReflectionStub(channel)
        
        # 서버에서 제공하는 모든 서비스 나열
        request = reflection_pb2.ServerReflectionRequest(list_services="")
        response = stub.ServerReflectionInfo(iter([request]))
        for service in response:
            for service_response in service.list_services_response.service:
                print(f"서비스: {service_response.name}")
                
        # 특정 서비스의 메서드 나열
        service_name = "reflection_example.EchoService"
        request = reflection_pb2.ServerReflectionRequest(
            file_containing_symbol=service_name
        )
        response = stub.ServerReflectionInfo(iter([request]))
        for file_descriptor in response:
            for proto in file_descriptor.file_descriptor_response.file_descriptor_proto:
                print(f"proto: {proto}")


if __name__ == "__main__":
    run()