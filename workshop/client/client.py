import grpc

from acqio import bank_pb2
from acqio import bank_pb2_grpc

def ping():
    with grpc.insecure_channel('bank:3000') as channel:
        stub = bank_pb2_grpc.BankStub(channel)
        response = stub.Ping(bank_pb2.PingRequest(text='Hi'))
        print(response)

def add_account(admin_password, fullname, password, initial_amount):
    with grpc.insecure_channel('bank:3000') as channel:
        stub = bank_pb2_grpc.BankStub(channel)
        response = stub.AddAccount(bank_pb2.AddAccountRequest(\
                admin_password=admin_password,fullname=fullname,\
                password=password,initial_amount=initial_amount))
        print(response)

def transfer(acc_id, password, to_acc_id, amount):
    with grpc.insecure_channel('bank:3000') as channel:
        stub = bank_pb2_grpc.BankStub(channel)
        response = stub.Transfer(bank_pb2.TransferRequest(\
                account_id=acc_id, password=password, amount=amount,\
                to_account_id=to_acc_id))
        print(response)

def test():
    ping()

    add_account('admin', 'paulo', 'senha', 10)
    add_account('admin', 'barros', 'senha2', 10)

    transfer(0, 'senha', 1, 5)
    transfer(1, 'senha2', 1, 15)

if __name__ == '__main__':
    test()

