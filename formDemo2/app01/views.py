from django.shortcuts import render,redirect,HttpResponse

# Create your views here.

from django import forms
from app01.models import Emp
from django.core.exceptions import NON_FIELD_ERRORS,ValidationError
class EmpForm(forms.Form):
    name = forms.CharField(min_length=5,label="姓名")
    age = forms.IntegerField(label="年龄")
    salary = forms.CharField(label="薪水")


    def clean_name(self):
        val = self.cleaned_data.get("name")
        #二次校验
        if val.isdigit():
            raise ValidationError("用户名不能为纯数字")
        elif Emp.objects.filter(name=val):
            raise ValidationError("该用户名已存在")
        else:
            return val

    def clean_age(self):
        val = self.cleaned_data.get("age")
        if int(val) >100:
            raise ValidationError("年龄不能大于100")
        else:
            return val

# def addemp(request):
#     if request.method == "GET":
#         form = EmpForm()
#         return render(request,"add.html",locals())
#     else:
#         print(request.POST)
#         form = EmpForm(request.POST)
#         if form.is_valid():
#             Emp.objects.create(**form.cleaned_data)
#             print(form.cleaned_data)
#             print(form.errors)
#             return HttpResponse("添加成功")
#         else:
#             print(form.cleaned_data)
#             print(form.errors)
#
#             return render(request,"add.html",locals())


from django.http import JsonResponse
def addemp(request):
    if request.is_ajax():
        res= {"state":True,"errors":None}
        form = EmpForm(request.POST)
        if form.is_valid():
            Emp.objects.create(**form.cleaned_data)
            print(form.cleaned_data)
            print(form.errors)
            return JsonResponse(res)
        else:
            print(form.cleaned_data)
            print(form.errors)
            res["state"] = False
            res["errors"] = form.errors
            return JsonResponse(res)
    else:
        form = EmpForm()
        return render(request, "add.html", locals())

