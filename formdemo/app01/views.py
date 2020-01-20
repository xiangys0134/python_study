from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
from django import forms
from app01.models import Emp
from django.core.exceptions import NON_FIELD_ERRORS,ValidationError
from django.http import JsonResponse

class EmpForm(forms.Form):
    name = forms.CharField(min_length=5,label="姓名")
    age = forms.IntegerField(label="年龄")
    salary = forms.CharField(label="薪水")

    def clean_name(self):
        val = self.cleaned_data.get("name")
        #二次校验
        if val.isdigit():
            raise ValidationError("姓名不能是纯数字")
        else:
            return val

    def clean_age(self):
        val = self.cleaned_data.get("age")
        if int(val) > 100:
            raise ValidationError("年龄不能大于100")
        else:
            return val

# def addEmp(request):
#     if request.method=="GET":
#         form = EmpForm()
#         return render(request,"add.html",locals())
#     else:
#         print(request.POST)
#         #获取字段值分别校验
#         form = EmpForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             Emp.objects.create(**form.cleaned_data)
#             return HttpResponse("添加成功")
#         else:
#             print(form.errors)
#             return render(request,"add.html",{"form":form})

#Ajax请求试图函数

def addEmp(request):
    print(request.POST)
    if request.is_ajax():
        res = {"state":True,"erros":None}
        form = EmpForm(request.POST)
        print(request.POST)
        if form.is_valid():
            res = Emp.objects.filter(name=form.cleaned_data["name"]).first().name
            Emp.objects.create(**form.cleaned_data)
        else:
            res["state"] = False
            res["erros"] = form.errors
        return JsonResponse(res)

    else:
        if request.method=="GET":
                form = EmpForm()
                return render(request,"add.html",locals())
        else:
            print(request.POST)
            #获取字段值分别校验
            form = EmpForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
                Emp.objects.create(**form.cleaned_data)
                return HttpResponse("添加成功")
            else:
                print(form.errors)
                return render(request,"add.html",{"form":form})