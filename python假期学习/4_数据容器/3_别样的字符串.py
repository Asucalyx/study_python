temp = "asucalyx"
print(f"原字符串是:{temp}")
print(temp[3])
# 字符串不可修改
num1 = temp.index("x")
print(num1)
# 字符串替换 replace方法
new_temp = temp.replace("x", "X")
print(f"原字符串是:{temp}")
print(f"替换后的新字符串是:{new_temp}")
# 字符串分割成列表 split方法
temp1 = "hello python i like javascript"
new_temp1 = temp1.split(" ")
print(f"原字符串是:{temp1}")
print(f"分割后的新字符串是:{new_temp1}")
# 字符串规整 strip方法
temp2 = " hello python i like javascript12      "
print(f"原字符串是:{temp2}")
new_temp2 = temp2.strip()
print(f"规整后的新字符串是:{new_temp2}")
temp3 = "12hello python i like javascript21"
print(f"原字符串是:{temp3}")
new_temp3 = temp3.strip("12")
print(f"规整后的新字符串是:{new_temp3}")
print("----------------")
lian_xi = "hello ayanami i like asuka"
print(f"原字符串是:{lian_xi}")
count = lian_xi.count("a")
print(f"统计a的数量是:{count}")
lian_xi1 = lian_xi.replace(" ", "|")
print(f"|替换空格后的新字符串是:{lian_xi1}")
lian_xi2 = lian_xi1.split("|")
print(f"分割后的新字符串是:{lian_xi2}")
