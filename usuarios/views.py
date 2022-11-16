from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from usuarios.models import Usuario
from django.contrib import messages
from django.contrib import auth
from validate_docbr import CPF

cPf = CPF()

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        e_mail = request.POST['email']
        senha = request.POST['senha']
        confirma_senha = request.POST['senha-confirme']
        
        if not nome.strip():
            messages.error(request, 'Nome inválido, tente novamente!')
            return redirect('cadastro')
        if not e_mail.strip():
            messages.error(request, 'E-mail inválido, tente novamente!')
            return redirect('cadastro')
        if not senha.strip():
            messages.error(request, 'Senha inválida, tente novamente!')
            return redirect('cadastro')
        if senha != confirma_senha:
            messages.error(request, 'Senhas divergentes, tente novamente')
            return redirect('cadastro')
        if User.objects.filter(email=e_mail).exists():
            messages.error(request, 'E-mail já cadastrado!')
            return redirect('cadastro')

        c_p_f = request.POST['cpf']
        telefone = request.POST['celular']

        if not c_p_f.strip():
            messages.error(request, 'CPF inválido, tente novamente!')
            return redirect('cadastro')
        if cPf.validate(c_p_f) is False:
            messages.error(request, 'CPF inválido, tente novamente!')
            return redirect('cadastro')
        if Usuario.objects.filter(cpf=c_p_f).exists():
            messages.error(request, 'CPF já cadastrado!')
            return redirect('cadastro')

        usuario = User.objects.create_user(username=nome, email=e_mail, password=senha)

        usuario2 = Usuario(cpf=c_p_f, celular=telefone)

        usuario2.usuario=usuario

        usuario.save()
        usuario2.save()
        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect('index')
    return render(request, 'galeria/cadastro.html')


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'galeria/dashboard.html')
    else:
        return redirect('index')

def logout(request):
    auth.logout(request)
    return render(request, 'galeria/index.html')

def criar_receita(request):
    if request.user.is_authenticated:
        return render(request, 'galeria/criar_receita.html')
    else:
        return redirect('index')

def receita(request):
    if request.user.is_authenticated:
        return render(request, 'galeria/receita.html')
    else:
        return redirect('index')
