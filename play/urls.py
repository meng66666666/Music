from django.urls import path

from .views import play
app_name='play'
urlpatterns = [
    path('play/<song_id>/',play,name='play'),

]