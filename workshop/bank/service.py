from concurrent import futures

import datetime
import math
import sys
import time

import grpc

from acqio import bank_pb2
from acqio import bank_pb2_grpc

accounts = [] # TODO: Persist this on MongoDB

class BankAccount:
    def __init__(self, fullname, password, amount):
        self.fullname = fullname
        self.password = password
        self.amount = amount

class BankServicerImpl(bank_pb2_grpc.BankServicer):
    def Ping(self, request, context):
        print(request)
        return bank_pb2.PingResponse(text='pong')

    def Transfer(self, request, context):
        acc_count = len(accounts)
        if acc_count <= request.account_id:
            return bank_pb2.TransferResponse(status=1, error='Sender acc not found.')
        if acc_count <= request.to_account_id:
            return bank_pb2.TransferResponse(status=1, error='Receiver acc not found.')
        sender_acc = accounts[request.account_id]
        if sender_acc.password != request.password:
            return bank_pb2.TransferResponse(status=1, error='Wrong password.')

        if sender_acc.amount < request.amount:
            return bank_pb2.TransferResponse(status=1, error='Insufficient funds.')

        receiver_acc = accounts[request.to_account_id]
        sender_acc.amount -= request.amount
        receiver_acc.amount += request.amount
        return bank_pb2.TransferResponse(status=0)

    def AddAccount(self, request, context):
        if request.admin_password != 'admin':
            return bank_pb2.AddAccountResponse(status=1, error='Wrong admin password.')

        acc = BankAccount(request.fullname, request.password, request.initial_amount)
        accounts.append(acc)
        acc_id = len(accounts)-1
        return bank_pb2.AddAccountResponse(status=0, account_id=acc_id)

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

