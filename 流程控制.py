# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 流程控制.py
# @Time : 2026/1/17 10:49
# 顺序控制
print("顺序控制")
print(1)
print(2)
print(3)
# 分支控制
# if 1 > 2: # 每个代码块缩进要相同
#     print("3大于2")
# print("3小于2")
# age  = int(input("请输入年龄："))
# if age >= 18:
#     print("你已成年")
# elif age >= 16:
#     print("你已青少年")
# else:
#     print("你未满16岁")

# 嵌套分支

# 循环分支
num = [1,2,3,4,5]
print(num, type(num))
for i in [1,2,3,4,5]:
    print(i,id(i))
print(id(num[0]))
print(id(1)) # 内存驻留
num1 = [1,1,1,1,1]
print(f"{id(num1[0])}\n{id(num1[1])}")
# range函数 生成列表 是不可变序列类型
# char range(start(默认为0), stop, step(默认为1))
r1 = range(1,5,2)
print(list(r1))
for i in  range(10) :
    print(i)
    break
else:
    print("循环结束")
print("")

# while 循环
i = 0
while i<101:
    if i % 3 == 0:
        print(i)
    i += 1
sum = 0
count = 0
for i in range(1,101):
    if i % 9 == 0:
        print( i)
        sum += i
        count += 1
print(f"1-100的9的倍数和为{sum},个数为{count}")
i = 0
# num = int(input("请输入一个整数："))
# while i <= num:
#     print(f"{i} + {num-i} = {num}")
#     i += 1

# 打印金字塔
# 1.先打印矩形，固定层数
n = int(input("请输入行数："))
for i in range(n):
    for j in range(n):
        print("*", end="")
