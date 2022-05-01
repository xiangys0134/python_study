#!/user/bin/env python3
# -*- coding: utf-8 -*-

d = {}
with open('/data/logs/nginx/access_blog.log') as f:
    for line in f:
        key = line.split()[10]
        d.setdefault(key,0)
        d[key] += 1

error_requests = 0
sum_requests = 0
for key,val in d.items():
    if int(key) >= 400:
        error_requests = error_requests + val
    sum_requests += val


print('sum request: %s'%sum_requests)
print('error request: %s'%error_requests)

'''
调用结果：
[root@xiangys0134 tmp]# python3 request.py 
sum request: 35
error request: 0
'''