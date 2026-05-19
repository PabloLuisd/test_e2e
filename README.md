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



## Tecnologias usadas

* Python
* Selenium
* Pytest

---

## Como executar

1. Criar ambiente virtual:

python3 -m venv venv

2. Ativar o ambiente:

source venv/bin/activate

3. Instalar dependências:

pip install -r requirements.txt

4. Rodar os testes:

pytest


## Estrutura do projeto

* tests/ → arquivos de teste
* pages/ → classes que representam as páginas


## Observações

* Foi utilizado o padrão Page Object para organizar o código
* Os testes simulam ações reais de um usuáro


## Autor

Nome: Pablo da Silva
