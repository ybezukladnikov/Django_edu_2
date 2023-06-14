from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    # кэширование на уровни представления.
    # кэшируем на 60 секунд.
    # path('', cache_page(60)(MyPageHome.as_view()), name='home')
    path('', MyPageHome.as_view(), name='home'), # чтобы связать класс представления с url надо обязательно вызвать функцию
                                                    # as.view()

    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('SportsGround/<slug:SportsGround_slug>/', ShowSportsGround.as_view(), name='SportsGround'),
    path('category/<slug:cat_slug>/', CityList.as_view(), name='category'),
    # path('project/', all_project, name='my_project'),
    # path('project/<int:proj_id>/', project),

]
