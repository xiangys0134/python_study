#!/user/bin/env python3
# -*- coding: utf-8 -*-

import whois

domain = whois.query("g6p.cn")
print(domain.__dict__)
# print(domain.expiration_date)