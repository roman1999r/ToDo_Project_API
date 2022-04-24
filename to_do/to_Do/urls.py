from django.contrib import admin
from django.urls import path, include
from to_Do.views import *
from rest_framework.authtoken.views import obtain_auth_token


app_name = 'toDo'
urlpatterns = [
    path('auth/token', obtain_auth_token, name='token'),
    path('create/', ToDoCreateView.as_view(), name='create_items'),
    path('all/', ToDoListView.as_view(), name='all_items'),
    path('item/detail/<int:pk>/', ToDoDetailView.as_view(), name='detail_item'),
]
