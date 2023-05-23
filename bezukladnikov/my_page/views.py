from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


from .models import Project, Category

COUNT_PROJECT = 5
# menu = ["About me", "Experience", "My project", "Contacts"]

menu = [{'title': "О сайте", 'url_name': "about"},
        {'title': "Добавить статью", 'url_name': "add_page"},
        {'title': "Обратная связь", 'url_name': "contact"},
        {'title': "Войти", 'url_name': "login"}
]



def index(request):
    posts = Project.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
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
    posts = Project.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }

    return render(request, 'my_page/index.html', context=context)


def all_project(request):
    projects = Project.objects.all()
    return render(request, 'my_page/project.html', {'projects': projects, 'menu': menu, 'title': 'My project'})

def project(request, proj_id):
    if proj_id < 1 or proj_id > COUNT_PROJECT:
        return redirect('home', permanent=False)
    return HttpResponse(f"<h1>Мои проекты</h1><p>Проект номер {proj_id}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")
