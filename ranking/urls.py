from django.contrib import admin
from django.urls import path,include

from mymusic.views import index
from play.views import play
from ranking.views import rankingView
from search.views import search
from user.views import user_home,logout


urlpatterns = [
    path('ranking/',rankingView,name='ranking'),
    path('home/',user_home,name='home'),
    path('logout/', logout, name='logout'),
    path('index/', index, name='index'),
    path('play/<song_id>/', play, name='play'),
    path('search/<page>/',search, name='search'),
]

