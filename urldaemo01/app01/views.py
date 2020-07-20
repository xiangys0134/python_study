from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def special_case_2003(request,y,m):
    return HttpResponse('年：%s月：%s'%(y,m))

def index(request):
    print(request.method)
    print(request.path)
    print(request.GET)
    print(request.POST)
    print(request.META)
    print(request.is_ajax())
    print(request.body)     #请求体原生数据
    import datetime
    good_list = {'name':'alex',"age":34,"addr":"沙河"}
    l=[111,222,333]
    name = 'alex'
    now = datetime.datetime.now()
    return render(request,'index.html',{'good_list':good_list,'name':name,'l':l,"now":now})



def login(request):
    if request.method =="POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == 'alex' and pwd =='123':
            return redirect('/app01/index/')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')



