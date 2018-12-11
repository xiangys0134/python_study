#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
from urllib import parse,request

def citrix():
    cmd = os.popen("query user")
    l1 = []
    l2 = []
    for i in cmd:
        if '运行中' in i:
            #print(i)
            i = i.replace('\n','')
            str1 = re.sub('\s+',',',i)
            if '>' in str1:
                str1 = str1.replace('>','')
            l1.append(str1)

    for i in l1:
        str2 = i.split(',')
        if re.search('^rdp',str2[1]):
            l2.append(str2[0])

    print(l2)
    # l3 = ['aaa','bbbb','dddd']
    if len(l2) == 1:
        return l2[0]
    else:
        str3 = ','.join(l2)
        return str3




if __name__ == '__main__':
    try:
        header_dict = {
            "User-Agent": 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        }
        url = citrix()
        url = 'admin'
        http_url = 'http://192.168.0.63/pub-uds/monitor/virtual_desk?username=%s' %url

        print(http_url)
        ret = request.Request(url=http_url,headers=header_dict)
        res = request.urlopen(ret)
        print(res.read().decode('utf8'))
    except Exception as e:
        print(e)




