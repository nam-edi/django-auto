from django.contrib import admin
from django.urls import path
import todo.views as views

urlpatterns = [
    path('', views.index, name="todo"),
    path('add-collection', views.add_collection, name="add-collection"),
    path('delete-collection', views.delete_collection, name="delete-collection"),
    path('add-task', views.add_task, name="add-task"),
    path('delete-task/<int:task_pk>/', views.delete_task, name="delete-task"),
    path('get-tasks/<int:collection_pk>/', views.get_tasks, name="get-tasks"),
    path('get-collection_detail/<int:collection_pk>/', views.get_collection_detail, name="get-collection-detail"),
]
