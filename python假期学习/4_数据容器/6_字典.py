# 可以通过key找到对应的value, key不可以重复 ,key不可以是字典 ， value任意 ， 没有下标索引
# 定义字典
my_dict = {"key1": 1, "key2": 2, "key3": 3}
temp = dict()
print(f"字典内容:{my_dict} , 类型为{type(my_dict)}")
# 字典取值
temp1 = my_dict["key2"]
print(f"取得字典的值:{temp1}")
# 嵌套字典
my_socre = {
    "asuka": {
        "语文": 99,
        "数学": 98,
        "日语": 99,
    },
    "ayanami": {
        "语文": 89,
        "数学": 88,
        "日语": 89,
    }
}
print(f"嵌套字典:{my_socre}")
temp2 = my_socre["asuka"]["数学"]
print(f"嵌套字典值:{temp2}")
# 字典新增/更新元素
temp = {"asuka": 2 , "ayanami" : 1}
temp["xinji"] = 0
print(f"字典新增/更新元素:{temp}")
# 字典删除元素
value = temp.pop("xinji")
print(f"字典删除元素:{temp},删除的元素:{value}")
# 获取字典全部key值
keys = temp.keys()
print(f"字典的全部key:{keys}")
# 遍历字典
for key in keys:
    print(f"1遍历字典的key:{key}")
    print(f"1遍历字典的值:{temp[key]}")
for i in temp:
    print(f"2遍历字典的key:{i}")
    print(f"2遍历字典的值:{temp[i]}")


# 字典清空元素
temp.clear()
print(f"字典清空元素:{temp}")