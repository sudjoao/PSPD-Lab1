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
`./word_counter_client`

Após iniciado o servidor, as seguintes perguntas irão aparecer no terminal: 

 - Digite o nome do arquivo que deseja utilizar
 - Digite o nome da palavra que seja saber a ocorrencia
 - Quantidade de workers (1 ou 2)
 - Nome do host numero

 Para fins de teste, o arquivo file.txt está disponível para uso. Porém, caso desejar, pode-se adicionar um novo arquivo .txt na pasta do projeto e informar seu uso na primeira pergunta. 
