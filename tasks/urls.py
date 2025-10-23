from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', views.TaskList.as_view(), name='list'),
    path('task/<int:pk>/', views.DetailTask.as_view(), name='task_detail'),
    path('task/create/', views.CreateTask.as_view(), name='create_task'),
    path('task/<int:pk>/update/', views.UpdateTask.as_view(), name='update_task'),
    path('task/<int:pk>/delete/', views.DeleteTask.as_view(), name='delete_task'),
    path('task/<int:pk>/toggle/', views.toggle, name='toggle_task'),

]