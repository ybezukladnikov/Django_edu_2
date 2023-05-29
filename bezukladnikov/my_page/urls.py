from django.urls import path

from .views import *

urlpatterns = [

    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('SportsGround/<slug:SportsGround_slug>/', show_sports_ground, name='SportsGround'),
    path('category/<slug:cat_slug>/', show_category, name='category'),
    # path('project/', all_project, name='my_project'),
    # path('project/<int:proj_id>/', project),

]
