from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse(f"Usuario {username} ja existe!")

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return HttpResponse(f"Usuario {username} criado com sucesso!")

@login_required
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            return HttpResponse("Credenciais invalidas.")

def logout(request):
    auth_logout(request)  
    return redirect('index')
