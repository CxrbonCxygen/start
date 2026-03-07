# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 容器（集合）.py
# @Time : 2026/3/7 13:04

# 集合
# 集合是无序的，不可重复的
# 集合支持数学运算
set1 = {1, 2, 200, 2, 2, 5, 6, 7, 8, 9, 10}
set2 = {"123","tom","jack","大侠"}
print(set1,type(set1))
# 集合不支持索引, so 不能用while
# print(set1[0])
for i in set2:
    print(i)
# 创建空集合只能用set()，不能用{}
