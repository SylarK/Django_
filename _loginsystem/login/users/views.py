from django.shortcuts import render, redirect
from django.urls import reverse

from users.models import Usuario

# Create your views here.

def index(request):
    return render(request, 'users/index.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'users/register.html')
    else:

        username = request.POST['username']
        password = request.POST['password']

        user_add = Usuario()
        user_add.name = username
        user_add.password = password
        user_add.email = 'default@local.br'
        user_add.save()

        return render(request, 'users/login.html', {
            'user_add':user_add
        })

def login(request):

    if request.method == 'GET':
        return render(request, 'users/login.html', {
            'msg': 'You must the write your username and password'
        })

    else: 
        username = request.POST['username']
        password = request.POST['password']
        if Usuario.objects.get(name = username) && Usuario.objects.get()):
            user_add = Usuario.objects.get(name = username)
            return render(request, 'users/login.html', {
                'user_add':user_add
            })
        else:
            return render(request, 'users/login.html', {
                'msg':'Is something wrong.'
            })

    