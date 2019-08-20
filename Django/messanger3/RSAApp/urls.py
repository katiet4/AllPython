from django.urls import path
from . import views
urlpatterns = [
    path('', views.RsA, name='RSA'),
]