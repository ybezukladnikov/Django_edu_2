from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Главная страница биографии обо мне")

def project(request):
    return HttpResponse("<h1>Мои проекты</h1>")
