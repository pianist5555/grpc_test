import grpc
from concurrent import futures
import messages_pb2
import messages_pb2_grpc
import time


class ChatService(messages_pb2_grpc.ChatServiceServicer):
    def Chat(self, request_iterator, context):
        for request in request_iterator:
            print(f"클라이언트 메시지: {request.message}")
            response_message = f"서버 응답: {request.message} 받음"
            print(f"서버 메시지: {response_message}")
            yield messages_pb2.ChatMessage(message=response_message)
            time.sleep(1) # 서버가 다음 메시지를 준비하는데 시간 지연 상황
                       

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    messages_pb2_grpc.add_ChatServiceServicer_to_server(ChatService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('서버 시작...')
    server.wait_for_termination()
    
if __name__ == "__main__":
    serve()