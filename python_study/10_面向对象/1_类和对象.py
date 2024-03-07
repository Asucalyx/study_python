"""
    类 = 属性(数据) + 行为(函数)
    class是关键字，表示要定义类
    类的属性，即定义在类中的变量(成员变量)
    类的行为，即定义在类中的函数(成员方法)
    对象 = 类名称()
"""

#设计类(类比生活中的设计一个表)
class EVA:
    name = None
    age = None
    gender = None
    nationality = None

#创建类(类比生活中的打印一个表)
eva_1 = EVA()
#对对象属性进行赋值(类比生活中的填写一个表)
eva_1.name = "asuka"
eva_1.age = "18"
eva_1.gender = "w"
eva_1.nationality = "JPN"
#获取对象信息
print(eva_1.name)
print(eva_1.age)
print(eva_1.gender)
print(eva_1.nationality)