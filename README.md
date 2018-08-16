# Acqio Workshop - The Twelve-Factor App

Esse repositório contém um exercício envolvendo boas prática recomendadas pelo
[Twelve-Factor App](https://12factor.net/).

## Passo 0:

Está presente um arquivo proto contendo vários métodos referentes à serviços de
Banking, e também um par cliente-servidor que implementa um dos métodos
definidos nesse proto: Ping.

## Passo 1:
Modificar `service.py`, adicionando implementações para os seguintes métodos:
```
AddAccount:
Compara que a admin_password tem valor 'workshop-acqio', e insere o novo
cliente com os dados informados, caso não haja duplicata.

Transfer: Transfere fundos de uma conta para outra, somente se o remetente tiver
saldo suficiente.
```

As contas serão armazenadas em memória, e não persistidas.

