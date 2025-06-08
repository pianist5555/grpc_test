import grpc
import messages_pb2
import messages_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = messages_pb2_grpc.ChatServiceStub(channel)
        responses = stub.ChatStream(messages_pb2.ChatMessage(message="시작"))
        for response in responses:
            print(f"Received message: {response.message}")
            
if __name__ == "__main__":
    run()