#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
import json
import hashlib

"""
alex:123
zhangsan:123
"""
user = {
    'alex':'123',
    'zhangsan':'123',
}

role = {
    'alex':'User',
    'zhangsan':'User'
}

dir = os.path.dirname(os.path.abspath(__name__))
db_dir = os.path.join(dir,'db')
print(db_dir)

for name,pwd in user.items():
    m2 = hashlib.md5()
    m2.update(user[name].encode('utf8'))
    user[name] = m2.hexdigest()
    print(m2.hexdigest())

with open(os.path.join(db_dir,'user_db'),'w',encoding='utf8') as f:
        user_josn = json.dumps(user)
        f.write(user_josn)

with open(os.path.join(db_dir,'role_db'),'w',encoding='utf8') as f1:
    role_josn = json.dumps(role)
    f1.write(role_josn)

##创建ftp目录
if not os.path.exists(os.path.join(dir,'ftpdata')):
    os.makedirs(os.path.join(dir,'ftpdata'))