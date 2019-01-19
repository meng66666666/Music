from django.urls import path, include

from mymusic.views import *

app_name = 'mymusic'
urlpatterns = [
    path('index/', index, name='index'),
]
