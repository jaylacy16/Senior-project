
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    context = models.CharField(max_length=100, default='')
    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)
    due_date = models.DateTimeField()
    assigned_to = models.ManyToManyField(User, related_name='assigned_tasks')
    due_date = models.DateField(null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)
   
    

class Group(models.Model):
    name = models.CharField(max_length=100)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    groups = models.ManyToManyField(Group, related_name='members')


class Profile(models.Model):
    
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/", default='default.jpg')
    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)
    
    
    
