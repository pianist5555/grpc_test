import grpc
from concurrent import futures
import messages_pb2
import messages_pb2_grpc
import time


class ChatService(messages_pb2_grpc.ChatServiceServicer):
    def ChatStream(self, request, context):
        print(f"클라이언트에서 보낸 메시지: {request.message}")
        
        messages = [
            "안녕하세요",
            "gRPC 서버 스트리밍 예제입니다.",
            "클라이언트에서 보낸 메시지를 받아 처리합니다.",
        ]
        
        for message in messages:
            yield messages_pb2.ChatMessage(message=message)
            time.sleep(1)
            
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    messages_pb2_grpc.add_ChatServiceServicer_to_server(ChatService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    
    print('서버시작...')
    server.wait_for_termination()
    
if __name__ == "__main__":
    serve()
