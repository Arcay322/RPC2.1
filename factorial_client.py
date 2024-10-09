import grpc
import factorial_pb2
import factorial_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = factorial_pb2_grpc.FactorialServiceStub(channel)
        number = int(input("Ingresa un número para calcular su factorial: "))
        request = factorial_pb2.FactorialRequest(number=number)
        response = stub.Calculate(request)
        print(f"Factorial de {number} es {response.result}")

if __name__ == '__main__':
    run()
