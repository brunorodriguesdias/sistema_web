from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

def index(request):
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
                messages.error(request, 'Usuário e/ou senha incorretos, tente novamente!')
                return redirect('index')
        
    return render (request, 'galeria/index.html')
