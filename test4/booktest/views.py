from django.shortcuts import render,redirect
from django.template import loader,RequestContext
from django.http import HttpResponse
# Create your views here.
from booktest.models import BookInfo
from django.urls import reverse

def login_required(view_func):
    '''登陆判断装饰器'''
    def wrapper(request,*args,**kwargs):
        #判断用户是否登陆
        if request.session.has_key('islogin'):
            return view_func(request,*args,**kwargs)
        else:
            return redirect('/login/')
    return wrapper

def my_render(request,template_path,context={}):
    temp = loader.get_template(template_path)
    res_html = temp.render(context)
    return HttpResponse(res_html)

def index(request):
    # return my_render(request,'booktest/index.html',{'my_name':'aaa'})
    return render(request,'booktest/index.html',{'my_name':'aaa'})

def index2(request):
    '''模板文件的加载顺序'''

    return render(request,'booktest/index2.html',{'my_name':'aaa'})

def temp_var(request):
    '''模板变量'''
    my_dict = {'title':'字典键值'}
    my_list = [1,2,3]

    book = BookInfo.objects.get(id=1)
    context = {'my_dict':my_dict,'my_list':my_list,'book':book}
    return render(request,'booktest/temp_var.html',context)

def temp_tags(request):
    '''模板标签'''
    books = BookInfo.objects.all()
    context = {'books':books}
    return render(request,'booktest/temp_tags.html',context)

def temp_filter(request):
    '''模板过滤器'''
    books = BookInfo.objects.all()
    context = {'books':books}
    return render(request,'booktest/temp_filter.html',context)

def temp_inherit(request):
    '''模板继承'''
    return render(request,'booktest/child.html')

def html_escape(request):
    '''html转义'''
    return render(request,'booktest/html_escape.html',{'content':'<h1>hello<h1/>'})

def login(request):
    '''显示登陆页面'''
    # if request.session.has_key('islogin'):
    #     return redirect('/change_pwd')
    # if 'username' in request.COOKIES:
    #     username = request.COOKIES.get('username')
    # else:
    #     username = ''
    return render(request,'booktest/login.html')

def login_check(request):
    '''登陆校验视图'''
    # print(request.POST)
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    # print(remember)

    print('>>>>')
    print(username,password)
    if username == 'smart' and password == '123':
        response = redirect('/change_pwd')
        #判断是否需要记住用户名
        if remember == 'on':
            # response.set_cookie('username',username,max_age=14*24*3600)
            request.session['islogin'] = True
            request.session['username'] = username
        return response
    else:
        return render(request,'booktest/login.html')
@login_required
def change_pwd(request):
    '''显示修改密码页面'''
    # if not request.session.has_key('isLogin'):
    #     redirect('/login')
    if request.session.has_key('islogin'):
        print('ssssss')
    if request.session.has_key('username'):
        print('yyyyyyy')
    return render(request,'booktest/change_pwd.html')

@login_required
def change_pwd_action(request):
    '''模拟修改密码处理'''
    # if not request.session.has_key('username'):
    #     return redirect('/login')
    # else:
    username = request.session.get('username')
    pwd = request.POST.get('pwd')

    return HttpResponse('%s修改密码为:%s'%(username,pwd))

def url_reverse(request):
    '''url反向解析页面'''
    return render(request,'booktest/url_reverse.html')

def show_args(request,a,b):
    return HttpResponse(str(a) + ':' + str(b))

def show_kwargs(request,c,d):
    return HttpResponse(str(c)+':'+str(d))

def test_redirect(request):
    # return redirect('/index')
    url = reverse('booktest:show_args',args=(1,2))
    return redirect(url)