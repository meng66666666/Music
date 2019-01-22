import hashlib

from django.shortcuts import render, redirect
from django.urls import reverse

from mymusic.models import User
from myuser.forms import UserRegister


def take_md5(content):
    md5 = hashlib.md5()  # 创建hash加密实例
    md5.update(content.encode())  # hash加密
    result = md5.hexdigest()  # 得到加密结果
    return result


def home(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(pk=user_id)
    return render(request, 'home.html',locals())


def register(request):
    if request.method == 'GET':
        form = UserRegister()
        print(form.as_p())
        return render(request, 'register.html', locals())
    if request.method == 'POST':
        form = UserRegister(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            name_filter = User.objects.filter(username=username)

            if len(name_filter) > 0:
                return render(request, 'register.html', {'error': '用户名已存在'})
            else:
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']

                if password1 != password2:
                    return render(request, 'register.html', {'error': '密码不一致！'})
                else:
                    password = take_md5(password1)
                    phone_num = form.cleaned_data['phone_num']
                    user = User.objects.create(username=username, password=password, phone_num=phone_num)
                    user.save()
                    return redirect(reverse('login'), locals())


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        username = request.POST.get('loginUser')
        password = request.POST.get('password')
        password1 = take_md5(password)
        # print(password1)
        users = User.objects.filter(username=username,password=password1)
        # print(users)
        if users:
            user = users.first()
            request.session['user_id'] = user.id
            return redirect(reverse('home'))
        else:
            return redirect(reverse('login', kwargs={'error': '该用户名不存在'}))

