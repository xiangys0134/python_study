from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.conf import settings
from booktest.models import PicTest,AreaInfo
import json

# Create your views here.

def index(request):
    return HttpResponse('os')

def static_test(request):
    print(settings.STATICFILES_DIRS)
    return render(request,'booktest/static_test.html')

def index(request):
    '''首页'''
    user_ip = request.META['REMOTE_ADDR']
    print(user_ip)
    return render(request,'booktest/index.html')

def show_upload(request):
    '''显示上传图片页面'''
    return render(request,'booktest/upload_pic.html')

def upload_handle(request):
    '''上传图片处理'''
    pic = request.FILES['pic']
    print(type(pic))

    save_path = '%s/booktest/%s'%(settings.MEDIA_ROOT,pic.name)

    with open(save_path,'wb') as f:
        for content in pic.chunks():
            f.write(content)
    PicTest.objects.create(goods_pic='booktest/%s'%pic.name)
    return HttpResponse('ok')

from django.core.paginator import Paginator,Page
def show_area(request,id):
    '''分页'''
    areas = AreaInfo.objects.filter(aParent__isnull=True)

    paginator = Paginator(areas,2)
    if id =='':
        id = 1
    else:
        id = int(id)
    page = paginator.page(id)
    print(page.number)
    return render(request,'booktest/show_area.html',{'page':page})

def areas(request):
    '''省市县选择案例'''
    return render(request,'booktest/areas.html')

def prov(request):
    '''获取所有省级地区的信息'''
    areas = AreaInfo.objects.filter(aParent__isnull=True)

    area_list = []
    for area in areas:
        area_list.append((area.id,area.atitle))
    return JsonResponse({'data':area_list})


def city(request,id):
    '''获取id的下级地区的信息'''
    # area = AreaInfo.objects.get(id=id)
    #     # areas = area.areainfo_set.all()

    areas = AreaInfo.objects.filter(aParent_id=id)
    area_list = []
    for area in areas:
        area_list.append((area.id,area.atitle))

    return JsonResponse({'data': area_list})


