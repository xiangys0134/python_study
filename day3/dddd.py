#!/usr/bin/python
# -*- coding: utf-8 -*-

# av_catalog = {"欧美":{
#             "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
#             "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
#             "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
#             "x‐art.com":["质量很高,真的很高","全部收费,屌丝请绕过"]
#                 },
#             "日韩":{
#                 "tokyo‐hot":["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]},
#             "大陆":{
#                 "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
#                   }
# }
#
# # av_catalog["欧美"]["www.youporn.com"].insert(1,'量很大')
# # print(av_catalog["欧美"]["www.youporn.com"])
# # av_catalog["欧美"]["x‐art.com"][-1:] = []
# # print(av_catalog["欧美"]["x‐art.com"])
# # av_catalog["日韩"]["tokyo‐hot"][1] = av_catalog["日韩"]["tokyo‐hot"][1].upper()
# # print(av_catalog["日韩"]["tokyo‐hot"][1])
#
#
#
# # del  av_catalog["欧美"]["letmedothistoyou.com"]
# # print(av_catalog["欧美"])
#
#
# str1 = "k:1|k1:2|k2:3|k3:4"
# str1 = str1.replace('|',',')
#
# print(str1)





li= [11,22,33,44,55,66,77,88,99,90]
d1 = {}
d1['k1'] = []
d1['k2'] = []
for i in li:
    if i >= 66:
        d1['k1'].append(i)
    else:
        d1['k2'].append(i)

print(d1)















