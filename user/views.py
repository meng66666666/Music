from django.shortcuts import render, redirect
from django.urls import reverse


def user_home(request):
    

    page = 1
    return render(request, 'home.html',locals())

def logout(request):
    request.session.flush()
    return redirect(reverse('mymusic:index'))

