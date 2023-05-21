from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import Project

COUNT_PROJECT = 5
menu = ["About me", "Experience", "My project", "Contacts"]
def index(request):
    return render(request, 'my_page/index.html', {'menu': menu, 'title': 'Main page'}) # Джанго сам найдет путь по настройкам в settings

def about(request):
    return render(request, 'my_page/about.html', {'menu': menu, 'title': 'About site'})

def all_project(request):
    projects = Project.objects.all()
    return render(request, 'my_page/project.html', {'projects': projects, 'menu': menu, 'title': 'My project'})

def project(request, proj_id):
    if proj_id < 1 or proj_id > COUNT_PROJECT:
        return redirect('home', permanent=False)
    return HttpResponse(f"<h1>Мои проекты</h1><p>Проект номер {proj_id}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")
