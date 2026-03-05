# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 容器（元组）.py
# @Time : 2026/3/5 17:14

# tuple 元组
# 元组和列表类似，但是元组不可变
# 元组中的元素可以不同，可以重复，不可修改，不能重新赋值
tuple1 = (1, "two", "three", 4, 5, 5)
print(tuple1, type(tuple1))
i = 0
while i < len(tuple1):
    print(f"第{i+1}个元素是{tuple1[i]}")
    i += 1
print("-----------------------------------------")
for i in tuple1:
    print(f"元素是{i}")
# 空元组
tuple2 = ()
tuple3 = tuple()
print(tuple2, type(tuple2))
print(tuple3, type(tuple3))
# 可以嵌套元组
tuple4 = (tuple1,tuple2,tuple3)
print(tuple4)
# 元组不可修改
# 元组内元素，是列表的可以修改
tuple4 = (tuple1,tuple2,tuple3,[1,2,3])
print(tuple4)
tuple4[3][0] = 4
print(tuple4)
i = 0
while i < 3:
    tuple4[3].append(i)
    i += 1
print(tuple4)
i = 0
while len(tuple4[3]):
    del tuple4[3][i]
print(tuple4)
print("----------------------------------------")
# 定义只有一个元素的元组，需要使用逗号
tuple5 = (1,)
print(tuple5, type(tuple5))
tuple6 = (1)
print(tuple6, type(tuple6))
print("---------------------------------------------")

# 元组常用操作
print(tuple1)
print(len(tuple1))
print(tuple1.count(5))
tuple1 = (1, 2, 3, 4)
print(max(tuple1))
print(min(tuple1))
print(f"3在第{tuple1.index(3)+1}个位置")
print(1 in tuple1)
print(5 in tuple1)