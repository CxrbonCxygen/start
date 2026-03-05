# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 全局变量和局部变量.py
# @Time : 2026/3/5 10:15

# 在函数内部使用global关键字，可以修改全局变量的值
a = 10
def change_a():
    global a
    a = 20
    print(a)
    print(id(a))
    a = 30
print(a)
print(id(a))
change_a()

