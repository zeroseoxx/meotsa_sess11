from django.urls import path
from . import views

app_name = 'mainpage'

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
]
