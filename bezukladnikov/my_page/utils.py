'''
this file for help to work another class.
He will content shere atribute.
'''
from .models import *
from django.db.models import Count

menu = [{'title': "About", 'url_name': "about"},
        {'title': "Add Sport Ground", 'url_name': "add_page"},
        {'title': "Feedback", 'url_name': "contact"},
        ]


class DataMixin:
    paginate_by = 2 # указываем количество элементов на одной странце. Это возможно, благодаря тому,
    # что класс в ListView уже встроена Пагинация.
    def get_user_context(self, **kwargs):
        context = kwargs
        # city = City.objects.all()
        city = City.objects.annotate(Count('sportsground'))

        # лучше конечно просто не показывать все меню неавторизованному пользователю
        # и мы можем убрать пункт меню с добавлением площадки если пользователь
        # неавторизован
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu

        context['city'] = city
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context