from django.shortcuts import render, get_object_or_404, redirect #é renderizar
from apps.app.models import Fotografia #importo todos os objetos de models
from apps.app.forms import FotografiaForms
from django.contrib import messages
from django.contrib.auth.models import User

def index(request):
    if not request.user.is_authenticated: #para quando um usuário não estiver logado ou não tiver cadastro
        messages.error(request, 'Usuário não logado!')
        return redirect('login') 
    
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True) #coloquei uma lista com todos os objetos criados em model
    print('Carregando a página INDEX!')
    return render(request, 'funcionalidades/index.html', {"cards": fotografias}) #modifico para passar o html e a view renderiza o código

def imagem(request, foto_id): #função view
    print('Carregando a página IMAGEM!')
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'funcionalidades/imagem.html', {"fotografia": fotografia})

def buscar(request): #3- Busca os itens do banco de dados
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado!')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True) 
    
    #4- Filtra os dados de acordo com a busca
    if "buscar" in request.GET: #verifico se as informações estão no request do usuário
        nome_a_buscar = request.GET['buscar'] #Guardo as informações do request do usuário (o que ele digitou para a procura) 
        if nome_a_buscar: #se existir alguma busca
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar) #busca se existe dentro do nome a buscar alguma semelhança com algum item dentro do site
    
    #5- Passa para o render
    return render(request, "funcionalidades/index.html", {"cards":fotografias}) 

def nova_imagem(request):
    if not request.user.is_authenticated: #para quando um usuário não estiver logado ou não tiver cadastro
        messages.error(request, 'Usuário não logado!')
        return redirect('login')
    form = FotografiaForms
    if request.method == 'POST':#para que as informações deixadas pelo usuário sejam salvas no banco de dados:
        form = FotografiaForms(request.POST, request.FILES) #passo as informações
        #validando o formulário
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova fotografia cadastrada!')
            return redirect('index')
            
    return render(request, 'funcionalidades/nova_imagem.html', {'form':form})

def editar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)
    
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia editada com sucesso!')
            return redirect('index')
    
    return render(request, 'funcionalidades/editar_imagem.html', {'form':form, 'foto_id':foto_id})

def deletar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Deleção feita com sucesso!')
    return redirect('index')

def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True, categoria=categoria)
    return render(request, 'funcionalidades/index.html', {"cards":fotografias})