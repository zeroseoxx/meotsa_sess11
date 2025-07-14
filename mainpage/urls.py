from django.urls import path
from . import views
from views import movie_list

app_name = 'mainpage'

urlpatterns = [
    path('', movie_list, name='movie_list'),
]