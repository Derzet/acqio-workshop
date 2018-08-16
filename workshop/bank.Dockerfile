FROM grpc/python:1.13

COPY bank/ /bank/
COPY protos /protos/

WORKDIR /bank

RUN python -m grpc_tools.protoc \
    -I/protos \
    --python_out=/bank \
    --grpc_python_out=/bank \
    /protos/acqio/bank.proto \
    /protos/google/api/annotations.proto \
    /protos/google/api/http.proto \
    /protos/google/rpc/code.proto \
    /protos/google/rpc/error_details.proto \
    /protos/google/rpc/status.proto

# Weird... but these files are required to avoid ModuleNotFoundError exception.
RUN touch /bank/google/__init__.py \
  && touch /bank/google/api/__init__.py \
  && touch /bank/google/rpc/__init__.py

RUN pip install --no-cache-dir -r ./requirements.txt

EXPOSE 3000

CMD ["python", "-u", "service.py"]
