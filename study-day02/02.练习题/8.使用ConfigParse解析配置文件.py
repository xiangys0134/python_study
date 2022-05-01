#!/user/bin/env python3
# -*- coding: utf-8 -*-
'''
将配置文件放到一个ini文件中方便取到里面的值
my.cnf配置文件如下：
[client]
port = 3306
user = mysql
password = mysql
host = 127.0.0.1

[mysqld]
basedir = /usr
datadir = /var/lib/mysql
tmpdir = /tmp
skip-external-locking

'''

import configparser

cf = configparser.ConfigParser(allow_no_value=True)

cf.read('my.cnf')


print(cf.sections())
print(cf.has_section('client'))
print(cf.options('client'))
print(cf.has_option('client','user'))
print(cf.get('client','host'))


