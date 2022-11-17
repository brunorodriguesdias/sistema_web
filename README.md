<h1 align="center">Sistema Web</h1>

<h2>Bem vindo!</h2>

<h2>🚀 Descrição</h2>

<p> Neste projeto desenvolvemos um sistema de cadastro, integrando front-end (HTML, CSS e Javascript),
com o back-end que utiliza Python e o framework Django. Como banco de dados, utilizamos o MySQL, com hospedagem no Heroku.
</p>

Projetamos 2 telas: inicial/login e cadastro. 
- Na tela incial/login, utilizamos autenticação do Django para fazer a consulta do cadastro do usuário e assim conceder acesso ao sistema.
- Na tela de cadastro, as seguintes atividades foram realizadas:
  - Verificação dos dados do usuário;
  - Confirmação da senha digitada;
  - Impedimento da geração de CPFs e-mails duplicados no banco de dados.


<h2>🎯 Objetivo do projeto</h2>
<p><a href="https://github.com/brunorodriguesdias">Bruno Rodrigues Dias</a>: <br>Neste projeto comecei a aprender como funciona o Django, aprendi sobre views, models, a classe User, a função migrate que integra com o database e a criar e organizar apps e integrar os arquivos de front-end.</p>


<p><a href="https://github.com/davikennedy">Davi Kennedy</a>: <br>Neste projeto tive a oportunidade de trabalhar com o Bruno, onde pude aprender sobre como funciona a integração do front-end com o back-end do Python. Aprendi um pouco mais sobre a utilização de divs, forms, efeitos de transition, shadow e hover, além dos conceitos de responsividade que pude colocar em prática.</p>


<h2>🔧 Instalação</h2>

- Realizar o git clone
- Instalar o [Python 3.8.5](https://www.python.org/downloads/release/python-385/ "Python 3.8.5")
- Executar os seguintes comandos:
```
python -m venv ./venv
venv/Scripts/Activate
pip install django python-dotenv mysqlclient validate_docbr
mkdir .env
python manage.py runserver
```
