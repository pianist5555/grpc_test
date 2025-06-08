import grpc
import streaming_pb2
import streaming_pb2_grpc


def generate_requests():
    messages = [
        "message1",
        "message2",
        "message3",
    ]
    for message in messages:
        yield streaming_pb2.RequestMessage(data=message)
        
def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = streaming_pb2_grpc.StreamingServiceStub(channel) 
        responses = stub.StreamData(generate_requests()) # 스텁에 전달해서 스트림 데이터로 서버에 요청한다.
        print(f"Received message: {responses.result}")
            
if __name__ == "__main__":
    run()