from django.shortcuts import render, redirect

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        print(nome)
        return redirect('login')
    else:
        return render(request, 'galeria/cadastro.html')
    

def login(request):
    return render (request, 'galeria/login.html')
