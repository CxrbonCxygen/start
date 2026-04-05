# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 容器（集合）.py
# @Time : 2026/3/7 13:04

# 集合 是可修改的
# 集合是无序的，不可重复的
# 集合支持数学运算
set1 = {1, 2, 200, 2, 2, 5, 6, 7, 8, 9, 10}
set2 = {1,2,2,2,6,7,8,"123","tom","jack","大侠"}
print(set1,type(set1))
# 集合的输出不确定
# 集合不支持索引, 所以 不能用while
# print(set1[0])
for i in set2:
    print(i)
# 创建空集合只能用set()，不能用{}
print(len(set1))
print(200 in set1)
set1.add(100)
print(set1)
set1.remove(100)
print(set1)
print(set1.pop())
print(set1)
set1.clear()
print(set1)
# 集合生成式
# {集合元素表达式 for 自定义变量 in 可迭代对象}
set3 = {i for i in range(10)}
print(set3)
j = 10
set4 = {i + j for i in range(10) if i % 2 == 0}
print(set4)
#
