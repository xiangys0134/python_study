#!/user/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

from dateutil.relativedelta import relativedelta
now = datetime.now()

r = datetime.strptime('1996-09-08','%Y-%m-%d')

a = relativedelta(now,r)
print(a.years,a.months)