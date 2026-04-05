# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 包.py
# @Time : 2026/3/12 15:56

# 导入包下的模块
import c_package.module01
import c_package.module02

# 使用导入的模块
c_package.module01.hi()
c_package.module02.ok()

# from 包名   import 模块， 这种方式导入模块，使用模块中的方法，不用带包名
from c_package import module01

module01.hi()

# from 包名.模块 import 方法
# from 包名.模块 import *
# 用上面方法导入包的模块的指定函数、类、变量，模块名都不用写
from c_package.module01 import hi
hi()
from c_package.module02 import ok
ok()
