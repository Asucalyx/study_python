#每个python文件都可以作为模块使用，模块名就是文件名
import my_module1
my_module1.test_my_module(4,5)

#当导入多个模块且模块内有同名功能，当调用这个功能的时候，调用的是后面导入的功能,未被使用的将变灰
from my_module1 import test_my_module
from my_module2 import test_my_module
test_my_module(2,1)

"""
    关于 __main__ 
    使用 if __name__ == '__main__': 语句,系统会将此文件标记为执行文件，从而执行下去
    如果作为模块导入，那么if下面的文件将不会执行,移步my_module2测试此功能
"""
"""
    如果一个模块文件中定义了__all__变量，当使用"from X import *" 时，将只导入这个__all__列表中的元素,只作用于*
"""
#测试__all__，移步my_module3
from my_module3 import *
test_a(2,1)
test_b(2,1)