from django.urls import path, include

from myuser.views import register,login_

urlpatterns = [
    path('home/', register, name='home'),
    path('login/',login_,name='login'),
]
