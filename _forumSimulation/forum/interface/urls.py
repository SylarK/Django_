from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('welcome/', views.welcome, name='welcome'),
    path('new/', views.newpost, name='newpost'),
    path('my/<int:user_id>', views.mypost, name='mypost')
]