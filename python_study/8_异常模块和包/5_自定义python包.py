"""
    python包就是一堆同类型功能模块的集合体，本质上也是模块的一种
    存在__init__.py文件将决定此文件夹是不是包
    导入语法如下:
        import 包名.模块名
        包名.模块名.目标
    __all__写于__init__中
"""
#几种导入方法
# import my_package.new_1
# import my_package.new_2

# my_package.new_1.info_print1()
# my_package.new_2.info_print2()

# from my_package import new_1
# from my_package import new_2
# new_1.info_print1()
# new_2.info_print2()

# from my_package.new_1 import info_print1
# from my_package.new_2 import info_print2
# info_print1()
# info_print2()

#通过__all__控制包的*
# from my_package import *
