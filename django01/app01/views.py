from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
import datetime

def index(request):
    s = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse('index')


def r_time(request):
    s = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(s)


def login(request):
    return render(request,"login.html")

def auth(request):
    username = request.POST.get("user")
    password = request.POST.get("pwd")
    if username =='alex' and password == '123':
        return HttpResponse("登录成功")
    else:
        return HttpResponse("登录失败")
