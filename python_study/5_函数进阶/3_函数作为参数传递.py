# 函数作为参数传递时，是执行逻辑的传递而不是数据的传递
def temp1(temp2):
    res = temp2(1, 2)
    print(res)


def temp2(x, y):
    return x + y


temp1(temp2)
