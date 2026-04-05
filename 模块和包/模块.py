# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 模块.py
# @Time : 2026/3/12 12:27

# 导入模块
import math
print(math.fabs(-12.6))
# 导入模块中的方法
from math import (fabs)
print(fabs(-12.6))
# 导入模块所以功能
from math import *
# 导入模块并起别名
import math as 数学
print(数学.fabs(-12.6))

# 自定义模块
# 使用__name__可以避免模块被直接运行

from __name__模块 import *
print("ook")
hi() # 重复输出了
ok()
# 如何解决导入模块会执行测试代码的问题？
print(__name__) # 给自定义模块加个if

# __all__ 可以选择模块是否可以被使用
# 注意：import 方式，不受__all__的影响