#!/user/bin/env python3
# -*- coding: utf-8 -*-

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect
import re

class PermissionMiddleware(MiddlewareMixin):
    def process_request(self,request):
        '''
        一旦请求路径不在当前登录用户的权限列表中，
        :return:
        '''
        #当前请求路径
        current_path = request.path
        print("current_path",current_path)

        #1.放行白名单
        white_list = ['/login/',"/admin/*"]
        for reg in white_list:
            if re.search(reg,current_path):
                return None

        #2.判断是否登陆
        user_id = request.session.get("user_id")

        if not user_id:
            return redirect("/login/")


        # 3校验访问路径是否在该用户权限列表中

        # 3.1获取当前用户的权限列表
        print("permission_list",request.session.get("permission_list"))
        permission_list = request.session.get("permission_list")

        # 3.2正则匹配
        for reg in permission_list:
            reg = '%s$'%reg
            if re.search(reg,current_path):
                return None
        return HttpResponse("您无权限访问!")


        # if current_path not in permission_list:
        #     return HttpResponse("您无权限访问!")