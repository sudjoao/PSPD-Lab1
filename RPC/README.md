# RPC

## Tecnologias utilizadas

Para o RPC foram utilizadas as seguintes tecnologias:
- C
- rpcgen
- Makefile

## Como rodar

1. Instalar todas as depedências citadas acima;
2. Rodar o comando `make` para gerar os arquivos executáveis
3. Rodar o arquivo do servidor:
`./word_counter_server`
4. Rodar o arquivo do client:
`./word_counter_client {palavra_buscada} {arquivo_txt} {endereco_do_server_1} {endereco_do_server_2}`
