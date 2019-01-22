from django.urls import path

from mymusic.views import *
from play.views import play
from search.views import search

app_name = 'mymusic'
urlpatterns = [
    path('index/', index, name='index'),
    path('play/<song_id>/',play,name='player'),
    # path('search/<int:page>/',search,name='search'),
    path('search/<int:page>/',search,name='search'),
]
