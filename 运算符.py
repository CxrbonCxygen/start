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
