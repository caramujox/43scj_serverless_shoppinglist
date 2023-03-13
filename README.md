# Projeto Final - 43scj_serverless_shoppinglist

<p align="center">
<img src="img\macro_trabalho_final.png" alt="Desenho macro de solução para o Trabalho">
</p>

> O objetivo deste projeto é desenvolver uma Lambda na AWS (pode ser na linguagem de programação de preferência do grupo e com runtime suportado pela plataforma).

A ideia do projeto é bem simples: Provisionar um sistema de lista de compras com base nos recursos da AWS por meio de uma arquitetura Serverless.

Os recursos utilizados foram:

- DynamoDB
- Simple Queue Service (SQS)
- Lambda Functions

## Integrantes do Grupo

- CAIO DE ARAUJO MORAIS RM: 345756 ✔️
- EVANDRO BORZI MARQUES RM: 345434 ✔️
- GIOVANNI RIBEIRO BENDINELLI TREVISAN RM: 344444 ✔️
- KAIQUE JUVENCIO COSTA RM: 345375 ✔️
- VINICIUS LUCAS SILVESTRE RM: 344213 ✔️

## :white_check_mark: Objetivos, Regras e Requisitos

O projeto contem as seguintes regras de avaliação

- [x] Documentação do projeto em Markdown
- [x] Implementar Persistência
- [x] Implementar Observability

## ☕ Usando e testando o projeto

Para que seja possível testar o projeto no ambiente de cada desenvolvedor é preciso que sejam reconfigurados os ARNs e URLs exibidos nos arquivos

- serverless.yml
- handler.py

Basta troca-los pelo ARN dos recursos existentes já utilizados.

Tome o cuidado, também, para que a conta que execute a lambda tenha os acessos nos recursos DynamoDB, Lambda e SQS.
