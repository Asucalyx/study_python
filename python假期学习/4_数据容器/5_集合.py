# 集合不支持重复，内容无序不支持下标访问
temp_set = {"asuka", "ayanami", "asuka", "ayanami", "asuka", "ayanami"}
temp_set1 = {}
print(temp_set)
print(temp_set1)
# add()添加新元素
temp_set.add("asucalyx")
print(f"添加后的集合是:{temp_set}")
# remove()方法移除元素
temp_set.remove("ayanami")
print(f"移除后的集合是:{temp_set}")
# pop()随机取出元素
temp = temp_set.pop()
print(f"取出元素是:{temp},被取出后的集合是:{temp_set}")
# clear()方法清空集合
temp_set.clear()
print(f"移除后的集合是:{temp_set}")
# difference()集合的差集，不会改变原有集合
num1 = {1, 2, 3, 4, 5}
num2 = {4, 5, 6, 7}
num3 = num1.difference(num2)
print(f"{num1}和{num2}的差集:{num3}")
# difference_update()消除差集
num1.difference_update(num2)
print(f"消除差集:{num1}和{num2}")
# 合并集合
num1 = {1, 2, 3, 4, 5}
num2 = {4, 5, 6, 7}
num4 = num1.union(num2)
print(f"合并后:{num4}")
print("-----------------")
lian_xi_list = ["a", "b", "a", "b", "c", "d", "c", "e"]
print(f"原始列表:{lian_xi_list}")
lian_xi = set()
for i in lian_xi_list:
    lian_xi.add(i)
print(f"降重后的集合:{lian_xi}")
