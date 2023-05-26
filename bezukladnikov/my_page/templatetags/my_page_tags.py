from django import template
from my_page.models import *

register = template.Library()

@register.simple_tag(name='getcities')
def get_cities(filter=None):
    if not filter:
        return City.objects.all()
    else:
        return City.objects.filter(pk=filter)

@register.inclusion_tag('my_page/user_templates/list_cities.html')
def show_cities(sort=None, cat_selected=0):
    if not sort:
        cities = City.objects.all()
    else:
        cities = City.objects.order_by(sort)

    return {"city": cities, "cat_selected": cat_selected}