from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from usuarios.models import Usuario
from django.contrib import messages
from django.contrib import auth

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        e_mail = request.POST['email']
        senha = request.POST['senha']
        confirma_senha = request.POST['senha-confirme']
        
        if not nome.strip():
            messages.info(request, 'Nome inválido, tente novamente!')
            return redirect('cadastro')
        if not e_mail.strip():
            messages.info(request, 'E-mail inválido, tente novamente!')
            return redirect('cadastro')
        if not senha.strip():
            messages.info(request, 'Senha inválida, tente novamente!')
            return redirect('cadastro')
        if senha != confirma_senha:
            messages.info(request, 'Senhas divergentes, tente novamente')
            return redirect('cadastro')
        if User.objects.filter(email=e_mail).exists():
            messages.info(request, 'E-mail já cadastrado!')
            return redirect('cadastro')

        usuario = User.objects.create_user(username=nome, email=e_mail, password=senha)

        c_p_f = request.POST['cpf']
        telefone = request.POST['celular']

        if not c_p_f.strip():
            messages.info(request, 'CPF inválido, tente novamente!')
            return redirect('cadastro')
        if Usuario.objects.filter(cpf=c_p_f).exists():
            messages.info(request, 'CPF já cadastrado!')
            return redirect('cadastro')

        usuario2 = Usuario(cpf=c_p_f, celular=telefone)

        usuario2.usuario=usuario

        usuario.save()
        usuario2.save()
        messages.info(request, 'Cadastro realizado com sucesso!')
        return redirect('login')
    return render(request, 'galeria/cadastro.html')

def login(request):
    if request.method == 'POST':
        e_mail = request.POST['email']
        senha = request.POST['senha']
        if User.objects.filter(email=e_mail).exists():
            nome = User.objects.filter(email=e_mail).values_list('username', flat=True).get()
            usuario = auth.authenticate(request, username=nome, password=senha)
            if usuario is not None:
                auth.login(request, usuario)
                return redirect('dashboard')

            else:
                messages.info(request, 'Usuário e/ou senha incorretos, tente novamente!')
                return redirect('login')
        
    return render (request, 'galeria/login.html')


def dashboard(request):
    return render(request, 'galeria/dashboard.html')
