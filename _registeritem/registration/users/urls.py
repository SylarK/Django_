from django.urls import path, include

from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('add/', views.add, name='add'),
    path('erase/<int:produto_id>', views.erase, name='erase'),
    path('edit/<int:produto_id>', views.edit, name='edit')
    
]