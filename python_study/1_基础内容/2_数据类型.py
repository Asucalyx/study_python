# 数据类型
print(type(1))
print(type(6.6))
print(type(True))
print(type("asuka"))
print("--------------")
a = "asuka"
type_a = type(a)
print(type_a)
print("**************")
# 数据类型转换
print(int(1.6))
print(float(1))
print(str(1.6))
"""标识符命名只有英文 中文 数字 下划线_ 
   大小写敏感
   不推荐中文
   不可以数字开头
   不可以使用关键字
   见名知其意
   简洁
"""
print("**************")
"""字符串有三种定义"""
name1 = 'asuka'
name2 = "asuka"
name3 = """asuka"""
# \转移定义
name4 = "\"asuka"
print(name1, name2, name3, name4)
