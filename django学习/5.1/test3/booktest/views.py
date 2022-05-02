from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request,'booktest/index.html')

def login(request):
    '''显示登陆页面'''
    # print('aaa')
    # 判断用户是否登录
    if request.session.has_key('islogin'):
        # 用户已登录，跳转到首页
        return redirect('/index')
    else:
        username = request.COOKIES.get('username')
        context = {}
        if username:
            context['username'] = username
        else:
            context['username'] = ''
        return render(request,'booktest/login.html',context)

def login_check(request):
    '''登陆校验视图'''
    # 1.获取提交的用户名和密码
    print(request.POST)
    print(request.POST.get("username"))

    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')

    if username == 'root' and password == '123':
        if remember == 'on':
            response = redirect('/index')
            response.set_cookie('username',username,max_age=14*24*3600)

        # 记录用户登录状态
        request.session['islogin'] = True

        return response
    return redirect("/login")

# /test_ajax
def ajax_test(request):
    '''显示ajax页面'''
    return render(request,'booktest/test_ajax.html')

# /ajax_handle
def ajax_handle(request):
    '''ajax清楚处理'''
    context = {'res':2}
    return JsonResponse(context)

# /login_ajax
def login_ajax(request):
    '''显示ajax登陆页面'''
    return render(request,'booktest/login_ajax.html')

# /login_ajax_check
def login_ajax_check(request):
    '''ajax登陆校验'''
    # 1.获取用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')

    print('aaa>>',username,password)
    context = {}
    # 2.校验
    if username == 'smart' and password == '123':
        context['res'] = 1
        return JsonResponse(context)
    else:
        context['res'] = 0
        return JsonResponse(context)

def set_cookie(request):
    '''设置一个cookie信息'''
    response = HttpResponse('设置cookie')
    response.set_cookie('num',1,max_age=14*24*3600)
    return response

def get_cookie(request):
    '''获取cookie的信息'''
    # 取出cookie num的值
    num = request.COOKIES['num']
    return HttpResponse(num)

# /set_session
def set_session(request):
    '''设置session'''
    request.session['username'] = 'smart'
    request.session['age'] = 18

    return HttpResponse('设置session')

def get_session(request):
    '''获取session'''
    username = request.session['username']
    age = request.session['age']

    context = {'username':username,'age':age}
    return HttpResponse(username + str(age))

# /clear_session
def clear_session(request):
    '''清除session'''
    request.session.clear()
    return HttpResponse('清除session成功')