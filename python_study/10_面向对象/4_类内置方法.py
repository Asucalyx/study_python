#内置的类方法各有各的特殊功能,称之为魔术方法
#__str__字符串方法 控制对象转换字符串行为 相当于Java的toString方法
#__lt__小于符号比较方法 顾名思义
#__le__小于等于符号比较方法 顾名思义
#__eq__比较运算符实现方法 顾名思义 默认比较内存地址
class EVA:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"EVA类对象，name:{self.name},age:{self.age}"
    def __lt__(self, other):
        return self.age < other.age
    def __le__(self, other):
        return self.age <= other.age
    def __eq__(self, other):
        return self.age == other.age

eva_1 = EVA("asuka",18)
print(eva_1)
print(str(eva_1))
print("***************")
eva_2 = EVA("ayanami",11)
print(eva_1 < eva_2)
print("***************")
eva_3 = EVA("shinji",11)
print(eva_2 <= eva_3)
print("***************")
eva_4 = EVA("ayaka",11)
print(eva_1 == eva_4)