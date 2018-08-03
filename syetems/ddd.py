
#encoding=utf-8

import re
f = open("/Users/chenyanghong/SecureCRT/tables.sql", "r")
tbl = {}
one = []
# 生成字典，字典的键为表名，值为字段名
for line in f:
	if "###" in line:  # 读到###的行
		if len(one) != 0:  # 如果one不为空表示已经读取成功一张表
			tbl[one[0]] = one[1:]  # 加入字典，字典健为one[0]第一个元素，值为一个列表，从one[0]第二个元素到最后一个元素
		one = []
	else:
		one.append(line.strip("\n"))
f.close()

table_names = tbl

# 格式化sql语句，入参数为一条记录列表
def parse(tbl):  
	name = tbl[0]  # 取列表第一个元素，第一个元素开头只有三个值 INSERT UPDATE DELETE 后面加库名表名
	add_where = "UPDATE" in name  # UPDATE语句状态
	is_delete = "DELETE" in name  # DELETE语句状态
	name = re.findall("`.*?\.`(.*)`", name)[0] # 取出表名
	if name not in table_names:return # 表名没在字典中直接返回
	# print name
	# print table_names[name]

	data = []
	for line in tbl:
		if "@" in line:
			idx = int(re.findall(".*@([0-9]+)=", line)[0]) - 1  # 字段位置
			# table_names[name][idx] 表名字典中的表名对应的字段位置，需要数据位置一一对应
			line = re.sub(".*@([0-9]+)=", table_names[name][idx] + "=", line) + ","
		data.append(line.replace("\n",""))
	
	if is_delete:  # 如果是delete语句,只需要取前面三段即可
		data = data[:3]
	ret = " ".join(data).strip().strip(",")
	if add_where: # 如果是update,因前面已将where去掉，后面需手动加上主键条件
		ret = ret + " where " + data[2].strip().strip(",")
	print ret + ";" # 最后加;号

# f = '''UPDATE `fxxt`.`user_cards`
#   WHERE
#     @1=6796
#     @2=17723
#     @3=0
#     @4=0
#     @5=35124
#     @6=0
#   SET
#     @1=6796
#     @2=17723
#     @3=0
#     @4=0
#     @5=35184
#     @6=0

# INSERT INTO `fxxt`.`game_orders`
#   SET
#     @1='201707271143114157329'
#     @2=66713
#     @3=0
#     @4=12.00
#     @5=12.00
#     @6=18
#     @7=1
#     @8='65208'
#     @9=''
#     @10=1501126991
#     @11=0
#     @12=3
#     @13=0
#  DELETE FROM `fxxt`.`accounts`
#  WHERE
#    @1=13057
#    @2=29405
#    @3='夏星'
#    @4='362322199511265457'
#    @5='工商银行'
#    @6='洋口支行'
#    @7=17
#    @8=240
#    @9=2036
#    @10='6215581512002757580'
#    @11=NULL
#    @12=NULL
#    @13=1
#    @14=1
# '''.split("\n")

f = open("/Users/chenyanghong/SecureCRT/3.sql", "r")
tbl = []
one = []
skip = False
for line in f:
	if "INSERT" in line or "UPDATE" in line or "DELETE" in line: # 当碰到insert或update或delete语句进行处理
		if len(one) != 0:  # 当one列表不为空，表示已经读取成功了一条记录
			tbl.append(one)
			parse(one)   # 生成mysql
			# if len(tbl) == 10: break
			# break
		one = []  # 清空one以便进行下一轮处理
	if "UPDATE" in line: 
		skip = True  # 更新语句，跳过where这段
		one.append(line)
	elif skip and "SET" in line: # 如果忽略值为真且读到了SET语句，取消忽略
		skip = False

	if not skip: # 忽略状态为假，添加列表
		one.append(line)
		# print one

if len(one) != 0:  # 处理最后一条语句
	parse(one)
f.close()