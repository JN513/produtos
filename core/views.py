from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Categoria, Tipo, Produto

def index(request):
    return render(request ,'index.html')

def cadastro(request):

    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if not nome.strip():
            print('o nome não pode ficar em branco')
            return redirect('cadastro')
        elif not email.strip():
            print('o email não pode ficar em branco')
            return redirect('cadastro')
        elif password != password2:
            print('as senhas não coicidem')
            return redirect('cadastro')
        elif User.objects.filter(email = email).exists():
            print('Úsuario já cadastrado')
            return redirect('cadastro')

        user = User.objects.create_user(username=nome, email=email, password=password)
        user.save()
        print('Usuario cadastrado com sucesso')  
        return redirect('login')
    else:
        return render(request, 'cadastro.html')

    return render(request ,'cadastro.html')

def login(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if email == "" or password == "":
            print("Os campos email e senha não podem ficar em branco")
            return redirect('login')
        if User.objects.filter(email = email).exists():
            nome=User.objects.filter(email=email).values_list('username',flat=True).get()
            user = auth.authenticate(request, username=nome, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')

    return render(request ,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        produtos = Produto.objects.order_by('datadecriacao')
        return render(request ,'dashboard.html')
    else:
        return redirect('index')

def cria_produto(request):
    categorias = Categoria.objects.order_by('nome')
    tipos = Tipo.objects.order_by('nome')
    dados = {
        'categorias': categorias,
        'tipos':tipos,
    }

    if request.method == 'POST':
        nome = request.POST['nomeproduto']
        descricao = request.POST['descricao']
        preco = request.POST['preco']
        quantidade = request.POST['quantidade']
        datafa = request.POST['datadefabri']
        categoria2 = request.POST['categoria']
        tipos = request.POST['tipo']
        user = get_object_or_404(User, pk=request.user.id)
        
        produto = Produto(nome=nome, descricao=descricao,preco=preco,quantidade=quantidade,datadefabricacao=datafa,criador=user,categoria_id=categoria2)
        produto.save()
        return redirect('dashboard')

    return render(request, 'criaproduto.html', dados)

def cria_categoria(request):

    if request.method == 'POST':
        nome = request.POST['nome']
        if nome == "":
            print("O campo nome não pode ficar em branco")
            return redirect('cria_categoria')
        if Categoria.objects.filter(nome=nome).exists():
            print('A categoria já existe')
            return redirect('cria_categoria')
        novacategoria = Categoria(nome=nome)
        novacategoria.save()
        print('Categoria cadastrada com sucesso')  
        return redirect('dashboard')
    
    return render(request,'criacategorias.html')

def cria_tipo(request):
    categorias = Categoria.objects.order_by('nome')
    dados = {
        'categorias': categorias,
    }

    if request.method == 'POST':
        nome = request.POST['nome']
        categoria2 = request.POST['categoria']
        print(categoria2)
        if nome == "":
            print("O campo nome não pode ficar em branco")
            return redirect('cria_tipo')
        if Tipo.objects.filter(nome=nome).exists():
            print('Tipo já existente')
            return redirect('cria_tipo')
        novotipo = Tipo(nome=nome, categoriadotipo_id=categoria2)
        novotipo.save()
        print('Categoria cadastrada com sucesso')  
        return redirect('dashboard')

    return render(request,'criatipo.html',dados)
