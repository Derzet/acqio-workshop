from concurrent import futures

import datetime
import math
import sys
import time

import grpc

from acqio import bank_pb2
from acqio import bank_pb2_grpc

from pymongo import MongoClient

bank_db = None

class BankAccount:
    def __init__(self, fullname, password, amount):
        self.fullname = fullname
        self.password = password
        self.amount = amount

class BankServicerImpl(bank_pb2_grpc.BankServicer):
    def Ping(self, request, context):
        print(request)
        return bank_pb2.PingResponse(text='pong bank')

    def Transfer(self, request, context):
        account_collection = bank_db['accounts']

        sender_acc = account_collection.find_one({"account_id": request.account_id})
        if not sender_acc:
            return bank_pb2.TransferResponse(status=1, error='Sender acc not found.')

        receiver_acc = account_collection.find_one({"account_id": request.to_account_id})
        if not receiver_acc:
            return bank_pb2.TransferResponse(status=1, error='Receiver acc not found.')

        if sender_acc['password'] != request.password:
            return bank_pb2.TransferResponse(status=1, error='Wrong password.')

        if sender_acc['amount'] < request.amount:
            return bank_pb2.TransferResponse(status=1, error='Insufficient funds.')

        account_collection.update_one(
            {"account_id": request.account_id},
            {
                "$inc": {
                    "amount": -request.amount
                }
            }
        )
        account_collection.update_one(
            {"account_id": request.to_account_id},
            {
                "$inc": {
                    "amount": request.amount
                }
            }
        )
        return bank_pb2.TransferResponse(status=0)

    def AddAccount(self, request, context):
        if request.admin_password != 'admin':
            return bank_pb2.AddAccountResponse(status=1, error='Wrong admin password.')

        acc = BankAccount(request.fullname, request.password,
                request.initial_amount)
        # mongo insertion
        account_collection = bank_db['accounts']
        acc_dict = acc.__dict__
        acc_id = account_collection.count()
        acc_dict['account_id'] = acc_id
        account_collection.insert_one(acc_dict)

        return bank_pb2.AddAccountResponse(status=0, account_id=acc_id)

def serve():
    print("Initializing...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    bank_pb2_grpc.add_BankServicer_to_server(BankServicerImpl(), server)
    mongo_client = MongoClient('mongodb://bank:bank@mongodb:27017/admin')

    global bank_db
    bank_db = mongo_client['bank']

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

