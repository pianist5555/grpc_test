import grpc
import helloworld_pb2
import helloworld_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:# 채널 생성
        stub = helloworld_pb2_grpc.GreeterStub(channel)# 스텁 생성 (채널 정보 필요)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name="Alice"),timeout=5)# 요청 전송
        print("Greeter client received: " + response.message)# 응답 출력

if __name__ == "__main__":
    run()