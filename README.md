# Brat - rapid annotation tool

Neste repositório você encontra os arquivos Docker necessários para executar a ferramenta *Brat* em containers e executar localmente ou em servidres como Heroku e Google Cloud.

*Brat - Brat Rapid Annotation Tool* é uma aplicação online para anotação colaborativa de corpus.

Para documentação da ferramenta, acesse:

- [brat homepage][brat]
- [brat_github][brat_github]

[brat]:         http://brat.nlplab.org
[brat_github]:  https://github.com/nlplab/brat/

#### Instalação:

Você precisará de:
	
- [Docker](https://docs.docker.com/install/) instalado em seu compuatdor
- Sistema operacional: Linux, MacOS ou Windows
- Requerimentos do sistema: pelo menos 8GB de memória

Para adicionar vários usuários, altere o arquivo `users.json` informando o nome do usuário e a senha, conforme abaixo:

```javascript
{
    "user1": "password",
    "user2": "password",
    ...
}
```

Se você desejar adicionar um novo corpus a ser anotado, você primeiro deve deixar o corpus no formato brat (contendo os arquivos .txt e .ann) e copiar a sua pasta contendo os aquivos antes de gerar a imagem. Vamos supor que seu corpus esteja na pasta "meuCorpus":

```
COPY meuCorpus /var/www/brat/brat-v1.3_Crunchy_Frog/data/meuCorpus
```

Para fazer o build da imagem: 

	$ docker build -t brat .

Para executar a imagem: 

	$ docker run --name brat_instance -p 80:80 -d brat

Para abrir a aplicação:

Abra o navegador e entre neste endereço: http://localhost/

Para parar e remover o container que está executando:

```
docker stop brat_instance

docker rm brat_instance
```

Para remover a imagem criada:
```
docker rmi [-f] brat
```

#### Para executar o container no Heroku:

Você deverá ter o [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli) instalado. Primeiro, abra o CMD e entre na pasta onde os arquivos do docker estão (pode ser onde você clonou este projeto).

Faça o login no Heroku (o primeiro comando abrirá o navegador para você se autenticar):

```
heroku login

heroku container:login
```

Basta enviar a imagem com o comando `push`, executar com o `release` e ver a aplicação com o comando `open`:

```
heroku container:push web --app minhaApp

heroku container:release web --app minhaApp

heroku open --app minhaApp
```

OBS: A aplicação não irá executar na porta 80, o Heroku escolhe uma porta para a sua aplicação executar. Por isso nos arquivos `conf` do Apache usamos a variável de ambiente `${PORT}`.
