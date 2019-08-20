from django.contrib import admin

from UsersApp.models import Users
from chatWithFriends.models import DialogueBD, DialoguesBD
admin.site.register(Users)
admin.site.register(DialogueBD)
admin.site.register(DialoguesBD)
# Register your models here.
