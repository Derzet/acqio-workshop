from concurrent import futures

import time

import grpc

from acqio import bank_pb2
from acqio import bank_pb2_grpc

class BankServicerImpl(bank_pb2_grpc.BankServicer):
    def Ping(self, request, context):
        print(request)
        return bank_pb2.PingResponse(text='pong')

def serve():
    print("Initializing...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    bank_pb2_grpc.add_BankServicer_to_server(BankServicerImpl(), server)

    print("Registering port...")
    server.add_insecure_port('0.0.0.0:3000')
    print("Starting...")
    server.start()
    print("Bank is up and running.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()

