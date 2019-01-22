from django.urls import path, include

from myuser.views import *


urlpatterns = [
    path('home/', home, name='home'),
    path('register/', register, name='register'),
    # path('play/',play,name='play'),
    path('login/', login, name='login'),


    # path('search/', search, name='search'),
]
