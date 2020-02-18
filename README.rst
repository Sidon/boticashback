#########################################
``Teste para desenvolvimento python``
#########################################


Descrição
**********

| Desafio – “Eu revendedor ‘O Boticário’ quero ter benefícios de acordo com o meu volume de vendas”.


PROBLEMA/OPORTUNIDADE
*********************
A oportunidade proposta é criar um sistema de Cashback, onde o valor será disponibilizado
como crédito para a próxima compra da revendedora no Boticário;
Cashback quer dizer “dinheiro de volta”, e funciona de forma simples: o revendedor faz uma
compra e seu benefício vem com a devolução de parte do dinheiro gasto.
Sendo assim o Boticário quer disponibilizar um sistema para seus revendedores(as)
cadastrarem suas compras e acompanhar o retorno de cashback de cada um.

Cashback quer dizer “dinheiro de volta”, e funciona de forma simples: o revendedor faz uma
compra e seu benefício vem com a devolução de parte do dinheiro gasto.



:Date: **15/02/2020**
:Author: **Sidon Duarte**

TL;DR
*******
| A aplicação foi hospedada no `Heroku <http://www.heroku.com>`_.
| Para testá-la clique: https://<in progress>/.
| Repositorio no github: https://github.com/Sidon/boticashb.

Ambiente de desenvolvimento:
****************************

    +-------------------+---------------------------+------------+
    | Resource          | Description               | Version    |
    +===================+===========================+============+
    | Computer          | Desktop 16 GB Memory      | I5 G5      |
    +-------------------+---------------------------+------------+
    | Operating System  | Ubuntu  LTS               | 18.04      |
    +-------------------+---------------------------+------------+
    | Editor/IDE        | Pycharm                   | 2019.3     |
    +-------------------+---------------------------+------------+
    | venv              | Conda (Miniconda)         | 4.7.12     |
    +-------------------+---------------------------+------------+
    | Devel Platform    + Django/Python             | 3.8        |
    +-------------------+---------------------------+------------+
    | CI                | CircleCI                  | 2017-08    |
    +-------------------+---------------------------+------------+
    | Coverage          | Codecov                   |            |
    +-------------------+---------------------------+------------+
    | Django            | Main framework            | 3.0.3      |
    +-------------------+---------------------------+------------+
    | DRF               | dajano-rest-fw            |  4.4.0     |
    +-------------------+---------------------------+------------+


#########################
Acessando a API via Curl
#########################


Cadastrar um revendedor
***********************

.. code-block::

    curl --location --request POST 'https://sdn-boticario.herokuapp.com/api/v1/revendedores/' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "full_name": "Frank Vincent Zappa",
        "cpf": "18375314048",
        "email": "frank@zappa.net",
        "password": "master123"
    }'

Response:

.. code-block::

    {
        "id": 9,
        "full_name": "Frank Vincent Zappa",
        "cpf": "18375314048",
        "email": "frank@zappa.net"
    }

Obter Token:
************

.. code-block::

    curl --location --request POST 'https://sdn-boticario.herokuapp.com/api/token/' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "email": "frank@zappa.net",
        "password": "master123"
    }'

Response:

.. code-block::

    {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU4MjA2NzAzMCwianRpIjoiZmY1ZTcwZDU3MjIwNDBhN2E0MjBmY2M2MjE5MzBiZTkiLCJ1c2VyX2lkIjo5fQ.A54xO9Ery7t_G5Whr_5JEpZuLGs3mJkc5ggpS4K6lUI",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgxOTgwOTMwLCJqdGkiOiI1ZmI2NDAzZjhmMjE0NjViYjdjNTRkYjg1MjNkMjQzZCIsInVzZXJfaWQiOjl9.IWS2wFI6suHNhJe--r61sfMja0e0Wenhy_iFFwiMoE0"
    }

API Root:
*********

.. code-block::


    $ curl https://sdn-boticario.herokuapp.com/api/v1/
    {"revendedores":"https://sdn-boticario.herokuapp.com/api/v1/revendedores/"}




Instalação local
****************

IN PROGRESS