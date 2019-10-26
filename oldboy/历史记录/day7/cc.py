#!/usr/bin/env python 
# -*- coding: utf-8 -*-

class Uesrname():
    user = 'alex'
    password = 'alex'
    def __init__(self,info):
        self.info = info
        # self.password = password

    def login(self,login_user,login_password):
        print('%s操作###########'%self.info)
        if self.user == login_password and self.password == login_password:
            return '用户登录成功'
        else:
            return '用户登录失败'

abc = Uesrname('登录')
ret = abc.login('alex','alex')
print(ret)