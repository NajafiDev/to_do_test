from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.tasks),
    path('tasks/<int:id>/', views.task_detail, name='task_list'),
]
