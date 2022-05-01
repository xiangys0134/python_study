from django.shortcuts import render,HttpResponse,redirect
from django.http import Http404,JsonResponse

# Create your views here.

def index(request):
    return render(request,'booktest/index.html')

def login(request):
    '''显示登陆页面'''
    if request.session.has_key('islogin'):
        return redirect('/index')
    if 'username' in request.COOKIES:
        username = request.COOKIES.get('username')
    else:
        username = ''
    return render(request,'booktest/login.html',{'username':username})

def login_check(request):
    '''登陆校验视图'''
    # print(request.POST)
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    # print(remember)

    if username == 'smart' and password == '123':
        response = redirect('/index')
        #判断是否需要记住用户名
        if remember == 'on':
            response.set_cookie('username',username,max_age=14*24*3600)
            request.session['islogin'] = True
            request.session['username'] = username
        return response
    else:
        return render(request,'booktest/login.html')

def ajax_test(request):
    '''显示ajax页面'''
    return render(request,'booktest/test_ajax.html')

def ajax_handle(request):
    import json
    '''返回ajax验证页面'''
    t = {}
    t['res'] = 1
    print(request.GET)
    return JsonResponse(t)

# /login_ajax
def login_ajax(request):
    return render(request,'booktest/login_ajax.html')

# /login_ajax_check
def login_ajx_check(request):
    '''ajax登陆校验'''
    username = request.POST.get('username')
    password = request.POST.get('password')

    if username == 'smart' and password =='123':
        return JsonResponse({'res':1})
    else:
        return JsonResponse({'res':0})

def set_cookie(request):
    '''设置cookie信息'''
    response = HttpResponse('设置cookie')
    response.set_cookie('num',1,max_age=14*24*3600)
    return response

def get_cookie(request):
    num = request.COOKIES['num']
    return HttpResponse(num)

def set_session(request):
    '''设置session'''
    request.session['username'] = 'samrt'
    request.session['age'] = 18

    return HttpResponse('设置session')

def get_session(request):
    '''获取session'''
    username = request.session['username']
    age = request.session['age']

    return HttpResponse(username + ':' + str(age))

def clear_session(request):
    '''清除session信息'''
    request.session.flush()
    return HttpResponse('清除成功')