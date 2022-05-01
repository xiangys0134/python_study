#!/user/bin/env python3
# -*- coding: utf-8 -*-
import csv

with open(r'C:\Users\xiangys0134\Desktop\csv操作\aaa.csv','r') as f, \
     open(r'C:\Users\xiangys0134\Desktop\csv操作\new.csv','w',encoding='utf-8',newline='') as f1:
    csv_reader = csv.reader(f)
    w_headers = ['域名','到期时间','剩余天数']
    csv_writer = csv.DictWriter(f1,fieldnames=w_headers)
    csv_writer.writeheader()

    # 构造字典
    itemDic = {'域名': 'blog.g6p.cn', '到期时间': '2022-06-19', '剩余天数': 90}
    for line in csv_reader:
        if line[0] == '域名': continue
        if line[0] == '': continue
        if '#' in line[0]: continue
        print(line)
    csv_writer.writerow(itemDic)

