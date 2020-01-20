from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

import time,json

def index(request):
    return render(request,"index.html")


def index_banner(request):
    time.sleep(5)
    return HttpResponse("index_banner")


def index_banner2(request):
    print(request.GET)
    print(request.POST)
    return HttpResponse("ok")

def cal(request):
    print(request.POST)
    print(request.GET)
    response = {"code":1000,"data":None,"msg":None}
    try:
        n1 = request.POST.get("n1")
        n2 = request.POST.get("n2")
        num_count = int(n1) + int(n2)
        response["data"] = num_count
        print(response["data"],response["code"])
        return HttpResponse(json.dump(response))
    except Exception as e:
        response["code"] = 1001
        response["msg"] = str(e)
        print(response["code"])
        return HttpResponse(json.dumps(response))