"""
    成员方法，即写在类里边的函数
    成员方法必须包括self关键字，但是传参时候可以忽略掉
    在方法内部，想要访问类的成员变量，必须使用self
    def 方法名(self,形参1,...,形参N):
        方法体
"""
class EVA:
    name = None
    age = None
    def say_name(self):
        print(f"我的名字是:{self.name}")
    def say_age(self,msg):
        print(f"我今年{self.age}岁,{msg}")

eva_1 = EVA()
eva_1.name = "asuka"
eva_1.age = 18
eva_1.say_name()
eva_1.say_age("AS")

eva_2 = EVA()
eva_2.name = "ayanami"
eva_2.say_name()
eva_2.age = 18
eva_2.say_age("AY")