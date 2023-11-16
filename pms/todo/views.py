from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserSearchForm
from .models import Group, UserProfile
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User, Group, Permission 
from .forms import CreateUserForm, LoginForm, CreateTaskForm, UpdateUserForm
from django.contrib.auth.models import Permission
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Task
from django.contrib import messages 

    

def home(request):
    
   
    
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User registraion was successful!")
            return redirect("my-login")  
    else:
        form = CreateUserForm()
    
    return render(request, 'register.html', {'form': form})
        
         
    

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
def profile_management(request):
    
    if request.method == 'POST':
        
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            
            user_form.save()
            
            return redirect('dashboard')
      
    user_form = UpdateUserForm(instance=request.user)
            
    context = {'user_form': user_form}
     
    return render(request, 'profile/profile-management.html', context=context)       

@login_required(login_url='my-login')
def deleteAccount(request):
    if request.method == 'POST':
        
        
        deleteUser = User.objects.get(username=request.user)
        
        deleteUser.delete()
        
        return redirect('')
    
    return render(request, 'profile/delete-account.html')



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

def create_task(request):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            form.save_m2m()  
            
            return redirect('profile/view-tasks')
    else:
        form = CreateTaskForm()
    return render(request, 'proifle/view-tasks.html', {'form': form}) 
   
                 


@login_required(login_url='my-login')
def viewTask(request):
    current_user = request.user.id
    tasks = Task.objects.filter(created_by=current_user)
    context = {'tasks': tasks}
    
    return render(request, 'profile/view-tasks.html', context=context)
    
    
    
@login_required(login_url='my-login')
def updateTask(request, pk):
    
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


def create_groups(request):
    group1, created = Group.objects.get_or_create(name='Task Managers')
    group2, created = Group.objects.get_or_create(name='Admins')

    task_permissions = Permission.objects.filter(content_type__app_label='todo', codename__startswith='can_')
    group1.permissions.add(*task_permissions)
    
    return render(request, 'profile/create_groups.html')
    



def user_search(request):
    if request.method == 'POST':
        form = UserSearchForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            print(f"Search Query: {username}")
            users = User.objects.filter(username__icontains=username)
            print(f"Number of Users Found: {users.count()}")
            return render(request, 'profile/user_search_results.html', {'users': users})
    else:
        form = UserSearchForm()
    return render(request, 'profile/user_search.html', {'form': form})




def user_search_results(request):
    
    return render(request, 'profile/user_search_results.html')

   
    
def display_groups(request):
    groups = Group.objects.all()
    return render(request, 'profile/groups.html', {'groups': groups})

@login_required(login_url='my-login')  
def edit_group(request, group_id):
    try:
        group = Group.objects.get(id=group_id)
    except Group.DoesNotExist:
        messages.error

