import grpc
import cancel_example_pb2
import cancel_example_pb2_grpc
import time


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = cancel_example_pb2_grpc.CancelServiceStub(channel)
        request = cancel_example_pb2.Request(request_data="Start")

        # 비동기 호출
        request = stub.LongRunningOperation.future(request)
        
        # 3초 후 요청 취소
        time.sleep(3)
        request.cancel()
        
        try:
            # 응답 받기 시도
            response = request.result()
            print(f"Response received: {response.response_data}")
        except grpc.FutureCancelledError:
            print("Request cancelled")
            
            
if __name__ == "__main__":
    run()