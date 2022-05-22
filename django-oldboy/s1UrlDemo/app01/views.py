from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

# Create your views here.

def articles(request,year):
    return HttpResponse(str(year))