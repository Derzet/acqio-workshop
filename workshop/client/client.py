import grpc

from acqio import bank_pb2
from acqio import bank_pb2_grpc

def ping(text):
    with grpc.insecure_channel('bank:3000') as channel:
        stub = bank_pb2_grpc.BankStub(channel)
        response = stub.Ping(bank_pb2.PingRequest(text=text))
        print(response)

if __name__ == '__main__':
    ping('Hi')

