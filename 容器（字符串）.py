# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 容器（字符串）.py
# @Time : 2026/3/5 18:14
from operator import ifloordiv

print("---------------------------------------------")
print(ord("a"))
print(chr(97))

print("""
ccc
ccc
ccc



ccc

""")

strc = "ccxxzz"
print(strc.count("c"))
for i in strc:
    print(i)
print("--------------------------")
i = 0
while i < len(strc):
    print(i)
    print(strc[i])
    i += 1
print("="*20)
# 字符串是不可变
print(strc[3])
# strc[3] = "d"
print(id(strc))
strc = "123456"
print(id(strc))
strc = "ccxxzz"
print(id(strc))
print("--------------------------")
# 字符串操作
# str.replace(old, new[, count]) 替换字符串
str_name = "Tom  Tom is my name12356"
# 此操作不会改变原字符串，会返回一个新的字符串
print(str_name.replace("Tom", "Jerry"),id(str_name.replace("Tom", "Jerry")))
print(str_name,id(str_name))
print(str_name.replace("Tom", "Jerry", 1),id(str_name.replace("Tom", "Jerry", 1)))
# str.split(sep=None, max split=-1)
# 返回一个列表，使用sep 作为分隔符，默认为所有的空字符，包括空格、制表符、换行符等
# 此操作不会改变原字符串
print(str_name.split())
print(str_name.count("Tom"))
print(str_name.index("Tom"))
# str.strip([chars]) strip() 方法会从两端开始删除字符，直到遇到不匹配的字符就停止。
print(str_name.strip("1536"))
print(str_name.lower())
print(str_name.upper())
print("------------------------------")
# 字符串的比较
# 两个字符串比较的是字符的ASCII码值
# ord(ch)是字符串对应的ASCII码
# chr(num)是ASCII码对应的字符串
print(ord("a"))
print(chr(97))
print("a" < "b")
str_name = "tom jack mary NoNo Smith Hsp 大侠"
print(f"一共有{len(str_name.split())}个人名")
print(f"把hsp替换为ccxxzz，结果是：{str_name.replace('Hsp', 'ccxxzz')}")
# 如果是英文名就把首字母大写
str_name_list = str_name.split()
str_name_new = ""
for i in str_name_list:
    if i.isalpha() :
        str_name_new += i.capitalize() + " "
print(str_name_new)