# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 函数.py
# @Time : 2026/1/19 12:23
from nt import scandir


# 位置参数
# 传递的参数必须按照函数定义的参数顺序进行传递
# 且参数个数必须与定义的参数个数一致
def car_info(name, price, color):
    print(f"车名： {name}")
    print(f"价格： {price}")
    print(f"颜色： {color}")

car_info("保时捷", "1000000", "黑色")

# 6.函数可以返回多个值

# 7.函数支持关键字参数

def book_info(name, author, price):
    print(f"书名： {name}")
    print(f"作者： {author}")
    print(f"价格： {price}")

book_info(name="《Python 3.7 语言基础》", price="49.9",author="王蒙")

# 8.默认（缺省参数）
# 可以给函数提供默认参数，当调用函数时，如果没有提供参数，则使用默认参数
def book_info2(name, author="李蒙", price="69.9"):
    print(f"书名： {name}")
    print(f"作者： {author}")
    print(f"价格： {price}")
book_info2("《Python 3.7 语言基础》","","66")
# 默认参数需要用在函数的末尾

# 9.*号代表0到多，函数支持可变参数、不定长参数
def book_info3(*args):
    print(f" args->{args}")
    print(f"class->{type(args)}")
    for i in args:
        print(i, end=" ")

book_info3(1,2,3,4,5)
print( ""  )

# 10.函数支持可变参数、不定义参数 还支持多个关键字参数
def book_info4(**args):
    print(f"args->{args}")
    print(f"class->{type(args)}")
    for i in args:
        print(f"参数{i}的值为：{args[i]}")
book_info4(name="《Python 3.7 语言基础》", author="王蒙", price="69.9")

# 11.调用另一个.py文件中的函数
# import xx.py
import 导入函数
a = int(input("a为："))
b = int(input("b为："))
print(f"a+b的和结果是：{导入函数.adds(a, b)}")
