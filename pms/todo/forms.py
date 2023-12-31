
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django import forms
from .models import Task, Profile
from django import forms
from .models import Message


        
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
        fields = ['title', 'context','due_date','user','assigned_to']
        
        
        
class UpdateUserForm(forms.ModelForm): 
    
    password = None
    
    class Meta:
        
        model = User
        fields = ['username', 'email',]
        exclude = ['password1', 'password2',]
        
class UpdateProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-file'}))
    class Meta:
         model = Profile
         fields = ['profile_pic',]



class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content', 'receiver']  

    def __init__(self, *args, **kwargs):
        sender = kwargs.pop('user', None)
        super(SendMessageForm, self).__init__(*args, **kwargs)
        if sender:
           
            self.fields['receiver'].queryset = User.objects.exclude(username=sender.username)



















