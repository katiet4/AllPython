from django.urls import path
from . import views
urlpatterns = [
    path('', views.login, name='Login'),
    path('registration', views.registration, name='registration'),
    path('Exit', views.exit, name='exit'),
]