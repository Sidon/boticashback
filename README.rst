#########################################
``Teste para desenvolvimento python``
#########################################


Descrição
**********

| Desafio – “Eu revendedor ‘O Boticário’ quero ter benefícios de acordo com o meu volume de vendas”.

TL;DR
*******
| A aplicação está hospedada no Heroku http://www.heroku.com.
| Para testá-la clique: https://sdn-boticario.herokuapp.com/.
| Repositorio no github: https://github.com/Sidon/boticashback.
| Documentação REST API: https://documenter.getpostman.com/view/3684623/SzKYNGXQ
| GraphQL API: https://sdn-boticario.herokuapp.com/graphiql/
| Testes (Integração): https://travis-ci.com/Sidon/boticashback

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

DESCRIÇÃO DA SOLUÇÃO PROPOSTA
*****************************
A applicação está sendo desenvolvida em python/django, tanto no backend (API REST e GraphQL) como no front-end,
contendo 4 subapps (Authenticacao, Caschback, Compras e Revendedores). Usuários administradores poderão cadastrar
novos revendedores, revendedores por sua vez só podoerão cadastar apenas suas compras. Ao ser cadastrado uma compra,
o sistema deverá, automaticamente, checar se aquele revendedor tem valores de cachback a serem resgatados (haverá
uma configuração para o numero de dias em que o resgate poderá serfeito) e gerar um débito (crédito para o revendedor)
de cashback, se aplicável, para aquela conta.

Dados iniciais:
Para simplificar foi utilizado o banco de dados "embutido" no python SQLite3,

Todas as funcionalidades serão disponibilizadas no backend via API REST e Graphql, assim como no front-end através
da url https://sdn-boticario.herokuapp.com/, para acessar como administrador, ao ser solicitado as crdenciais,
digite:

    :Usuário: admin@fakemail.com
    :Senha: Master123


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
    | CI                | travis-ci                 | 2020       |
    +-------------------+---------------------------+------------+
    | Coverage          | Pytest --cov              | 2.8.1      |
    +-------------------+---------------------------+------------+
    | Django            | Main framework            | 3.0.3      |
    +-------------------+---------------------------+------------+
    | DRF               | dajano-rest-fw            |  4.4.0     |
    +-------------------+---------------------------+------------+

:Date: **03/03/2020**
:Author: **Sidon Duarte**

Cobertura (Pytest)
******************

.. code-block::

        --- coverage: platform linux, python 3.8.1-final-0 ----
        Name                                Stmts   Miss  Cover
        -------------------------------------------------------
        boticashback/__init__.py                0      0   100%
        boticashback/asgi.py                    4      4     0%
        boticashback/schema.py                 17     17     0%
        boticashback/settings/__init__.py       0      0   100%
        boticashback/settings/base.py          49      3    94%
        boticashback/settings/dev.py            5      0   100%
        boticashback/urls.py                   29      2    93%
        boticashback/views.py                   6      2    67%
        boticashback/wsgi.py                    4      4     0%
        -------------------------------------------------------
        TOTAL                                 114     32    72%




###########################
Documentação da  API (REST)
###########################

Para a documentação foi utilizado a versão free do software para desenvolvimento de APIs `Postman <https://www.postman.com/>`_.
A documentação oferece exemplos de requests em varios formatos, tais como cURL, c#, Go, HTTP, Javascrip, Java, Etc.
Para acessar clique no link: https://documenter.getpostman.com/view/3684623/SzKYNGXQ

Testes
******
Para testar a api, além do Postman citado, foi utilizado também o pacote `Pytest <https://docs.pytest.org/en/latest/>`_.

Instalação local
****************

Clone o repositorio https://github.com/Sidon/boticashback;

Crie um ambiente virtual com seu gerenciador favorito (conda, pyenv, virtualenv, etc);

Crie uma variável de ambiente chamada ENVIRONMENT com o valor 'local':

.. code-block::

    $ export ENVIRONMENT='local'

No diretorio clonado, instale os requirements com o comando:

.. code-block::

    $ pip install -r dev_requirements.txt

Crie os dados iniciais com o comando:

.. code-block::

    $ python ./manage.py initial_data

Execute a aplicação com o comando:

.. code-block::

    $ python ./manage.py runserver
