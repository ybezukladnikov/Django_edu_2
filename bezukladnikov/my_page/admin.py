from django.contrib import admin

from .models import *

class SportsGroundAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published', 'city') # интересный момент связи таблиц
    # если я укажу city то сработает связка и я получу название города, но если я напишу
    # city_id я уже получу доступ именно значению данного атрибута из таблицы площадок. А именно просто цифру)
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}

class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    # prepopulated_fields данное поле позволит автоматичеси
    # заполнять поле slug в админ панели при заполеннии поля name
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(SportsGround, SportsGroundAdmin)
admin.site.register(City, CityAdmin)