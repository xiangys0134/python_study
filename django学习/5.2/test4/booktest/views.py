from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse

# Create your views here.

# 装饰器函数
def login_required(view_func):
    '''登陆判断装饰器'''
    def wrapper(request,*args,**kwargs):
        #判断用户是否登录
        if request.session.has_key('islogin'):
            # 用户已登录
            res = view_func(request,*args,**kwargs)
            return res
        else:
            # 用户未登陆
            return redirect('/login')
    return wrapper

def index(request):
    return render(request, 'booktest/index.html')

def login(request):
    '''显示登陆页面'''
    # print('aaa')
    # 判断用户是否登录
    if request.session.has_key('islogin'):
        # 用户已登录，跳转到修改密码页面
        return redirect('/change_pwd')
    else:
        username = request.COOKIES.get('username')
        context = {}
        if username:
            context['username'] = username
        else:
            context['username'] = ''
        return render(request, 'booktest/login.html', context)

def login_check(request):
    '''登陆校验视图'''
    # 1.获取提交的用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')

    # 获取验证
    vcode1 = request.POST.get('vcode')
    # 获取session所保存的验证码
    vcode2 = request.session.get('verifycode')

    # 进行验证码验证
    if vcode1 != vcode2:
        print('aaaaaaaa')
        return redirect('/login')

    if username == 'root' and password == '123':
        response = redirect('/change_pwd')

        if remember == 'on':
            # 跳转到修改密码页面
            # 记录用户登录状态
            response.set_cookie('username', username, max_age=14 * 24 * 3600)
        request.session['username'] = username
        request.session['islogin'] = True
        return response
    return redirect("/login")

# /change_pwd
@login_required
def change_pwd(request):
    '''显示修改密码页面'''
    # 进行用户是否登录的判断
    # if not request.session.has_key('islogin'):
    #     return redirect('/login')
    return render(request,'booktest/change_pwd.html')

@login_required
def change_pwd_action(request):
    '''模拟修改密码处理'''
    # 1.获取新密码
    pwd = request.POST.get('pwd')

    # 2.获取用户名
    username = request.session.get('username')
    return HttpResponse('%s修改了密码，新密码：%s'%(username,pwd))

from PIL import Image,ImageDraw,ImageFont
from django.utils.six import BytesIO

# /verify_code
def verify_code(request):
    import random

    # 自定义变量用于画面的背景色、宽、高
    bgcolor = (random.randrange(20,100),random.randrange(20,100),255)
    width = 100
    heigt = 25

    # 创建画面对象
    im = Image.new('RGB',(width,heigt),bgcolor)

    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0,100):
        xy = (random.randrange(0,width),random.randrange(0,heigt))
        fill = (random.randrange(0,255),255,random.randrange(0,255))
        draw.point(xy,fill=fill)

    # 定义验证码备选值
    l1 = []
    for i in range(5):
        list1 = [chr(i) for i in range(65, 91)]
        list2 = [chr(i) for i in range(97,123)]
        list3 = [str(i) for i in range(0,9)]

        str_list = list1 + list2 +list3
        random_num = random.choice(str_list)
        l1.append(str(random_num))
    # print('list>>>',type(l1[0]))
    rand_str = "".join(l1)

    #构造字体对象
    # font = ImageFont.truetype('static/font/kumo.ttf',23)
    font = ImageFont.truetype("static/font/kumo.ttf",23)

    #构造字体颜色
    fontcolor = (255,random.randrange(0,255),random.randrange(0,255))
    # print('aaaaa',fontcolor)
    # 绘制4个字
    # draw.text((5, 2), rand_str[0])
    draw.text((5,2),rand_str[0],font=font,fill=fontcolor)
    draw.text((25,2),rand_str[1],font=font,fill=fontcolor)
    draw.text((50,2),rand_str[2],font=font,fill=fontcolor)
    draw.text((75,2),rand_str[3],font=font,fill=fontcolor)

    # 释放画笔
    del draw
    # 存入session 用于进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf,'png')
    return HttpResponse(buf.getvalue(),'image/png')

def url_reverse(request):
    '''url反向解析页面'''
    return render(request,'booktest/url_reverse.html')

def show_args(request,a,b):
    return HttpResponse(a+':'+b)

def show_kwargs(request,c,d):
    return HttpResponse(c + ':' + d)

from django.shortcuts import reverse
def test_redirect(request):
    url = reverse('booktest:index')
    return redirect(url)
