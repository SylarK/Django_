from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from users.models import Produto

def index(request):
    list_view = Produto.objects.all()
    return render(request, 'users/index.html', {
        'list_view':list_view
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            #Salvando no banco de dados
            form.save()
            #Realizando a autenticação e redirecionando para o index
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    else:    
        form = UserCreationForm()

    return render(request, 'registration/register.html', {
        'form': form
    })

def add(request):
    if request.method == 'POST':

        name = request.POST['name_product']
        value = request.POST['value_product']
        validate = request.POST['validate_product']
        img = request.POST['url_img_product']

        newProduct = Produto(name=name, value=value, validate=validate, img=img)
        newProduct.save()
        return redirect('index')

    else:    
        return render(request, 'users/add.html', {
            'msg':'Please, write the informations about the product and press "Add"'
        })

def erase(request, produto_id):
    
    Produto.objects.get(id=produto_id).delete()

    return redirect('index')

def edit(request, produto_id):

    if request.method == 'POST':

        name = request.POST['name_product']
        value = request.POST['value_product']
        validate = request.POST['validate_product']
        img = request.POST['url_img_product']

        editProduct = Produto(name=name, value=value, validate=validate, img=img)
        editProduct.save()

        return redirect('index')
    
    else:

        product = Produto.objects.get(id=produto_id)

        return render(request, 'users/edit.html', {'product':product})