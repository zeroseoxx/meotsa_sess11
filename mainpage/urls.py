from django.urls import path
from . import views

app_name = 'mainpage'

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    # 상세 페이지 연결
    # path('movie/<int:pk>', views.detailpage, name='detailpage'),
]
