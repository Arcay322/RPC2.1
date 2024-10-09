from concurrent import futures
import grpc
import factorial_pb2
import factorial_pb2_grpc

class FactorialService(factorial_pb2_grpc.FactorialServiceServicer):
    def Calculate(self, request, context):
        number = request.number
        result = 1
        for i in range(2, number + 1):
            result *= i
        return factorial_pb2.FactorialResponse(result=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    factorial_pb2_grpc.add_FactorialServiceServicer_to_server(FactorialService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor escuchando en el puerto 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
