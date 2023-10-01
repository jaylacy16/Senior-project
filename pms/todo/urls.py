
from django.urls import path

from . import views

urlpatterns = [
    
  
    path('', views.home, name=""),
    
    
    path('dashboard', views.dashboard, name="dashboard"),
    
    
    path('create-task', views.createTask, name="create-task"),
    
    
    path('view-tasks', views.viewTask, name="view-tasks"),
    
    path('update-task/<str:pk>/', views.updateTask, name="update-task"),
    
    
    path('delete-task/<str:pk>/', views.deleteTask, name="delete-task"),
    
    
    path('register', views.register, name="register"),
    
    
    path('my-login', views.my_login, name="my-login"),
    
    
    path('user-logout', views.user_logout, name="user-logout"),
    
    path('user_search', views.user_search, name='user_search'),
    
    path('user_search_results', views.user_search_results, name='user_search_results'),
    
    path('groups', views.create_groups, name='groups' ),
    
    
    
    ]