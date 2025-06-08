import grpc
from concurrent import futures
import streaming_pb2
import streaming_pb2_grpc


class StreamingService(streaming_pb2_grpc.StreamingServiceServicer):
    def StreamData(self, request_iterator, context):
        result = ""
        for req in request_iterator:
            print(f"Received partial message: {req.data}")
            result += req.data + ""
        print(f"Received final message: {result}")
        return streaming_pb2.ResponseMessage(result=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    streaming_pb2_grpc.add_StreamingServiceServicer_to_server(StreamingService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
    
if __name__ == "__main__":
    serve()