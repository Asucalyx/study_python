def temp_a():
    print(f"直接输出：{num}")


def temp_b():
    num = 500
    print(f"函数内改变参数：{num}")


def temp_c():
    global num
    num = 400
    print(f"函数内global改变参数：{num}")


num = 200
temp_a()
temp_b()
print(f"函数内改变后：{num}")
temp_c()
print(f"函数内global改变参数后：{num}")
