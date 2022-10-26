from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from models import Usuario

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        e_mail = request.POST['email']
        senha = request.POST['senha']
        confirma_senha = request.POST['senha-confirme']
        
        """if not nome.strip():
            return redirect('cadastro')
        if not e_mail.strip():
            return redirect('cadastro')
        if senha != confirma_senha:
            return redirect('cadastro')
        if User.objects.filter(email=e_mail).exists():
            return redirect('cadastro')

        user = User.objects.create_user(username=nome, email=e_mail, password=senha)

        id_usuario = User.objects.get(username=usuario)

        c_p_f = request.POST['cpf']
        telefone = request.POST['celular']

        usuario = Usuario(
            cpf=c_p_f,
            celular=telefone
        )
        

        user = User.objects.create_user(username=nome, email=e_mail, password=senha)"""
        
        
        
        

    """return redirect('login')"""

def login(request):
    return render (request, 'galeria/login.html')
