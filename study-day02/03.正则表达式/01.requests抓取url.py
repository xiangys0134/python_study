#!/user/bin/env python3
# -*- coding: utf-8 -*-

import re
import requests

r = requests.get('https://blog.g6p.cn/')
re_obj = re.compile(r'"(https?://.*?)"',flags=re.IGNORECASE)

# print(r.content.decode("utf-8"))
obj_list = re_obj.findall(r.content.decode("utf-8"))
print(obj_list)

