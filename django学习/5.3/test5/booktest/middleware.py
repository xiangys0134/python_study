#!/user/bin/env python3
# -*- coding: utf-8 -*-
from django.shortcuts import render,HttpResponse,redirect

class BlockedIPSMiddleware(object):
    '''中间件类'''
    EXCLUDE_IPS = ['192.168.124.241']
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in self.EXCLUDE_IPS:
            return HttpResponse('<h1>Forbidden</h1>')
        else:
            response = self.get_response(request)
            return response


    def process_view(self,request):
        '''视图函数调用之前会调用'''
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in self.EXCLUDE_IPS:
            return HttpResponse('<h1>Forbidden</h1>')
