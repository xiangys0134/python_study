from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

from rbac.models import User

def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    else:
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        user_obj = User.objects.filter(name=user,pwd=pwd).first()
        if user_obj:
            #注入用户信息
            request.session["user_id"] = user_obj.pk

            from rbac.service.permissions import permission_init

            permission_init(request,user_obj)

            return redirect("/index/")
        else:
            return render(request,"login.html")


def index(request):

    return render(request,"index.html")