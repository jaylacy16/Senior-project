
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django import forms
from .models import Task



        
class CreateUserForm(UserCreationForm):
    
    class Meta:
        
        model = User
        fields =['username', 'email', 'password1', 'password2']
        
class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    
        
class UserSearchForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description','assigned_to','due_date']
        
        
        






















