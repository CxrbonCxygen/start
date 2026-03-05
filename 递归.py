# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 递归.py
# @Time : 2026/3/2 17:59
from pygetwindow import pointInRect


def test(n):
    if n > 2 :
        test(n-1)
    print(n)

test(4)
print("----------------------------------------------------------------------------------------------------------------")

# 吃桃子
def peach(day):
    if day == 10:
        return 1
    else:
        return (peach(day+1) + 1) * 2

print(peach(1))

print("----------------------------------------------------------------------------------------------------------------")

def fun(n):
    if n == 1:
        return 3
    else:
        return fun(n-1) * 2 + 1

print(fun(10))
print("----------------------------------------------------------------------------------------------------------------")
# 汉罗塔
def hanoi(n, a, b, c):
    """
    :param n: 盘子
    :param a: 初始柱子
    :param b: 临时柱子
    :param c: 目标柱子
    :return:
    """
    if n == 1:
        print(f"将第1个盘子从{a}--->{c}")
        return
    # 边界条件
    hanoi(n-1, a, c, b) # 函数递归 手动调整使得目标柱子为b
    print(f"将第{n}个盘子从{a}--->{c}") # 移动盘子
    hanoi(n-1, b, a, c)

# n = input("请输入盘子数量：")
# hanoi(int(n), "A", "B", "C")


# 函数可以传递函数
x , y = 1, 1

def max_num(num1, num2):
    max = num1 if num1 > num2 else num2
    return max

def f1(fun, num1, num2):
    return fun(num1, num2)

def f2(fun, num1, num2):
    return fun(num1, num2), num1 + num2

a = f1(max_num, x, y)
b1, b2 = f2(max_num, x, y)
print(f"{a}\n{b1} {b2}")

# 一个函数可以接收多个函数

def fun1(x, y):
    return x + y

def fun2(x, y):
    return x * y

def f3(fun1, x, y, fun2):
    return fun1(x, y), fun2(x, y)
x , y = 1, 1
x, y = f3(fun1, x, y, fun2)
print(f"{x} {y}")