from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout

from entries.models import *

def index(request):

    return HttpResponseRedirect('/accounts/login')

def logout(requet):
    logout(request)

def welcome(request):
    list_post = Posts.objects.all()
    return render(request, 'interface/welcome.html', {
        'list_post':list_post
    })

def mypost(request, user_id):
    list_post = Posts.objects.filter(user=user_id)
    return render(request, 'interface/manange.html', {
        'list_post':list_post
    })

def newpost(request):
    if request.method == 'GET':
        return render(request, 'interface/newpost.html')
    else:
        title = request.POST['title']
        text = request.POST['text']
        user = User.objects.get(id=request.POST['userid'])

        npost = Posts(user=user, title=title, text=text)
        npost.save()

        return redirect('interface:welcome')

def edit(request, item_id):
    item = Posts.objects.get(id=item_id)
    if request.method == 'GET':
        return render(request, 'interface/edit.html', {
            'item':item
        })
    else:
        item.title = request.POST['title']
        item.text = request.POST['text']

        item.save()

        return redirect('interface:welcome')

def erase(request, item_id):
    Posts.objects.filter(id=item_id).delete()
    return redirect('interface:welcome')

def post(request, item_id):
    item = Posts.objects.get(id=item_id)
    return render(request, 'interface/view.html', {
        'item': item
    })    