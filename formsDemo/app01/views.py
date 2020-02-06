from django.shortcuts import render,redirect,HttpResponse

# Create your views here.

from django import forms
from app01.models import Emp
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

class EmpForm(forms.Form):
    name = forms.CharField(min_length=5,label='姓名',error_messages={"required":"该字段不能为空"})
    age=forms.IntegerField(label='年龄')
    salary = forms.DecimalField(label='薪水')

    def clean_name(self):
        val = self.cleaned_data.get("name")

        #二次校验
        if val.isdigit():
            raise ValidationError("姓名不能是纯数字")
        elif Emp.objects.filter(name= val):
            raise ValidationError("该用户已经存在")
        else:
            return val

    def clean_age(self):
        val = self.cleaned_data.get("age")
        if int(val) >100 or int(val) < 0:
            raise ValidationError("年龄不能小于0或大于100")
        else:
            return val


# def addEmp(request):
#     if request.method == "GET":
#         ef = EmpForm()
#         return render(request,"add.html",locals())
#     else:
#         print(request.POST)
#         ef = EmpForm(request.POST)
#         if ef.is_valid():
#             Emp.objects.create(**ef.cleaned_data)
#             return HttpResponse("添加成功")
#         else:
#             # print(ef.errors)
#             # return render(request,"add.html",locals())
#             return render(request, "add.html", locals())

from django.http import JsonResponse
from django.contrib import auth

#ajax请求的视图函数
def addEmp(request):
    if request.is_ajax():
        print(">>>",request.POST)
        ef = EmpForm(request.POST)
        res = {"state":True,"errors":None}
        if ef.is_valid():
            print(ef.cleaned_data)
            Emp.objects.create(**ef.cleaned_data)
        else:
            res["state"] = False
            res["errors"] = ef.errors
            print(ef.cleaned_data)
        return JsonResponse(res)
    else:
        ef = EmpForm()
        return render(request,"add.html",locals())

def login(request):
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("/login/")
