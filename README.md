# Spider de Produto

Este repositório é referente ao [teste prático da intelivix](https://github.com/intelivix/teste_pratico_scraping). Com desenvolvimento iniciado em 20/09/2017 e concluído em 23/09/2017.

### Informações gerais
O site escolhido para a busca foi o [KaBuM!](http://kabum.com.br/), um site de *e-commerce* focado em produtos eletrônicos de onde foram obitidos 9515 (até a última execução). Por conta das características do site algumas mudanças foram feitas sobre os campos que foram processados:
* O campo `nome_vendedor` não foi utilizado, pois o KaBuM! é o próprio fornecedor dos produtos (ao contrário de sites como Amazon ou eBay).
* O campo `dimensoes` também não foi utilizado, pois a maior parte dos produtos do site não possui essa informação declarada.
* o campo `valor_desconto` foi adicionado, pois os produtos do site costumeiramente apresentam 3 indicações de preço (original, atual e desconto).

A persistência dos dados foi feita em MongoDB.

### Instruções para execução linux

1. Inicie uma sessão com um usuário com permissão sudo
2. Execute o script `setup` para instalar os requisitos.
3. Inicie o servidor MongoDB
4. No diretório do projeto execute `sudo scrapy crawl kabum`