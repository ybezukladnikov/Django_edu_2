from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy


# чтобы закрыть доступ к странице нужно импортировать данный класс.
from django.contrib.auth.mixins import LoginRequiredMixin

# чтобы закрыть доступ к странице нужно в том случае если представление сделано через
# функуцию.
# то надо использовать декоратор login_required.

from .forms import *
from .models import SportsGround, City
from .utils import *

COUNT_PROJECT = 5




class MyPageHome(DataMixin, ListView):
    model = SportsGround
    template_name = 'my_page/index.html'
    context_object_name = 'posts' # Класс использует свою коллекцию данных и она называется object_list.
    # Но, так как у нас в index.html использутеся слово posts из старой функции, то нужно просто заменить
    # имя.
    # extra_context = {'title': 'Main page'} # но это только для передачи статической информации.
    # для динамической информации такой как список меню ввержу нужно уже использовать функцию.

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs) # сначала мы должны поднять к зазовому классу и забрать
        # все коллекции, которые уже сформированы. Такие как posts, title.

        # Если не создадвать класса Mixin, то надо прописать доп. атребуты.
        # context['menu'] = menu
        # context['cat_selected'] = 0

        # Это уже с классом Mixin:
        c_def = self.get_user_context(title="Main page")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        # select_related('city') Это жадный запрос.
        # это сделано, чтобы уменьшить количество SQL запросов к базе данных.
        # Что при отображении площадки на странице нам лишний раз не обращаться к базе
        # за названием категории.
        return SportsGround.objects.filter(is_published=True).select_related('city')

# def index(request):
#     # posts = SportsGround.objects.all()
#     posts = SportsGround.objects.all().filter(is_published=1)
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Main page',
#         'cat_selected': 0,
#     }
#     return render(request, 'my_page/index.html', context=context)  # Джанго сам найдет путь по настройкам в settings


def about(request):
    return render(request, 'my_page/about.html', {'menu': menu, 'title': 'About site'})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'my_page/addpage.html'
    # Джанго автоматическии через функцию get_url, которая прописана в модели.
    # Сформирует url для нового поста и перекинит меня туда. Но, если я хочу, чтобы после
    # добавления статьи меня перекидывало в определенное место нужно прописать следующий параметр:
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home') # если неавторизованный пользователь попытвается добавить
    # площадку его перекинет на главную страницу сайта.

    # так же можно сгенерить ошибку 403 доступ запрещен.
    # raise_exception = True
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs) # сначала мы должны поднять к зазовому классу и забрать
        # все коллекции, которые уже сформированы. Такие как posts, title.
        c_def = self.get_user_context(title="Add Page")
        return dict(list(context.items()) + list(c_def.items()))



# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES) # Формируется форма с заполенными данными и получение фото.
#         if form.is_valid():
#             form.save()  # это сохранение если форма связанa c базой данных
#
#             '''
#             если форма не связа с базой данный:
#             try:
#                 SportsGround.objects.create(**form.cleaned_data)
#                 return redirect('home')
#             except:
#                 form.add_error(None, 'Error adding post')
#             '''
#
#             # print(form.cleaned_data) # просто выведит в консоль данные, которые были введены в форму
#                                         # если они корректны.
#             return redirect('home')
#     else:
#         form = AddPostForm() # Формируется пустая форма
#     return render(request, 'my_page/addpage.html', {'form': form, 'menu': menu, 'title': 'Add page'})


def contact(request):
    return HttpResponse("Обратная связь")


# def login(request):
#     return HttpResponse("Авторизация")

class ShowSportsGround(DataMixin, DetailView):
    model = SportsGround
    template_name = 'my_page/SportsGround.html'
    slug_url_kwarg = 'SportsGround_slug' # в старых версиях Джанго имя бралось не из файла url, а
    # просто slug. Но в новых версиях эта проблема решена.
    context_object_name = 'sports_ground'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs) # сначала мы должны поднять к зазовому классу и забрать
        # все коллекции, которые уже сформированы. Такие как posts, title.
        # context['menu'] = menu
        # context['title'] = context['sports_ground']
        # return context

        c_def = self.get_user_context(title = context['sports_ground'])
        return dict(list(context.items()) + list(c_def.items()))


# def show_sports_ground(request, SportsGround_slug):
#     sports_ground = get_object_or_404(SportsGround, slug=SportsGround_slug)
#
#     context = {
#         'sports_ground': sports_ground,
#         'menu': menu,
#         'title': sports_ground.title,
#         #     Я бы закомментировал cat_selected. Потому что
#         #     если этого не сделать, то если я захочу после выбора площадки ознакомитсья
#         # со всеми площадками города к которой относится выбранная площадка я этого сделать
#         # уже не смогу. Потому город станет простым текстом, а не ссылкой.
#         'cat_selected': sports_ground.city_id,
#     }
#     return render(request, 'my_page/SportsGround.html', context=context)


class CityList(DataMixin, ListView):
    model = SportsGround
    template_name = 'my_page/index.html'
    context_object_name = 'posts'
    allow_empty = False # это как раз нам решит проблемы если нет площадок в выбраном городе.
                        # и будет формировать ошибка 404.

    def get_queryset(self):
        return SportsGround.objects.filter(city__slug=self.kwargs['cat_slug'], is_published=True).select_related('city')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs) # сначала мы должны поднять к зазовому классу и забрать
        # все коллекции, которые уже сформированы. Такие как posts, title.
        # context['menu'] = menu
        # context['title'] = 'City - ' + str(context['posts'][0].city) # очень опастно так делать. Потому что
        #                         # если не будет плащадок в опеделенном городе, мы получим ошибку.
        #
        # context['cat_selected'] = context['posts'][0].city_id
        c_def = self.get_user_context(title='City - ' + str(context['posts'][0].city),
                                      cat_selected=context['posts'][0].city_id)

        return dict(list(context.items()) + list(c_def.items()))

# def show_category(request, cat_slug):
#     city_obj = City.objects.filter(slug=cat_slug)
#     city_id = city_obj[0].pk
#     posts = SportsGround.objects.filter(city=city_id).filter(is_published=1)
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Grounds in cities',
#         'cat_selected': city_id,
#     }

    # return render(request, 'my_page/index.html', context=context)


def all_project(request):
    projects = SportsGround.objects.all()
    return render(request, 'my_page/project.html', {'projects': projects, 'menu': menu, 'title': 'My project'})


def project(request, proj_id):
    if proj_id < 1 or proj_id > COUNT_PROJECT:
        return redirect('home', permanent=False)
    return HttpResponse(f"<h1>Мои проекты</h1><p>Проект номер {proj_id}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'my_page/register.html'
    success_url = reverse_lazy('login') # ссылка на url при успешной регистрации пользователя.

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Sign up")
        return dict(list(context.items()) + list(c_def.items()))


    def form_valid(self, form):
        """
        Данный метод позволяет перевести пользователя после успешной регистрации
        сразу на домашнюю страницу.

        """
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'my_page/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Sing in")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')