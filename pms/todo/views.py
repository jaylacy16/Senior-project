from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task 

from .forms import TaskForm, CreateUserForm, LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login


    

def home(request):
    
   
    
    return render(request, 'index.html')



def register(request):
    
    return render(request, 'register.html')

def my_login(request):
    
    return render(request, 'my-login.html')

def createTask(request):
    
    form = TaskForm()
    
    if request.method == 'POST':
        
        form = TaskForm(request.POST)
        
        if form.is_valid():
           
            form.save()

            return redirect('view-tasks')
        
    context = {'form': form}
    
    
    return render(request, 'create-task.html', context=context)


def viewTasks(request):
    
    tasks = Task.objects.all()
    
    context = {'tasks': tasks}
    
    
    return render(request, 'view-tasks.html', context=context)



def updateTask(request, pk):
    
    task = Task.objects.get(id=pk)
    
    form = TaskForm(instance=task)
    
    if request.method == 'POST':
        
        form = TaskForm(request.POST, instance=task)
    
        if form.is_valid():
            
            form.save()
            
            return redirect('view-tasks')
    
    context = {'form': form}
    
    return render(request, 'update-task.html', context=context)


def deleteTask(request, pk):
    
    task = Task.objects.get(id=pk)
    
    if request.method == 'POST':
        
        task.delete()
        
        return redirect('view-tasks')
    
    return render(request, 'delete-task.html')

    
    
    
    
    
    
    
    
    
    
    
def register(request):
        
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            return HttpResponse("Your account has been created!")
    
    context ={'form':form}
    
    return render(request, 'register.html', context=context)
        
         
    

def my_login(request):
    
    form = LoginForm
    
    if request.method == 'POST':
    
        form = LoginForm(request, data=request.POST)
    
        if form.is_valid():
        
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            
            if user is not None:
                
                auth.login(request, user)
                
                return HttpResponse("You have successfully logged in!")
            
    context = {'form': form}
    
    return render(request, 'my-login.html', context=context)
                