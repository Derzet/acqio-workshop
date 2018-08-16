# Acqio Workshop - The Twelve-Factor App

## Passo 0:
Está presente um arquivo proto contendo vários
métodos referentes à serviços de Banking, e também um par cliente-servidor
que implementa um dos métodos definidos nesse proto: Ping.

## Passo 1:
Modificar service.py, adicionando implementações para os seguintes métodos:
### AddAccount: Compara que a admin_password tem valor 'workshop-acqio', e insere o novo cliente com os dados informados, caso não haja duplicata.
### Transfer: Transfere fundos de uma conta para outra, somente se o remetente tiver saldo suficiente.

As contas serão armazenadas em memória, e não persistidas.

## Passo 2:
Utilizar MongoDB para persistir contas e utilizar Stack ELK para observar logs.

## Passo 3:
Implementar uma interface para cliente REST, utilizando devsu/grpc-gateway. O
usuário deve conseguir se comunicar com o servidor através de um REST client, ao
invés de usar o client.py.

## Passo 4:
Adicionar um Nginx para fazer um reverse proxy. Subir várias instancias do
serviço de banco, e observar no Kibana o balanceamento de carga feito pelo
docker.

## Passo 5:
Definir um novo método no .proto, FullReport, que vai ser capaz de retornar o
extrato de um cliente, exibindo todas as transações, bem como o saldo final do
cliente.

