from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('new-user/', views.new_user, name='new_user'),
]