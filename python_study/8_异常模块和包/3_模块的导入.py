"""
    模块在使用前需要导入，语法如下:
        [from 模块名] import [模块|类|变量|函数|*][as 别名]
    ctrl+右键点击查看模块文件
    常用组合形式如:
        import 模块名
        from 模块名 import 类、变量、函数等
        from 模块名 import *
        import 模块名 as 别名
        from 模块名 import 功能名 as 别名
    例如:
        import 模块名
        模块名.功能名()
"""
#使用import导入 将导入全部功能
import time
time.sleep(1)
#使用from import 导入 将导入指定功能
from time import sleep
sleep(2)
#使用*导入 将导入全部功能,不需要使用.就可以直接使用
from time import *
sleep(3)
#使用 as导入 将设置别名
from time import sleep as sl
sl(4)