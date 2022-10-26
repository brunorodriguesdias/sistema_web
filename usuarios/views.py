from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from usuarios.models import Usuario

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        e_mail = request.POST['email']
        senha = request.POST['senha']
        confirma_senha = request.POST['senha-confirme']
        
        if not nome.strip():
            return redirect('cadastro')
        if senha != confirma_senha:
            return redirect('cadastro')
        if User.objects.filter(email=e_mail).exists():
            return redirect('cadastro')

        usuario = User.objects.create_user(username=nome, email=e_mail, password=senha)

        c_p_f = request.POST['cpf']
        telefone = request.POST['celular']

        if Usuario.objects.filter(cpf=c_p_f).exists():
            return redirect('cadastro')

        usuario2 = Usuario(cpf=c_p_f, celular=telefone)

        usuario2.usuario=usuario

        usuario.save()
        usuario2.save()
        
        return redirect('login')
    return render(request, 'galeria/cadastro.html')

def login(request):
    return render (request, 'galeria/login.html')
