# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 匿名函数.py
# @Time : 2026/3/4 18:54

# 匿名函数，只能使用一次
# lambda x,y（参数）:x+y（函数体，只能写一行）
# 不用return
lambda  x,y: x if x > y else y

def f1(fun, num1, num2):
    """
    功能：调用fun，返回num1和num2的最大值
    :param fun: 接收函数(匿名)
    :param num1:
    :param num2:
    :return:
    """
    print(f"fun的类型是{type(fun)}")
    return fun(num1, num2)

max_num = f1(lambda x,y: x if x > y else y, 10, 10.5)
print(max_num)
