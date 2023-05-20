from django.urls import path

from .views import *

urlpatterns = [

    path('', index, name='home'),
    path('project/<int:proj_id>/', project),

]
