# coding=utf-8

from django.shortcuts import render,HttpResponse

# Create your views here.

def set_session(request):
    request.session['name'] = 'root'
    request.session['age'] = 18

    return HttpResponse('设置session')

def get_session(request):
    username = request.session['name']
    age = request.session['age']

    return HttpResponse(username+':'+str(age))
