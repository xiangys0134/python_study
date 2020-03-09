from django.shortcuts import render,redirect,HttpResponse

# Create your views here.


from app01.models import UserInfo

def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    else:
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")

        user_obj = UserInfo.objects.filter(name=user,pwd=pwd).first()

        if user_obj:
            obj = redirect("/index/")
            obj.set_cookie("is_login",True,20)
            obj.set_cookie("username",user)

            return obj
        return HttpResponse("Error!")

def index(request):
    print("request.COOKIES",request.COOKIES)
    is_login = request.COOKIES.get("is_login")
    username = request.COOKIES.get("username")

    if not is_login:
        return redirect("/login/")

    return render(request,"index.html",locals())


def logout_session(request):
    obj = redirect("/login/")
    obj.delete_cookie("is_login")
    return obj



