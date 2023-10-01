from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserSearchForm
from .models import Group, UserProfile
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User, Group, Permission 
from .forms import CreateUserForm, LoginForm, CreateTaskForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required

from . models import Task

    

def home(request):
    
   
    
    return render(request, 'index.html')


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
                
                return redirect("dashboard")
   
    context = {'form': form}
    
    return render(request, 'my-login.html', context=context)
                
    
@login_required(login_url='my-login')
def dashboard(request):
    
   
     return render(request, 'profile/dashboard.html')  
 
 


@login_required(login_url='my-login')
def createTask(request):
    
    form = CreateTaskForm()
    
    if request.method == 'POST':
        
        form = CreateTaskForm(request.POST)
        
        if form.is_valid():
            
            task = form.save(commit=False)
            
            task.user = request.user
            
            
            task.save()
            
            return redirect('view-tasks')

    context = {'form': form}

    return render(request,'profile/create-task.html', context=context)    
   
                 


@login_required(login_url='my-login')
def viewTask(request):
    
    current_user = request.user.id
    task = Task.objects.all().filter(user=current_user)
    
    context = {'task': task}
    
    return render(request, 'profile/view-tasks.html', context=context)
    
    
    
@login_required(login_url='my-login')
def updateTask(request,pk):
    
    task = Task.objects.get(id=pk)
    
    form = CreateTaskForm(instance=task)
    
    if request.method == 'POST':
        
        form = CreateTaskForm(request.POST, instance=task)
        
        if form.is_valid():
           
            form.save()
            
            return redirect('view-tasks')
        
    context = {'form': form}
    
    return render(request,'profile/update-task.html', context=context) 




def deleteTask(request, pk):
    
    task = Task.objects.get(id=pk)
    
    if request.method =='POST':
        
        task.delete()
        
        return redirect('view-tasks')
    
    
    return render(request, 'profile/delete-task.html')
    
    
    
    
    

                
def user_logout(request):
    
    auth.logout(request)
    
    return redirect("")                 


def create_groups():
    group1, created = Group.objects.get_or_create(name='Task Managers')
    group2, created = Group.objects.get_or_create(name='Admins')

    task_permissions = Permission.objects.filter(content_type__app_label='todo', codename__startswith='can_')
    group1.permissions.add(*task_permissions)
    
    
create_groups()


def user_search(request):
    if request.method == 'POST':
        form = UserSearchForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            users = User.objects.filter(username__icontains=username)
            return render(request, 'user_search_results.html', {'users': users})
    else:
        form = UserSearchForm()
    return render(request, 'user_search.html', {'form': form})


def create_task(request):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            form.save_m2m()  
            return redirect('task_list')
    else:
        form = CreateTaskForm()
    return render(request, 'create-task.html', {'form': form})



def user_search_results(request):
    
    return render(request, 'user_search_results.html')
    