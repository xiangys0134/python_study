#!/user/bin/env python3
# -*- coding: utf-8 -*-

from redis import StrictRedis

if __name__ == '__main__':
    # 创建一个StrictRedis对象，连接redis数据库
    try:
        sr = StrictRedis(host='192.168.124.241',port=6379,db=0)
        # 添加一个key
        #res = sr.set('name','g6p.cn')
        #print(res)

        # 获取一个字符串key
        # res = sr.get('name')
        # print(res.decode('utf-8'))

        # 修改name的值为itcast
        # res = sr.set('name','itcast')
        # print(res)

        # 删除name对应的值
        res = sr.delete('name')
        print(res)
    except Exception as e:
        print(e)