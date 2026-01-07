# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 数据类型.py
# @Time : 2026/1/6 16:23
import math
import sys
from os import name
from sys import flags

# 数据类型
a = "start.cx"
print(a,type("b"))
is_bool = True
if is_bool:
    print(type(is_bool))
print(f"a的值是：{is_bool}\n{type(is_bool)}\n{type(a)}")

# int型可以表示4300个数字
long1 = str(2 ** 14284)
print(len(long1))# python字节很有意思，会自动变长缩短，每次增加缩小是4字节为单位
print(0x10)
print(0o10)
print(0b10)
print(sys.getsizeof(long1),type(long1))

# float型，存在精度损失
n1 = .512
print(n1)
n1 = .512e2
print(n1)
n1 = .512e-3
print(n1)
print(sys.float_info.max)
print(sys.float_info.min)
print(math.ulp(0.0))
print(f"8.3/2.7 = {8.1/3}")# 精度损失
from decimal import Decimal
print(Decimal("8.1")/Decimal("3"))
# bool型
result = "-1"
if result:
    print(True)
else:
    print(False)
# string型"和'有细微区别,不支持单符号c
print("Tom说：' 你好啊！'")
print('Tom说："你好啊！"')
print("""print("Tom说：' 你好啊！'")
print('Tom说："你好啊！"')""")# 三个"、'可以原封不动输出
# 在字符串前面加个r可以让转义符不起作用
str1 = "abcdefg"
print(rf"abc \n {str1}")

# 字符串驻留机制
# python只保留一份相同的字符串值放在字符串池里面
str2 = "abcdefg"
print(id(str1))
print(id(str2))
# 字符串在编译时驻留，而非运行时
a = "abc"
b = "".join(["a","b","c"])
print(a,b)
print(id(a),id(b))
# 整数的-5，256会驻留
a = 5
b = 5
print(id(a),id(b))
# (pycharm会优化)
b = -6
a = -6
print(id(a),id(b))

# 数据类型转换
n1 = 100
result = "abc" + str(n1)
print(result)
# python的类型不固定，可以随时转换，运算转高精度
a = 10.2
print(type(50))
print(a+50,type(a),"\n")
# 数字字符串可以转数值型，但是要逻辑成立
s = "12.3"
print(s,type(s))
s = float(s)
print(s,type(s))

# 练习
print("\\n \\t \\r 1 2 3")
namea = "悲惨世界"
namea_vaue = 30
nameb_value = 50
nameb = "百年孤独"
print(namea + " " + nameb)
print(namea_vaue + nameb_value)

