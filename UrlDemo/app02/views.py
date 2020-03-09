from django.shortcuts import render,redirect,HttpResponse

# Create your views here.


def videos(request,id):
    return HttpResponse("Videos:%s"%id)