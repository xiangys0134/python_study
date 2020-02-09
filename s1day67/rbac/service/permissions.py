#!/user/bin/env python3
# -*- coding: utf-8 -*-


def permission_init(request,user_obj):
    # 获取当前登录用户的所有权限

    ret = user_obj.roles.all().values("permission__url").distinct()
    print(ret)

    permission_list = []

    for per in ret:
        permission_list.append(per["permission__url"])

    request.session["permission_list"] = permission_list
