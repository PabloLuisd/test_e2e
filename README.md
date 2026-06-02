# Testes E2E com Selenium - SauceDemo

## Sobre o projeto

Este projeto foi desenvolvido para a disciplina de Testes de Software do curso de TADS - IFRS campus Rolante, com o objetivo de praticar testes automatizados E2E utilizando Selenium e Pytest.

O sistema utilizado foi o SauceDemo, da empresa Sauce Labs.

Link do sistema: https://www.saucedemo.com


## O que o sistema faz

O SauceDemo é um site de exemplo de loja virtual onde é possível:

* Fazer login
* Ver produtos
* Adicionar produtos ao carrinho
* Remover produtos
* Fazer checkout


## Testes realizados

* Login válido
* Login inválido
* Logout
* Adicionar produto ao carrinho
* Remover produto do carrinho
* Checkout válido
* Checkout inválido


## Tecnologias usadas

* Python
* Selenium
* Pytest


## Como executar

1. Criar ambiente virtual:

python3 -m venv venv

2. Ativar o ambiente:

source venv/bin/activate

3. Instalar dependências:

pip install -r requirements.txt

4. Rodar os testes:

pytest -v


## Estrutura do projeto


* pages/ → classes Page Object das páginas do sistema
* tests/ → cenários de teste automatizados
* conftest.py → fixture responsável por criar e fechar o navegador
* requirements.txt → dependências do projeto
* README.md → documentação do projeto


## Dependências

- selenium
- pytest
- webdriver-manager


## Limitações

Durante o desenvolvimento em Linux com Firefox instalado via Snap, foi necessário configurar o caminho do navegador no arquivo conftest.py para que o Selenium pudesse iniciar corretamente o Firefox.
Dependendo do sistema operacional utilizado, essa configuração poderá precisar ser ajustada.


## Observações

* Foi utilizado o padrão Page Object para organizar o código
* Os testes simulam ações reais de um usuário

## Autor

Nome: Pablo da Silva
Curso: TADS - IFRS Campus Rolante
