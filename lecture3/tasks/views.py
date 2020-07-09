from django.shortcuts import render
from django import forms

tasks = ['boo', 'tee', 'bah', 'mozzie', 'pepper', 'folk', 'booster']

class NewTaskForm(forms.Form)    

# Create your views here.

def index(request):  
    return render(request, "tasks/index.html", {
        "tasks":tasks

    })

def add(request):

    return render(request, "tasks/add.html")

    