#异常具有传递性 带年纪报错行可以理解传递性
#定义一个出现异常的函数
def func1():
    print("func1开始执行")
    #num = 1 / 0
    print("func1结束执行")
#定义一个无异常的函数
def func2():
    print("func2开始执行")
    func1()
    print("func2结束执行")
#定义主函数调用
def main():
    try:
        func2()
    except Exception as e:
        print(f"出现异常，异常的信息是:{e}")

main()