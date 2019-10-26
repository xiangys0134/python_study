from django.shortcuts import render,HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse('ok')

def hehe(request):
    return HttpResponse('呵呵')

def haha(request):
    return HttpResponse("<h1>睡觉的站起来！</h1>")

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')