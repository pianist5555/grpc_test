import grpc
from concurrent import futures
import cancel_example_pb2
import cancel_example_pb2_grpc
import time


class CancelServiceServicer(cancel_example_pb2_grpc.CancelServiceServicer):
    def LongRunningOperation(self, request, context):
        for i in range(10):
            # 요청이 활성 상태인지 스텁에서 제공해주는 context의 is_active 메서드로 확인
            if context.is_active():
                print(f"Processing {i}...")
                time.sleep(1) # 지연 상태를 시뮬레이션 하기 위해 슬립
            else:
                # 요청 취소 시
                print("Request was cancelled")
                return cancel_example_pb2.Response(response_data="Cancelled")
        
        # 작업 완료
        return cancel_example_pb2.Response(response_data="Completed")
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    cancel_example_pb2_grpc.add_CancelServiceServicer_to_server(CancelServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    
    print('서버시작...')
    server.wait_for_termination()
    
if __name__ == "__main__":
    serve()
