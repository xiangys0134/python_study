#!/user/bin/env python3
# -*- coding: utf-8 -*-

ips = []
with open('/data/logs/nginx/access_blog.log') as f:
    for line in f:
        ips.append(line.split()[0])

print('*PV is %s'%(len(ips)))
print('*UV is %s'%(len(set(ips))))

'''
调用结果：
[root@xiangys0134 tmp]# python3 pv.py 
*PV is 2649106
*UV is 790

'''