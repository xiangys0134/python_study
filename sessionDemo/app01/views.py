from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
from django.forms import Form,fields
from django.contrib import auth
from app01.models import UserInfo
from django.contrib.auth.decorators import login_required
class UserInfoForm(Form):
    name = fields.CharField(max_length=32,label="用户名")
    pwd = fields.CharField(max_length=32,label="密码")


'''
def login_required(func):
    def inner(request,*args,**kwargs):
        is_login = request.session.get("is_login")
        print(is_login)
        if not is_login:
            return redirect("/login/")
        else:
            return func(request,*args,**kwargs)
    return inner


@login_required
def index(request): #login_required(index(request))
    # print(request.user)
    # username = request.user.username
    # print("username",username)
    username = request.session.get("username")
    return render(request,"index.html",locals())

def login(request):
    if request.method == "GET":
        ef = UserInfoForm()
        return render(request,"login.html",locals())
    else:
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        # user_obj = auth.authenticate(username=user,password=pwd)
        print('>>>>',user,pwd)
        user_obj = UserInfo.objects.filter(name=user,pwd=pwd).first()
        print(">>>>>>",user_obj)
        if user_obj:
            # auth.login(request,user_obj)    #注入session信息
            request.session["is_login"] = True
            request.session["username"] = user
            return redirect("/index/")
        return HttpResponse("msg")

@login_required
def order(request):
    return render(request,"order.html")

def logout(request):
    # auth.logout(request)
    request.session["is_login"] = False
    return redirect("/login/")
'''

@login_required
def index(request): #login_required(index(request))
    # print(request.user)
    # username = request.user.username
    # print("username",username)
    # username = request.session.get("username")
    # if not request.user.id:
    #     print("---",request.user.id)
    #     return redirect("/login/")
    username = request.user.username
    pwd = request.user.password
    print(">>>>",username)
    print(">>>>",pwd)
    return render(request,"index.html",locals())

def login(request):
    if request.method == "GET":
        ef = UserInfoForm()
        return render(request,"login.html",locals())
    else:
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        user_obj = auth.authenticate(username=user,password=pwd)
        print('>>>>',user,pwd)
        # user_obj = UserInfo.objects.filter(name=user,pwd=pwd).first()
        print(">>>>>>",user_obj)
        if user_obj:
            auth.login(request,user_obj)    #注入session信息
            # request.session["is_login"] = True
            # request.session["username"] = user
            print(request.path)
            print(request.get_full_path())
            print(request.GET.get("next"))
            path = request.GET.get("next") or "/index/"
            # return HttpResponse("000")
            return redirect(path)
        return redirect("/login/")


@login_required
def order(request):
    # if not request.user.id:
    #     return redirect("/login/")
    return render(request,"order.html")

def logout(request):
    auth.logout(request)
    # request.session["is_login"] = False
    return redirect("/login/")

