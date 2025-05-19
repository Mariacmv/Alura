from django.shortcuts import render, redirect

from apps.usuarios.forms import LoginForms, CadastroForms

from django.contrib.auth.models import User

from django.contrib import auth

from django.contrib import messages

def login(request):
    form = LoginForms() #instância da classe LoginForms
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()
        
        usuario = auth.authenticate(
            request,
            username = nome,
            password = senha
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f'{nome} logado com sucesso')
            return redirect('index')
        else:
            messages.error(request, 'Usuário não encontrado')
            return redirect('login')
    
    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    form = CadastroForms()
    
    if request.method == 'POST': #se o método de requisição for POST (dar uma pesquisada sobre), faça:
        form = CadastroForms(request.POST) #pego as informações do formulário
        if form.is_valid():
            # if form['senha1'].value() != form['senha2'].value():#puxo as informações passadas ao formulário e comparo com a senha 2 para verificação 
            #     messages.error(request, 'Senhas não correspondem!')
            #     return redirect('cadastro')
            nome = form["nome_cadastro"].value()
            email = form["email"].value()
            senha = form["senha1"].value()
            
            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já existe')
                return redirect('cadastro') 
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, 'Cadastro efetuado com sucesso')
            return redirect('login')
            
    return render(request, "usuarios/cadastro.html", {"form": form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')