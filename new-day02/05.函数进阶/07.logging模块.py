#!/usr/bin/env python
# -*- coding:utf-8 -*-


import logging

logger = logging.getLogger()

#创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log',encoding='utf-8')

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
fh.setLevel(logging.DEBUG)

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)   #Logger对象客户添加多个fh和ch对象
logger.addHandler(ch)


# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#     datefmt='%a,%d %b %Y %H:%M:%S',
#     filename='./test.log',
#     filemode='w',
# )

logger.debug('这是一条debug日志')
logger.info('这是一条info日志')
logger.warning('这是一条warning日志')
logger.error('这是一条error日志')
logger.critical('这是一条critical日志')


