import grpc
import messages_pb2
import messages_pb2_grpc
import time


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = messages_pb2_grpc.ChatServiceStub(channel)
        
        # 메시지를 보내고 응답을 받기 위한 요청 생성기
        def request_generator():
            messages = [
                "안녕하세요",
                "gRPC 양방향 스트리밍 테스트",
                "입니다. 괜찮나요?",
            ]
            for message in messages:
                print(f"클라이언트 메시지: {message}")
                yield messages_pb2.ChatMessage(message=message)
                time.sleep(2)
                
        # 서버로부터 응답을 받는 스트림을 생성
        responses = stub.Chat(request_generator())
        
        # 서버로 받은 메시지 출력
        for response in responses:
            print(f"서버 응답: {response.message}")
                
            
if __name__ == "__main__":
    run()