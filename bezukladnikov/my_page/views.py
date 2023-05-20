from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

COUNT_PROJECT = 5
def index(request):
    return HttpResponse("Главная страница биографии обо мне")

def project(request, proj_id):
    if proj_id < 1 or proj_id > COUNT_PROJECT:
        return redirect('home', permanent=False)
    return HttpResponse(f"<h1>Мои проекты</h1><p>Проект номер {proj_id}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")
