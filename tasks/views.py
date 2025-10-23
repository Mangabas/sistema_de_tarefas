import django
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
)
from .models import Task

def search_tasks(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        tasks = Task.objects.filter(user=request.user, title__icontains=search).order_by('-completed', 'created_at')
        return render(request, 'tasklist.html', {'tasks': tasks})


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

def login(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        
        if user is not None:
            auth_login(request, user)
            return redirect('list')
        else:
            return HttpResponse("Credenciais invalidas.")

def logout(request):
    auth_logout(request)  
    return redirect('list')

@login_required
def toggle(request, pk):
    if request.method == 'POST':
        task = Task.objects.filter(user=request.user, pk=pk).first()
        if task:
            task.completed = not task.completed
            task.save()
    return redirect('list')

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasklist.html'
    paginate_by = 5

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('-completed', 'created_at')
        
        

class DetailTask(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'detailtask.html'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class CreateTask(LoginRequiredMixin, CreateView):
    
    def get(self, request):
        return render(request, 'createtask.html')

    def post(self, request):
        title = request.POST.get('title')
        description = request.POST.get('description')

        task = Task.objects.create(
            title=title,
            description=description,
            user=request.user
        )
        task.save()

        return redirect('list')

class UpdateTask(LoginRequiredMixin, UpdateView):
    
    def get(self, request, pk):
        task = Task.objects.filter(user=request.user, pk=pk).first()
        if task:
            return render(request, 'updatetask.html', {'task': task})
        return redirect('list')

    def post(self, request, pk):
        title = request.POST.get('title')
        description = request.POST.get('description')

        task = Task.objects.filter(user=request.user, pk=pk).first()
        if task:
            task.title = title
            task.description = description
            task.save()

        return redirect('list')
    
class DeleteTask(LoginRequiredMixin, DeleteView):

    def post(self, request, pk):
        task = Task.objects.filter(user=request.user, pk=pk).first()
        if task:
            task.delete()
        return redirect('list')


    

