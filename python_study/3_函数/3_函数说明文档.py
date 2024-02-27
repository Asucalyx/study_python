# 函数内三引号回车后生成说明文档，鼠标悬停可以查看
def add(x, y):
    """
    add函数实现加法
    :param x: 被加数
    :param y: 加数
    :return: 两数之和
    """
    result = x + y
    return result


num1 = int(input("num1:"))
num2 = int(input("num2:"))
num3 = add(num1, num2)
print(num3)
