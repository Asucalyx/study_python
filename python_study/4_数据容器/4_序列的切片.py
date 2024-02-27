# 序列指的是内容连续，有序，可以使用下标索引的一类数据容器
# 切片语法: 序列[起始下标:结束下标:步长] 范围左闭右开
temp_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(f"原始列表:{temp_list}")
temp1 = temp_list[1:4]
print(f"1开始4结束的切片:{temp1}")
temp_tuple = (0, 1, 2, 3, 4, 5)
print(f"原始元组:{temp_tuple}")
temp2 = temp_tuple[::]
print(f"从头开始到结束的元组切片:{temp2}")
temp_str = "abcdefg"
print(f"原始字符串:{temp_str}")
temp3 = temp_str[::2]
print(f"从头到尾步长为2的字符串切片:{temp3}")
temp4 = temp_str[::-1]
print(f"反转字符串切片:{temp4}")
temp5 = temp_list[5:1:-1]
print(f"从3到1的反转列表切片:{temp5}")
temp6 = temp_tuple[::-2]
print(f"从头到尾的反转元组切片:{temp6}")
print("----------------------------")
# 正序取出 凌波丽
lian_xi = "香日明欢喜我,丽波凌,好你"
print(lian_xi)
temp_lian1 = lian_xi[::-1][3:6]
temp_lian2 = lian_xi[7:10][::-1]
print(f"先倒后取:{temp_lian1}")
print(f"先取后倒:{temp_lian2}")
temp_lian3 = lian_xi.split(",")
temp_lian4 = temp_lian3[0].replace("我", "|")
temp_lian5 = temp_lian4[::-1]
print(temp_lian3)
print(temp_lian4)
print(temp_lian5)
