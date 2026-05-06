# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 类型注解 typing.py
# @Time : 2026/4/21 13:55


def fun1(a: str):
    for ele in a:
        print( ele)


fun1("100")
print("-"*20)

# 变量类型注解
"""
    n1: int :n1进行类型注解，标注n1的类型为int
    给的跟标注的不一致，会给出黄色警告
"""
n1: int = 10

class Cat:
    pass

# 类的类型注解
cat: Cat = Cat()

# 容器类型注解
# 列表是有序的，可以存重复数据，可以修改，通常存相同类型元素
my_list: list = [1, 2, 3]
# 元组有序，可以存放重复数据，不可变长度固定
my_tuple: tuple[str, int, float] = ("1", 2, 3.6)
# 字典是无序的，可以存放重复数据，键值对，键唯一
my_dict: dict[str, int] = {"name": "CarbonOxygen", "age": 18}
# 集合是无序的，元素不重复，所以不能指定位置注解
my_set: set[int] = {1, 1, 2.2}


# 注释中使用类型注解
n3 = 89.9 # type: float
my_list3 = [1, 2, 3] # type: list[int]

print("-"*20)


# 函数类型注解
def fun1(name: str):
    for ele in name:
        print(ele)


fun1("CarbonOxygen")

print("-"*20)

# 对a，b进行类型注解，返回值进行类型注解
def fun2(a:int,b:int) -> int:
    return a + b

print(fun2(1,2))
# 类型注解是提示性，不强制

