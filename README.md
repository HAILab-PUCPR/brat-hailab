# Brat - rapid annotation tool

Neste repositório você encontra os arquivos Docker necessários para executar a ferramenta *Brat* em containers e executar localmente ou em servidres como Heroku e Google Cloud.

*Brat - Brat Rapid Annotation Tool* é uma aplicação online para anotação colaborativa de corpus.

Para documentação da ferramenta, acesse:

- [brat homepage][brat]
- [brat_github][brat_github]

Exemplos:

<img src="https://brat.nlplab.org/img/examples/esp.train-doc-536-small.png">
<img src="https://brat.nlplab.org/img/examples/swedish_talbanken05_train.conll-doc-880-small.png">
<img src="https://brat.nlplab.org/img/examples/TDT-w078-small.png">
<img src="https://brat.nlplab.org/img/examples/MLEE-PMID-15975645-small.png">

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


Ou, se desejar executá-la diretamente da nossa [imagem](https://hub.docker.com/repository/docker/terumi/hailab-brat):

	$ docker run --name brat_instance -p 80:80 -d terumi/hailab-brat:V3

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
OBS: Para persistir os arquivos gravados mesmo após parar o container, você provavelmente precisará definir um volume. Para isso, crie uma pasta chamada `data` e execute o container dessa maneira :

```
$ docker run --name=brat_instance -p 80:80 -v data:/var/www/brat/brat-v1.3_Crunchy_Frog/data/ -d brat 
```

Ou, se estiver usando `docker-compose`. poderá definir assim:

```
 brat:
        build: ./brat
        container_name: brat_instance
        restart: unless-stopped
        tty: true
        ports:
            - "80:80"
        volumes:
            - ./data:/var/www/brat/brat-v1.3_Crunchy_Frog/data/

```
Onde na pasta `brat` está o seu `Dockerfile`.


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

*Atenção: Ao subir a aplicação no Heroku, não há a garantia de que os arquivos persistidos serão mantidos atualizados no servidor. Caso queria criar um trabalho de anotação, por favor verifique uma maneira de gravar os dados anotados em um bucket ou algo assim, para não perder as anotações realizadas a cada re-deploy ou alteração de dyno.*

#### Para executar o container no Google Cloud:

Primeiro vamos gerar a imagem e subir para o Google Cloud. Para isso, instale o [Google CLI](https://cloud.google.com/sdk/docs/install?hl=pt-br) e faça o login:

```
gcloud auth login
```

Agora, supondo que você já fez o build na sua máquina local (de nome `brat`), conforme explicado anteriormente, vamos tagear a nossa imagem. Você precisa ter um projeto já criado no Console do Google.

```
docker tag brat gcr.io/brat-hailab-351613/brat
```
Agora vamos enviar a imagem:

```
docker push gcr.io/brat-hailab-351613/brat
```

No seu console do Google, a imagem irá aparecer em *Container Registry*. Selecione a imagem e clique em *Implantar*. O sistema irá implantar a sua imagem e te fornecer uma URL para que você acesse a aplicação.

OBS: cuidado para não ultrapassar a cota gratuita do Google Cloud. Hoje esse valor é de 50 horas semanais, então quando não for mais utilizar (ex de madrugada), vá em *APIs e serviços* e clique em *Desativar API*.


<a href="https://www.buymeacoffee.com/lisaterumi"><img src="https://raw.githubusercontent.com/lisaterumi/lisaterumi/main/bymeacoffe_mini.png" width="200"></a>

