from django.shortcuts import render,HttpResponse,redirect

# Create your views here.


def articles_case_2003(request):
    return HttpResponse("2003")


def year_archive(request,id):
    return HttpResponse(str(id))

