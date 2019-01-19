import hashlib
import random
import urllib.parse

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
import http.client

from mymusic.models import User
from myuser.forms import RegisterForm

host = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"
# 用户名是登录ihuyi.com账号名
account = "78124019"
password = "1c765cd6366c6d6425c293c48b243fda"


def send_message(request):
    # 获取ajax的get方法发送过来你的手机号码
    mobile = request.GET.get('mobile')
    # 通过手机去查找用户是否已经注册
    user = User.objects.filter(tel=mobile)
    if len(user) == 1:
        return JsonResponse({'msg': '该手机已经注册'})
    message_code = ""
    for i in range(6):
        i = random.randint(0, 9)
        message_code += str(i)
    # 拼接成发出的短信
    text = "您的验证码是：" + message_code + "。请不要把验证码泄露给其他人。"
    # 把请求参数编码
    params = urllib.parse.urlencode(
        {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    # 向连接后的服务器发送post请求,路径sms_send_uri是全局变量,参数,请求头
    conn.request("POST", sms_send_uri, params, headers)
    # 获取服务器属性
    response = conn.getresponse()
    # 获取响应数据
    response_str = response.read()
    conn.close()
    request.session['message_code'] = message_code
    print(eval(response_str.decode()))
    return JsonResponse(eval(response_str.decode()))


def register(request):
    if request.method == 'GET':
        register_form = RegisterForm()
        return render(request, 'home.html', locals())

    # if request.method == 'POST':
    #     userform = RegisterForm()
    #     if userform.is_valid():
    #         regemail = userform.clean_data["regemail"]
    #         regname = userform.clean_data["regname"]
    #         regtel = userform.clean_data["regtel"]
    #         regpwd = userform.clean_data["regpwd"]
    #         # check_user_info(regemail, regname, regtel, regpwd)
    #         new_user = User()  # 实例化新用户对象，新用户属性
    #         new_user.email = regemail
    #         new_user.name = regname
    #         new_user.tel = regtel
    #         md5 = hashlib.md5()
    #         md5.update(regpwd.encode("utf-8"))
    #         new_user.pwd = md5.hexdigest()
    #
    #         new_user.save()
    #         return render(request, 'home.html', locals())


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':
        login_email = request.POST.get("login_email")
        login_pwd = request.POST.get('login_pwd')
        md5 = hashlib.md5()
        md5.update(login_pwd.encode("utf-8"))
        login_pwd = md5.hexdigest()

        users = User.objects.filter(name=login_email, pwd=login_pwd)
        if users:
            user = users.first()
            request.session['user_id'] = user.id  # 登录成功后设置session属性
            return redirect(reverse('mymusic:index'))
        else:
            return redirect(reverse('login.html'))


def logout(request):
    request.session.flush()  # 如果退出登录，则彻底删除之前设置的session
    return redirect(reverse('yougou:index'))

def login_(request):
    return render(request, 'login.html')
