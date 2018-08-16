# Acqio Workshop - The Twelve-Factor App

Esse repositório contém um exercício envolvendo boas práticas recomendadas pelo
[Twelve-Factor App](https://12factor.net/).

Está presente um arquivo `.proto` contendo vários métodos referentes à serviços
de Banking, e também um par cliente-servidor que implementa um dos métodos
definidos nesse proto: `Ping`.

Testando o `Ping`:
```
$ cd workshop
$ docker-compose -f server-compose.yml --build

Em um outro terminal:
$ cd workshop
$ docker-compose -f client-compose.yml --build

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

