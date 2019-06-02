#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import time
import random

conent = {
            'count':1
           }
conent_dumps = json.dumps(conent)
print(conent_dumps,type(conent_dumps))
with open('db','w',encoding='utf8') as f:
    f.write(conent_dumps)
#
#
# def search():
#     time.sleep(random.randrange(0,5))
#     with open('db','r',encoding='utf8') as f:
#         f = f.read()
#         data = json.loads(f)
#         print('剩余票数：%s' %(data['count']))
#
# search()