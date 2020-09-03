# Star Wars Planet API

Este repositório consiste em uma aplicação com um CRUD com planetas aonde se faz necessário consumir uma api para 
verificar aparições destes planetas nos filmes de starwars (swapi) e armazenar os dados necessários em um banco de 
dados.

## Tecnologias

- Fast API
- MongoDB
- Docker

## Execução de Testes

    $ python -m unittest discover
    
or 

    $ coverage run --source=tests -m unittest discover
    $ coverage report

## Mongo Configuration

Para execução da aplicação é necessário uma variável de ambiente referenciando a base de dados do projeto.

Ex:

    DATABASE_URI=mongodb://localhost:27017/

## Iniciar a Aplicação

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
           "climate": "clima do planeta"
        }
    ]

GET: `localhost:8080/api/planet/{ID}` Busca o planeta cadastrado com o ID indicado.

GET: `localhost:8080/api/planet/name/?name={NAME}` Busca o planeta cadastrado com o nome indicado.

    Resposta:
    
    {
        "name": "nome do planeta",
        "terrain": "terreno do planeta",
        "climate": "clima do planeta"
    }


POST: `localhost:8080/api/planet/` Insere um novo planeta na base de dados. Para isso se faz necessário enviar um json com a seguinte estrutura:

```
{
    "name": "nome do planeta",
    "terrain": "terreno do planeta",
    "climate": "clima do planeta"
}
```

DELETE: `localhost:8080/api/planet/{ID}` Deleta um planeta na base de dados com o id indicado.
    
    Sem conteúdo de resposta


## Exceptions

Caso ocorra um erro, o retorno será da seguinte forma:

```
{
    "error": "Mensagem do erro"
}
```
### Erros comuns:

* Campo vazio, gera um erro de BAD REQUEST.
* Planeta já existente, gera um erro de CONFLICT.
* Planeta não encontrado, gera um erro de NOT FOUND.