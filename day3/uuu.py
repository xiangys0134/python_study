#!/usr/bin/python
li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
tb1 = []
for i in  li:
    i = i.strip()
    if (i.startswith('A') or i.startswith('a')) and i.endswith('c'):
        tb1.append(i)

print(tb1)
