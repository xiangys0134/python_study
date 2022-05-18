from django.shortcuts import render,HttpResponse,redirect

from django.conf import settings
from django.core.paginator import Paginator
from django.http import JsonResponse
from domainmanage.models import DomainInfo,Whoiscompany
import re
# Create your views here.

def domainslist(request):
    '''获取域名信息'''
    domains = DomainInfo.objects.all()
    context_list = []

    for domain in domains:
        context_dict = {}
        # if domain.isDelete == True:
        #     continue
        context_dict['name'] = domain.dname
        context_dict['port'] = domain.port

        context_list.append(context_dict)
    data = {'data':context_list}
    return JsonResponse(data,json_dumps_params={'ensure_ascii':False})

def domain_check(domain):
    domain_list = [".com.cn",".net.cn",".org.cn",".ac.cn",".zj.cn",".yn.cn",".sz.cn"]
    for i in domain_list:
        if i in domain:
            ret = re.findall(r'^\w+\.((?:\w+\.)+\w+)$', domain)
            if ret:
                return ret[0]
    ret = re.findall(r'\w+\.(\w+\.\w+)$', domain)
    if ret:
        print(ret[0])
        return ret[0]

def whoisgetlist(request):
    '''获取域名运营商'''
    context_dict = {}

    # 查询出所有域名信息
    domains = DomainInfo.objects.filter(isDeploy=True)
    for domain in domains:
        # 通过域名查询运营商
        whois = Whoiscompany.objects.filter(domaininfo__dname__contains=domain)[0]
        print(whois.name)
        if not re.search(r'^(\w+\.){0,}\w+\.\w+$',domain.dname):
            continue
        # ret = re.findall(r'\w+.(\w+.\w+)$', domain.dname)[0]
        domain = domain_check(domain.dname)
        # print('aaaaa',type(whois.url))
        context_dict[domain] = {'name':whois.name}

    return JsonResponse(context_dict,json_dumps_params={'ensure_ascii':False})





