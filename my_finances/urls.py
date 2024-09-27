from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('register/', views.register_view, name='register'),
    path('login/', views.user_login, name='login'),
]