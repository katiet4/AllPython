from django.urls import path
from . import views
urlpatterns = [
	#friends/
	path('friends/', views.Friends, name = 'friends'),
	path('dialogues/', views.Dialogues, name = 'dialogues')
]