"""
    捕获异常的基本语法
    try:
        可能发生错误的代码
    except Exception as e:
        如果出现异常执行的代码
"""
#自行解除注释使用 ！！！
#捕获单个异常
# try:
#     f = open("D:/GitHub/study_python/python_study/7_测试文件夹/6_异常捕获测试","r",encoding="UTF-8")
# except:
#     print("出现异常,将更改文件打开模式")
#     f = open("D:/GitHub/study_python/python_study/7_测试文件夹/6_异常捕获测试", "w", encoding="UTF-8")
#捕获指定异常 于except后面写需要捕获的异常类型
# try:
#     print(name)
#     1/0
# except NameError as i:
#     print("出现变量未定义异常")
#     print(i)
#捕获多个异常 于except后开括号写入异常类型，
# try:
#     print(name)
#     1/0
# except(NameError,ZeroDivisionError) as i:
#     print("出现变量未定义异常或除零异常")
#     print(i)
#捕获全部异常 except后面啥都不写将捕获全部异常，也可以用except Exception来捕获全部异常
# try:
#     print(name)
#     1/0
# except Exception as i:
#     print("出现变量未定义异常或除零异常")
#     print(i)
#异常的else语法 可写可不写
# try:
#     print("hello")
# except Exception as i:
#     print("出现变量未定义异常或除零异常")
#     print(i)
# else:
#     print("没有异常")
#异常的finally语法 无论如何都将执行finally
？
