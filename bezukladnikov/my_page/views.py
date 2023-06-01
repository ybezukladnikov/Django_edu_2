from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
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
    return render(request, 'my_page/index.html', context=context)  # Джанго сам найдет путь по настройкам в settings


def about(request):
    return render(request, 'my_page/about.html', {'menu': menu, 'title': 'About site'})


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES) # Формируется форма с заполенными данными и получение фото.
        if form.is_valid():
            form.save()  # это сохранение если форма связанa c базой данных

            '''
            если форма не связа с базой данный:
            try:
                SportsGround.objects.create(**form.cleaned_data) 
                return redirect('home')
            except:
                form.add_error(None, 'Error adding post')
            '''

            # print(form.cleaned_data) # просто выведит в консоль данные, которые были введены в форму
                                        # если они корректны.
            return redirect('home')
    else:
        form = AddPostForm() # Формируется пустая форма
    return render(request, 'my_page/addpage.html', {'form': form, 'menu': menu, 'title': 'Add page'})


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_sports_ground(request, SportsGround_slug):
    sports_ground = get_object_or_404(SportsGround, slug=SportsGround_slug)

    context = {
        'sports_ground': sports_ground,
        'menu': menu,
        'title': sports_ground.title,
        #     Я бы закомментировал cat_selected. Потому что
        #     если этого не сделать, то если я захочу после выбора площадки ознакомитсья
        # со всеми площадками города к которой относится выбранная площадка я этого сделать
        # уже не смогу. Потому город станет простым текстом, а не ссылкой.
        'cat_selected': sports_ground.city_id,
    }
    return render(request, 'my_page/SportsGround.html', context=context)


def show_category(request, cat_slug):
    city_obj = City.objects.filter(slug=cat_slug)
    city_id = city_obj[0].pk
    posts = SportsGround.objects.filter(city=city_id).filter(is_published=1)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Grounds in cities',
        'cat_selected': city_id,
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
