from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('user/', views.user_detail, name='user-detail'),
]