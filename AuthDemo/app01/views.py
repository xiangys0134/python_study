from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
from app01.models import UserInfo
from django.contrib import auth

def login_required(func):
    def inner(request,*args,**kwargs):
        is_login =request.session.get("is_login")
        if not is_login:
            return redirect("/login/")
        else:
            return func(request,*args,**kwargs)
    return inner


def index(request):
    print(">>>",request.session.get("is_login"))
    print(">>>",request.session.get("username"))
    if request.user.id:
        return render(request,"index.html",locals())
    return redirect("/login/")


def login(request):
    print(">>>",request.session.get("is_login"))
    print(">>>",request.session.get("username"))
    if request.method =="GET":
        return render(request,"login.html")
    else:
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        print(user,pwd)
        user_obj=auth.authenticate(username=user,password=pwd)
        print(user_obj,"############")
        if user_obj:
            print(request.user.username)
            auth.login(request, user_obj)
            print(request.path)
            return redirect("/index/")
        else:
            return redirect("/login/")

def loginout_session(request):
    request.session["is_login"] = False
    return redirect("/login/")

# @login_required
def order(request):
    if request.user.id:
        return render(request, "order.html", locals())
    return redirect("/login/")

def logout(request):
    auth.logout(request)
    return redirect("/login/")