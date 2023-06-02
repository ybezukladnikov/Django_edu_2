from django.urls import path

from .views import *

urlpatterns = [

    path('', MyPageHome.as_view(), name='home'), # чтобы связать класс представления с url надо обязательно вызвать функцию
                                                    # as.view()
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('SportsGround/<slug:SportsGround_slug>/', ShowSportsGround.as_view(), name='SportsGround'),
    path('category/<slug:cat_slug>/', CityList.as_view(), name='category'),
    # path('project/', all_project, name='my_project'),
    # path('project/<int:proj_id>/', project),

]
