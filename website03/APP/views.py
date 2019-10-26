from django.shortcuts import render,HttpResponse
from APP.models import Student
from APP.models import Users

# Create your views here.
def static01(request):
    return HttpResponse('static ok')

def index(request):
    context = {}
    context['hello'] = 'Hello World!'
    context['tt'] = 52
    context['athlete_list']= ['张三','李四']
    return render(request,'index.html',context)

def addstudent(request):
    student = Student()
    student.s_name = 'Tom'
    student.save()
    return HttpResponse("添加成功")

def getstudents(request):
    stuents = Student.objects.all()
    for s in stuents:
        print(s.s_name)
    # return HttpResponse("Student List")
    context = {
        'hobby':'羽毛球',
        "students":s
    }
    return render(request,'student_list.html',context=context)

def deletestudent(request):
    student = Student.objects.get(pk=3)
    student.delete()
    return HttpResponse("删除成功")

def adduser(request):
    user = Users()
    user.u_name = 'Marr'
    user.u_age = 13
    user.u_addr= '北京'
    user.save()
    return HttpResponse("添加成功")


def getuser(request):
    context_user = {}
    user = Users.objects.all()
    context_user['user'] = user
    return render(request,'getuser.html',context=context_user)


def userupdate(request):
    u = Users.objects.get(u_name='Tom')
    u.u_name = '张三'
    u.u_age = 16
    u.save()
    context_user = {}
    user = Users.objects.all()
    context_user['user'] = user
    return render(request,'getuser.html',context_user)

def deleteuser(request):
    u = Users.objects.get(u_name='Marr')
    u.delete()
    context_user = {}
    user = Users.objects.all()
    context_user['user'] = user
    return render(request,'getuser.html',context_user)