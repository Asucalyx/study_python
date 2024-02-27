# 非匿名函数可以重复调用，匿名不用变量接受的话只执行一次,且函数体只能写一行
lambda x,y: x+y

def temp(num):
    res = num(1,2)
    print(res)

temp(lambda x,y: x+y)
