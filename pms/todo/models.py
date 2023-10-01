# todo/models.py
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_to = models.ManyToManyField(User, related_name='assigned_tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)

class Group(models.Model):
    name = models.CharField(max_length=100)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    groups = models.ManyToManyField(Group, related_name='members')


    
    
    
