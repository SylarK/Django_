from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

def index(request):
    return HttpResponseRedirect('/accounts/login')

def logout(requet):
    logout(request)

def welcome(request):
    return render(request, 'interface/welcome.html')

def mypost(request):
    return render(request, 'interface/manange.html')

def newpost(request):
    return render(request, 'interface/newpost.html')