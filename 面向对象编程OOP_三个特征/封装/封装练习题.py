# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 封装练习题.py
# @Time : 2026/4/13 12:24

class Account:
    """
    封装练习题
    """
    def __init__(self, __name, __balance, __password):
        if len(__name) < 2 or len(__name) > 4:
            print("警告：用户名长度必须在2-4之间,已默认为admin")
            __name = "admin"
        if __balance <= 20:
            print("警告：余额必须大于20,已默认为20")
            __balance = 20
        if len(__password) != 6:
            print("警告：密码长度必须为6位,已默为123456")
            __password = "123456"
        
        self.__name = __name
        self.__balance = __balance
        self.__password = __password

    def set_name(self, __name):
        self.__name = __name
        print(f"用户名已修改为:{self.__name}")

    def set_balance(self, __balance):
        self.__balance = __balance
        print(f"余额已修改为:{self.__balance}")

    def set_password(self, __password):
        self.__password = __password
        print(f"密码已修改为:{self.__password}")

    def query_info(self, __name, __password):
        if __name == self.__name and __password == self.__password:
            print(f"用户名:{self.__name}")
            print(f"余额:{self.__balance}")
        else:
            print("用户名或密码错误")

account = Account("超级大尾巴", 10, "123456789")
account.query_info("超级大尾巴", "123456789")
account.query_info("admin", "123456")
account.set_name("小尾巴")
account.set_balance(100)
account.set_password("123456")
account.query_info("小尾巴", "123456")