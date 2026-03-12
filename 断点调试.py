# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 断点调试.py
# @Time : 2026/3/12 11:15

sum = 0
for i in range(10):
    sum += i
    print(f"i = {i}")
    print(f"sum = {sum}")

list = [1, 2, 3, 4, 5]
i = 0
while i < len(list):
    print(list[i])
    i += 1
print("分割线".center(20, "-"))
def f1(x):
    print(x)
    f2(x+1)
    print(x)

def f2(x):
    print( x)
    print(x)
    print( x)

f1(10)