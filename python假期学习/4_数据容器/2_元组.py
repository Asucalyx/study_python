# 元组就是不可修改，只读的列表
temp_tuple = ("asuka", 18, True, ("asuka", 18, True))
print(temp_tuple, type(temp_tuple))
num = temp_tuple[3][2]
print(num)
temp_index = temp_tuple.index("asuka")
print(temp_index)
temp_count = temp_tuple.count("asuka")
print(temp_count)
temp_len = len(temp_tuple)
print(temp_len)
index = 0
while index < temp_len:
    print(temp_tuple[index])
    index += 1
for index in temp_tuple:
    print(index)
# 元组内的列表的内容是可以修改的
temp = ("asuka", 18, ["asuka", "ayanami"])
temp[2][1] = "Ayanami"
print(temp)
print("-----------------------")
lian_xi = ("asuka", 18, ["music", "game"])
print(lian_xi)
num1 = lian_xi.index(18)
print(num1)
print(lian_xi[0])
# 删除元组内列表元素
del lian_xi[2][0]
print(lian_xi)
# 修改元组内列表元素
lian_xi[2].append("coding")
print(lian_xi)
