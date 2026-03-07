# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 切片.py
# @Time : 2026/3/7 12:47

# 切片
# 从一个序列中，取出一个子序列
# 序列是列表，元组，字符串，内容连续，索引有序
# 语法：[start:end:step]
# 左闭右开
a = [1,2,3,4,5,6,7,8,9,10]
b = (1,2,3,4,5,6,7,8,9,10)
c = "abc","def","ghi","jklmnopqrstuvwxyz"
print(a[1:5])
print(a[:6])
print(a[5:])
print(c[1:10:2])
print(c[::-2])
# 切片不改变原序列
print(c[-3::])
# 左闭右开
