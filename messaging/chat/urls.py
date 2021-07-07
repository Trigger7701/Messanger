from django.urls import  path
from .views import *
urlpatterns = [
    path('', messanger,name='messanger'),
    path('chat/', chat,name='chat'),
    path('sendmessage/', sendmessage,name='sendmessage'),
]