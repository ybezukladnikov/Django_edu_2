from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


from .models import SportsGround, City

COUNT_PROJECT = 5


menu = [{'title': "About", 'url_name': "about"},
        {'title': "Add Sport Ground", 'url_name': "add_page"},
        {'title': "Feedback", 'url_name': "contact"},
        {'title': "Sign in", 'url_name': "login"}
]



def index(request):
    # posts = SportsGround.objects.all()
    posts = SportsGround.objects.all().filter(is_published=1)
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Main page',
        'cat_selected': 0,
    }
    return render(request, 'my_page/index.html', context=context) # Джанго сам найдет путь по настройкам в settings

def about(request):
    return render(request, 'my_page/about.html', {'menu': menu, 'title': 'About site'})


def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id {post_id}")

def show_category(request, cat_id):
    posts = SportsGround.objects.filter(city=cat_id).filter(is_published=1)


    if len(posts) is 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }

    return render(request, 'my_page/index.html', context=context)


def all_project(request):
    projects = SportsGround.objects.all()
    return render(request, 'my_page/project.html', {'projects': projects, 'menu': menu, 'title': 'My project'})

def project(request, proj_id):
    if proj_id < 1 or proj_id > COUNT_PROJECT:
        return redirect('home', permanent=False)
    return HttpResponse(f"<h1>Мои проекты</h1><p>Проект номер {proj_id}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")
