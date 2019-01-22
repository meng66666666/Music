from django.urls import path

from play.views import play
from search.views import search

app_name = 'search'

urlpatterns = [
    path('search/<int:page>/',search,name='search'),
    path('play/<song_id>/',play,name='play')
]