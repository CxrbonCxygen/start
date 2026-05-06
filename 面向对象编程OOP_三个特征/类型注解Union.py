# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 类型注解Union.py
# @Time : 2026/4/22 10:33

# 联合类型注解

# 变量
from typing import Union
a: Union[int, str,  float] = 2.1

# 容器
my_list: list[Union[int, str]] = [1, "2"]

# 函数
def cal(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    return num1 + num2

print(cal(1, 2.134))