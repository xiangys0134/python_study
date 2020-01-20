from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
from app01.models import UserInfo


def login_required(func):
    def inner(request,*args,**kwargs):
        is_login =request.session.get("is_login")
        if not is_login:
            return redirect("/login/")
        else:
            return func(request,*args,**kwargs)
    return inner

@login_required
def index(request):
    print(">>>",request.session.get("is_login"))
    print(">>>",request.session.get("username"))

    is_login = request.session.get("is_login")
    username = request.session.get("username")

    # if not is_login:
    #     return redirect("/login/")
    return render(request,"index.html",locals())

def login(request):
    print(">>>",request.session.get("is_login"))
    print(">>>",request.session.get("username"))
    if request.method =="GET":
        return render(request,"login.html")
    else:
        is_login=request.session.get("is_login")
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        if not is_login:
            user_obj = UserInfo.objects.filter(name=user, pwd=pwd).first()
            if user_obj:
                request.session["is_login"] = True
                request.session["username"] = user
                username=user
                return redirect("/index/",locals())
            else:
                return redirect("/login/")
        else:
            username = request.session.get("username")
            redirect("/index/",locals())

def loginout_session(request):
    request.session["is_login"] = False
    return redirect("/login/")

@login_required
def order(request):
    is_login = request.session.get("is_login")
    username = request.session.get("username")
    # if not is_login:
    #     return redirect("/login/")
    return render(request,"order.html",locals())