# Star Wars Planet API

Este repositório consiste em uma aplicação com um CRUD com planetas aonde se faz necessário consumir uma api para 
verificar aparições destes planetas nos filmes de starwars (swapi) e armazenar os dados necessários em um banco de 
dados.

## Tecnologias

- Fast API
- MongoDB
- Docker

## Variaveis de Ambiente

Para execução da aplicação é necessário uma variável de ambiente referenciando a base de dados do projeto e outra a fim 
de informar a api da SWAPI.

Ex:

    DATABASE_URI=mongodb://localhost:27017/
    SWAPI_URI=https://swapi.co/api/planets/

## Iniciar a Aplicação

Com o mongo db devidamente inicializado e variaveis de ambiente preenchidas.

### Execução de Testes

    $ python -m unittest discover
    
or 

    $ coverage run --source=test -m unittest discover
    $ coverage report

### Execução do servico

Para iniciar a aplicação, primeiro é necessário instalar as dependencias do projeto
    
    pip install -r requirements.txt
    
e em seguida iniciar a aplicação

    uvicorn starter:app --reload --host 0.0.0.0 --port 8080
    
## Requests
A api suporta requests de GET, POST, DELETE.

GET: `localhost:8080/api/planet/` Busca todos os planetas cadastrados na base de dados.

    Resposta:
    [
       {
           "name": "nome do planeta",
           "terrain": "terreno do planeta",
           "climate": "clima do planeta",
           "apparition_counter": 0
        }
    ]

GET: `localhost:8080/api/planet/{ID}` Busca o planeta cadastrado com o ID indicado.

GET: `localhost:8080/api/planet_name?planet_name={NAME}` Busca o planeta cadastrado com o nome indicado.

    Resposta:
    
    {
        "name": "nome do planeta",
        "terrain": "terreno do planeta",
        "climate": "clima do planeta",
        "apparition_counter": 0
    }


POST: `localhost:8080/api/planet/` Insere um novo planeta na base de dados. Para isso se faz necessário enviar um json com a seguinte estrutura:


    {
        "name": "nome do planeta",
        "terrain": "terreno do planeta",
        "climate": "clima do planeta"
    }


DELETE: `localhost:8080/api/planet/{ID}` Deleta um planeta na base de dados com o id indicado.
    
    Sem conteúdo de resposta

### Erros comuns:

* Campo vazio, gera um erro de BAD REQUEST.
* Planeta já existente, gera um erro de CONFLICT.
* Planeta não encontrado, gera um erro de NOT FOUND.