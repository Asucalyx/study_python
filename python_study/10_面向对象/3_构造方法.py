"""
    python类可以使用__init__()方法，称之为构造方法
    构造方法可以将繁琐的属性赋值简化
    此功能可以实现:
        在创建类对象(构造类)的时候，自动执行
        在创建类对象(构造类)的时候，将传入参数自动传递给__init__()方法使用
"""
class EVA:
    name = None
    age = None
    tel = None
    def __init__(self,name,age,tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("这是构造方法")

eva_1 = EVA("asuka",18,"123456")
print(eva_1.name,eva_1.age,eva_1.tel)