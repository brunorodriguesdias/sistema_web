<h1 align="center">Sistema Web</h1>

<h2>🎯 Objetivo</h2>

<h2>Bem vindo!</h2>
Obrigado por conferir este projeto, nele estamamos desenvolvendo um sistema web integrando back e front end.<br>
Na parte do back-end busquei começar meu aprendizado no framework django para intergrar com a parte de front-end<br>
E ligar esse sistema com um banco de dados que fica hospedado na nuvem<br>
No que diz respeito ao front end, Davi buscou ...<br>

<h2>O projeto</h2>
Neste projeto estamos desenvolvendo inicialmente um sistema de cadastro, aonde integramos front-end que utiliza HTML, CSS e Javascript,<br>
com o back-end que utiliza Python e o framework Django, e também utilizamos o Mysql para criação do banco de dados e hospedamos utilizando o heroku<br>
No planejamento deste sistema, projetamos a tela inicial que seria o login, cadastro e dashboard.<br>
Na tela de login, utilizamos autenticação do Django para fazer a consulta do cadastro do usuário,<br>
Verificando se os dados inseridos conferem com os dados que estão no banco de dados e assim conceder acesso ao sistema.<br>
Na tela de cadastro, criamos verificações para conferir os dados do usuário, restringindo a duplicação de cpf e e-mail no banco, <br>
Verificando se o cpf é válido, veficação se as senhas estão iguais <br>
Neste projeto comecei a aprender como funciona o django, aprendi sobre views, models, a classe User,<br> 
A função migrate que integra com o database e a criar e organizar apps e integrar os arquivos de front-end.


<h2>🔧 Instalação</h2>

- Realizar o git clone
- Instalar o [Python 3.8.5](https://www.python.org/downloads/release/python-385/ "Python 3.8.5")
- Executar os seguintes comandos:
```
python -m venv ./venv
venv/Scripts/Activate
pip install django python-dotenv mysqlclient validate_docbr

```
- Criar arquivo .env no diretório principal
- Executar os seguintes comandos:
```
python manage.py runserver
```
