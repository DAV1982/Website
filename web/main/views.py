from django.shortcuts import render
from django.http import HttpResponse
from . models import Task

def index(request):
    task = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница', 'tasks': 'title', 'level': 'title'})

def about(request):
    return render(request, 'main/about.html')






