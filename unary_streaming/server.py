import grpc
from concurrent import futures
import helloworld_pb2
import helloworld_pb2_grpc


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        metadata = dict(context.invocation_metadata())
        print(f"received metadata: {metadata}")
        
        # 클라이언트에 메타데이터 전송
        context.set_trailing_metadata((('server-metadata-key', 'server-metadata-value'),))
        
        return helloworld_pb2.HelloReply(message=f"Hello, {request.name}!")
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10)) # 서버 생성, 컨커런시를 활용하기 위해 스레드풀 사용
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server) # 서비스 등록
    server.add_insecure_port('[::]:50051') # 비보안 채널 시작 (모든 IP 주소의 50051 포트를 받아 처리한다)
    server.start()
    server.wait_for_termination() # 서버가 종료될떄까지 메인함수가 종료되지 않도록 하기위함 (메인 함수가 종료되면 서버도 종료되기 때문에 무한 루프 사용)
    
if __name__ == "__main__":
    serve()