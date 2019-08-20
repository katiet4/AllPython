from django.urls import path
from . import views
urlpatterns = [
	path('', views.chatDef, name = 'chat')
]