# PSPD Laboratório 1

## Alunos
Gabriel Davi Pereira - 17/0010341
João Pedro José Santos da Silva Guedes - 17/0013910

## Objetivo do Lab
Trabalhar com as ferramentas rpcgen e grpc para criar um contador de palavras de um arquivo de maneira distribuída

## Tecnologias utilizadas
### RPC
Para o RPC foram utilizadas as seguintes tecnologias:
- C
- Makefile
- [rpcgen](https://manpages.ubuntu.com/manpages/bionic/man1/rpcgen.1.html)

### GRPC
- [python3](https://www.python.org/downloads/)
- [grpc](https://grpc.io/docs/languages/python/quickstart/)

## Como rodar
### RPC

1. Instalar todas as depedências citadas acima;
2. Rodar o comando `make` para gerar os arquivos executáveis
3. Rodar o arquivo do servidor:
`./word_counter_server`
4. Rodar o arquivo do client:
`./word_counter_client {palavra_buscada} {arquivo_txt} {endereco_do_server_1} {endereco_do_server_2}`

### GRPC
1. Instalar todas as dependências citadas acima;
2. Rodar o servidor(es), com o comando abaixo, e digitar a porta, quando requisitada:
`python3 word_count_server.py`
3. Rodar o client com o comando abaixo e inserir informações requisitadas:
`python3 word_count_client.py`
