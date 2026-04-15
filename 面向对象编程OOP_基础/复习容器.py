# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 复习容器.py
# @Time : 2026/4/8 13:25

print("以下对象的布尔值伪False")
print(bool(0))
print(bool(False))
print(bool(None))
print(bool(""))
print(bool([])) # 空列表
print(bool({})) # 空字典
print(bool(())) # 空元组
print(bool(set())) # 空集合

content = ""
if content:
    print("内容不为空")
else:
    print("内容为空")

lst = [1,2,3]
if lst:
    print("列表不为空")
else:
    print("列表为空")
