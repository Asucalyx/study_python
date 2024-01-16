# 列表可以一次性容纳多个数据，上限为2^63-1，可以嵌套
name = ["asuka", 18, True, ["asuka", 18, True]]
print(name, name[1], name[-2], name[3][1], type(name))
print("-----------------")
"""
    指定元素查找 .index(查找元素)方法
    尾部追加单个元素 .append(追加元素)方法，追加的元素可以是数据容器
    统计指定元素数量 .count(统计元素)方法
    插入指定元素到指定位置 .insert(插入下标位置,内容)方法
    修改
"""
# 增删改查
# 函数写在class类里面的话叫方法，只是调用方式不一样
temp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
print(f"原始列表:{temp}")
temp_index1 = temp.index(4)
temp_index2 = temp.index(1)
print(f"4的位置下表为:{temp_index1}")
print(f"1的位置下表为:{temp_index2}")
# 统计指定元素
count = temp.count(1)
print(f"统计数字:{count}")
# 统计列表元素数量(长度)
temp_len = len(temp)
print(f"列表的元素个数是:{temp_len}")
print(f"原始列表:{temp}")
# 改
temp[6] = "asuka"
print(f"修改后:{temp}")
temp[6] = 7
# 增
temp.insert(1, 0)
print(f"列表插入后:{temp}")
# 追加
temp.append([10, 11, 12])
print(f"追加单个元素后:{temp}")
# 追加Pro
temp_extend = [10, 11, 12]
temp.extend(temp_extend)
print(f"追加列表后:{temp}")
# 删
del temp[9]
print(f"指定删除后:{temp}")
num = 8
temp.pop(num)
print(f"pop方法删除后:{temp}，删除的元素是:{num}")
temp.remove(5)
print(f"删除匹配元素后:{temp}")
temp.clear()
print(f"清空列表后:{temp}")
print("***********************************")
age = [21, 25, 21, 23, 22, 20]
print(age)
# 尾部追加数字31
age.append(31)
print(age)
# 尾部追加新列表
age2 = [29, 33, 30]
age.extend(age2)
print(age)
# 取出第一个元素
num1 = age[0]
print(num1)
# 取出最后一个元素
num2 = age[-1]
print(num2)
# 查找元素31的下标
num3 = age.index(31)
print(num3)
