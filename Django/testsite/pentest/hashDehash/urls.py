from django.urls import path
from . import views
urlpatterns = [
	path('', views.hashDehash, name = 'hashDehash')
]