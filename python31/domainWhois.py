#!/user/bin/env python3
# -*- coding: utf-8 -*-

import whois,os,csv
from datetime import datetime

csv_source_dir = r'C:\Users\xiangys0134\Desktop\csv操作\csv'
# csv_source_dir = '/data/domain/csv/source_dir'
csv_dir = r'C:\Users\xiangys0134\Desktop\csv操作'
#csv_dir = '/data/domain/csv/'
now = datetime.now().strftime("%Y%m%d%H%M%S")
headers = ['域名','域名到期时间','域名剩余天数']
csv_r_name = 'domain.csv'
csv_w_name = 'domainwhois%s.csv'%now

def domainCheck(hostname):
    '''域名到期时间检查'''
    try:
        domain = whois.query(hostname)
        now = datetime.now()
        expir_time = domain.__dict__['expiration_date']
        end_days = (expir_time - now).days

        itemDic = {'域名': hostname, '域名到期时间': expir_time.strftime('%Y-%m-%d'), '域名剩余天数': end_days}

        print(itemDic)
        return itemDic
    except Exception as e:
        print('错误',e)
        itemDic = {'域名': hostname, '域名到期时间': 'whois检查失败，请手工检查!', '域名剩余天数': '检查失败!'}
        return itemDic

with open(os.path.join(csv_source_dir,csv_r_name),'r') as f, \
     open(os.path.join(csv_dir,'%s'%csv_w_name),'w',encoding='utf-8',newline='') as f1:
    csv_reader = csv.reader(f)
    csv_writer = csv.DictWriter(f1,fieldnames=headers)
    csv_writer.writeheader()

    # # 构造字典
    # itemDic = {'域名': 'blog.g6p.cn', '证书到期时间': '2022-06-19', '证书剩余天数': 90}
    for line in csv_reader:
        print(line)
        if len(line) == 0: continue
        if line[0] == '域名': continue
        if line[0] == '': continue
        if '#' in line[0]: continue

        if len(line) == 1:
            ret = domainCheck(*line)
        else:
            ret = False
        if ret:
            csv_writer.writerow(ret)
    print('检查完毕，csv表格路径：%s'%os.path.join(csv_dir,csv_w_name))