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
str.split(str, sep=None, maxsplit=-1)