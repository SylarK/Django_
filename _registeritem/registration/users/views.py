from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login



def index(request):
    return render(request, 'users/index.html')

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
