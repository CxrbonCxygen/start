# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 运算符.py
# @Time : 2026/1/6 16:25
a = 105
#格式化输出
# %操作符
print("a的值是：        %.5d" %a)
print("%d%%"%a)# %符号输出要用%5
# format
print("a的值    是:   {}".format(a))
print("{}+{}=?".format(a,a,a))# .format可以多，少了会报错
# f-strings
print(f"a的值是：    {a}")

# +用在两边是数值型就是加分 用在字符串就是拼接
b = 150
c = 1.5
name = "cx"
print(a+b)
print("%s" %name)
print(a+b+c)

#算术运算符
a = -10
b = 3
print("加",a+b)
print("减",a-b)
print("乘",a*b)
print('除',a/b)
print('取余',a%b)# 公式a % b = a - a // b * b
print("整除",a//b)# 向下取整
print('幂指数',2**10)

# 97天是几个星期几天
print(f"{97//7}个星期+{97%7}天")
# 华氏度转摄氏度
print(f"{5/9*(234.5-100)}")
print("{0}".format(5/9*(234.5-100)))
print("%.2f"%(5/9*(234.5-100)))

#比较运算符 返回值为bool值
# is   is not 两个对象空间是否为同一个
a = 12
b = 156
if a is not b:
    print("yes")
else:
    print("no")
print(a is not b)

# bool运算符：and or not
if not a or not b:
    print("yes")
else:
    print("no")
x = 10
y = 20
x and y # 短路运算符
# 如果 x 为 false 返回x 否则返回y
x or y # 短路运算符
# 如果 x 为 true 返回 x 否则返回y
not x
# not 只会返回bool型
# 感觉是c的内核
print(not "yes")
print(not 0)

# 复合赋值运算符
i = 100
num1 = 200
i //= 15
print(i)
num1 %= 30
print(num1)

a = 30
b = 40
a += b
b = a - b
a -= b
print(f"交换后：{a},{b}")
a,b = b,a
print(f"再次交换后：{a},{b}")
print(a,b)

# 三元运算符号ternary operator
# 值 if 条件 else 条件
a = 10
b = 20
max = a if a > b else b
print(f"{max}")
c = 30
max = b if b > (a if a > c else c) else (a if a > c else c)
# 嵌套三元运算符
print(f"{max}")

# 优先级
# 算术运算符# () **
# * / // % + -
# 位运算符
# 比较运算符
# 逻辑运算符
# 赋值运算符