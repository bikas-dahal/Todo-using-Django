from django.urls import path 

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.task_list, name='task_list'),
    path('<int:task_id>/', views.task_detail, name='task_detail'),
     path('task/<int:task_id>/edit/', views.edit_task, name='edit_task'),
    path('add/', views.add_task, name='add_task'),
    # path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('profile/', views.profile, name='profile'),
    
    path('today/', views.today_tasks, name='today_tasks'),
    path('upcoming/', views.upcoming_tasks, name='upcoming_tasks'),
    # path('completed/', views.completed_tasks, name='completed_tasks'),
    

]