from django import apps
from django.contrib import admin
from django.urls import path
from .views import index, item_id

app_name = 'myapp'
urlpatterns = [
    path('hello/', index, name='index'),
    path('hello/<int:my_id>/', item_id, name='item_id'),
]
