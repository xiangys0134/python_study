#!/user/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter


c = Counter()

with open('/data/logs/nginx/access_blog.log') as f:
    for line in f:
        c[line.split()[5]] += 1

print('*Popular resources: %s'%c.most_common(10))
