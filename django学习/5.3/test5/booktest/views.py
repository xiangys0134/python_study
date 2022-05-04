from django.shortcuts import render,HttpResponse,redirect
from django.conf import settings
from booktest.models import PicTest,AreaInfo
from django.core.paginator import Paginator
from django.http import JsonResponse

EXCLUDE_IPS = ['192.168.124.241']

# def blocked_ips(view_func):
#     def wrapper(request,*args,**kwargs):
#         user_ip = request.META['REMOTE_ADDR']
#         if user_ip in EXCLUDE_IPS:
#             return HttpResponse('<h1>Forbidden</h1>')
#         else:
#             return view_func(request,*args,**kwargs)
#     return wrapper

# Create your views here.
# @blocked_ips
def index(request):
    # 获取浏览器端的ip地址
    # user_ip = request.META['REMOTE_ADDR']
    # print(user_ip)
    # if user_ip in EXCLUDE_IPS:
    #     return HttpResponse('<h1>Forbidden</h1>')
    return render(request,'booktest/index.html')

# @blocked_ips
def static_test(request):
    '''静态文件'''
    return render(request,'booktest/static_test.html')

def show_upload(request):
    '''显示上传图片页面'''
    return render(request,'booktest/upload_pic.html')

def upload_handle(request):
    '''上传图片处理'''
    # 1.获取上传图片
    pic = request.FILES['pic']
    print(type(pic))

    # 2.创建一个文件
    import time,os,random
    pic_date = time.strftime('%Y-%m-%d',time.localtime())
    if not os.path.exists('%s/booktest/%s' % (settings.MEDIA_ROOT, pic_date)):
        os.makedirs('%s/booktest/%s' % (settings.MEDIA_ROOT, pic_date))
    print('aaaa>>>',type(pic.name))
    rand_str = str(random.randrange(0,9999999999))
    upload_file = rand_str + pic.name
    save_path = '%s/booktest/%s/%s'%(settings.MEDIA_ROOT,pic_date,upload_file)
    with open(save_path,'wb') as f:
        for content in pic.chunks():
            f.write(content)

    # 4.保存上传文件记录 数据库
    PicTest.objects.create(good_pic='booktest/%s'%upload_file)

    return HttpResponse("ok")

def show_area(request,pindex):
    '''分页'''
    # 1.查询出所有省级地区的信息
    areas = AreaInfo.objects.filter(aParent__isnull=True)

    # 2.分页
    paginator = Paginator(areas,10)
    # 3.获取第一页的内容
    if pindex == '':
        pindex = 1
    page = paginator.page(int(pindex))

    # 4.使用模板
    context = {'page':page}
    return render(request,'booktest/show_area.html',context)

def areas(request):
    '''省市县选择案例'''
    return render(request,'booktest/areas.html')

def prov(request):
    '''获取所有省级地区的信息'''
    # 1.获取省级信息
    areas = AreaInfo.objects.filter(aParent__isnull=True)

    # 2.变量areas并拼接出json数据
    areas_list = []
    for area in areas:
        areas_list.append((area.id,area.atitle))
    context = {'data':areas_list}
    # print('context',context)
    return JsonResponse(context)

def city(request,pid):
    '''获取pid下级地区的信息'''
    # area = AreaInfo.objects.get(id=pid)
    # areas = area.areainfo_set.all()

    areas = AreaInfo.objects.filter(aParent_id=pid)
    # 2.变量areas并拼接出json数据
    areas_list = []
    for area in areas:
        areas_list.append((area.id,area.atitle))
    context = {'data':areas_list}
    print('context',context)
    return JsonResponse(context)

def dis(request,pid):
    '''获取city下级地区的信息'''
    # area = AreaInfo.objects.get(id=pid)
    # areas = area.areainfo_set.all()

    areas = AreaInfo.objects.filter(aParent_id=pid)
    # 2.变量areas并拼接出json数据
    areas_list = []
    for area in areas:
        areas_list.append((area.id,area.atitle))
    context = {'data':areas_list}
    print('context',context)
    return JsonResponse(context)