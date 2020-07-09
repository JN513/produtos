from django.shortcuts import render, redirect

def index(request):
    return render(request ,'index.html')

def cadastro(request):
    if request.method == 'POST':
        print(' Deu certo')
        return redirect('login')
        
    return render(request ,'cadastro.html')

def login(request):
    return render(request ,'login.html')

def logout(request):
    return render(request ,'logout.html')

def dashboard(request):
    return render(request ,'dashboard.html')
