from django.shortcuts import render,redirect,HttpResponse

# Create your views here.


def login(request):
    return render(request,"login.html")


def auth(request):
    print(request.POST)
    if request.method == "GET":
        return render(request,"login.html")

    if request.POST.get("user") == "alex" and request.POST.get("pwd") == "123":
        return HttpResponse("登陆成功")
    return HttpResponse("登陆失败")