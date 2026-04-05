# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 流程控制.py
# @Time : 2026/1/17 10:49
# 顺序控制
import random
from idlelib.configdialog import changes
from operator import truediv
from turtledemo.rosette import mn_eck

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
# char range(start(默认为0), stop, step(默认为1))
# 打印金字塔
# 1.先打印矩形，固定层数
rows = 5# int(input("请输入行数："))
for i in range(1,rows+1):
    for j in range(rows-i):
        print(" ", end="")
    for j in range(2*i-1):
        if j == 0 or j == 2*(i-1) :
            print("*", end="")
        else:
            print(" ", end="")
    print("")
for i in range(1,rows):
    for j in range(i):
        print(" ", end="")
    for j in range(2*(rows-i)):
        if j == 0 or j == 2*(rows-i-1):
            print("*", end="")
        else:
            print(" ", end="")
    print("")
print("")

# 改用while
rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= rows-i:
        print(" ", end="")
        j += 1
    j = 1
    while j <= 2*i-1:
        if j == 1 or j == 2*i-1 or i == rows:
            print("*", end="")
        else:
            print(" ", end="")
        j += 1
    print("")
    i += 1
print("")
# classs = int(input("请输入要录入几个班学生的分数:"))
# students_sum = 0 # 统计所有班级的总人数
# classs_sum = 0 # 统计所有班级的总分数
# pass_sum_num = 0  # 统计所有班级通过人数
# for i in range(1,classs+1):
#     sum = 0 # 统计一个班的总分数
#     students = int(input(f"请输入第{i}个班级人数："))
#     students_sum += students
#     for j in range(1,students+1):
#         score = int(input(f"输入第{i}个班级第{j}个同学的分数："))
#         sum += score
#         classs_sum += score
#         if score >= 60:
#             pass_sum_num += 1
#     print(f"第{i}个班级的平均分是：{sum/students}")
# print(f"所有班级的平均分是：{classs_sum/students_sum}")
# print(f"所有班级通过人数是：{pass_sum_num}")

# 打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}", end="\t")
    print("")
print("")
count = 0
i = 0
while i <= 100:
    i += 1
    n = random.randint(1,100)
    count += 1
    if n == 100:
        print(f"恭喜你，运气不错！{count}次就找到了100")
        break
    elif n<=10:
        print(f"{n}比10小,此时没找到100，还在while循环内")
else:
    print("循环结束")
print(i)
sum = 0
for i in range(1,101):
    sum += i
    if sum >= 20:
        break
print(i)
changes = 3
# for i in range(changes):
#     name = input("请输入用户名：")
#     password = input("请输入密码：")
#     if name == "admin" and password == "888":
#         print("登录成功")
#         break
#     elif i < changes-1:
#         print(f"还有{changes-1-i}次机会")
#     else:
#         print("登录失败")

money = 100000
count = 0
while True:
    if money <= 1000:
        print("没钱了")
        break
    elif money > 50000 :
        money -= money * 0.05
        count += 1
    else:
        money -= 1000
        count += 1
print(f"可以通过{count}次路口")