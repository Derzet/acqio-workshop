# Acqio Workshop - The Twelve-Factor App

Esse repositório contém um exercício envolvendo boas práticas recomendadas pelo
[Twelve-Factor App](https://12factor.net/).

Está presente um arquivo `.proto` contendo vários métodos referentes à serviços
de Banking, e também um par cliente-servidor que implementa um dos métodos
definidos nesse proto: `Ping`.

Testando o `Ping`:
```
$ cd workshop
$ docker-compose -f bank-compose.yml up --build

Em um outro terminal:
$ cd workshop
$ docker-compose -f client-compose.yml up --build

Saída esperada:
$ client_1 | text: "pong"
```

## Passo 1:
Modificar `service.py`, adicionando implementações para os seguintes métodos:
```
AddAccount:
Compara que a AddAccountRequest.admin_password tem valor 'workshop-acqio', e
insere o novo cliente com os dados informados, caso não haja duplicata.

Transfer: Transfere fundos de uma conta para outra, somente se o remetente tiver
saldo suficiente.
```

As contas serão armazenadas em memória, e não persistidas.

## Passo 2:
Utilizar MongoDB para persistir BankAccounts.
Utilizar Stack ELK para observar logs.

## Passo 3:
Implementar uma interface para cliente REST, utilizando `devsu/grpc-gateway`. O
usuário deve ser capaz de se comunicar com o servidor através de um REST client,
ao invés de usar o `client.py`.

