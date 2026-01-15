# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 标识符.py
# @Time : 2026/1/15 20:27

# 标识符
# 标识符：标识符是程序中用来唯一标识变量、函数、类、模块等的名称。
# 标识符的组成：
# 1. 由字母、数字、下划线组成
# 2. 不能以数字开头
# 3. 不能使用关键字，但可以包含关键字
# 4. 区分大小写，不能有空格

# 类使用大驼峰命名法

# 输入函数input()
name = int(input("请输入你的名字："))
print(type(name))
print("类型转换：",10+float(name))
print("myname:"+str(name))
print(f"你的名字是：{name}")