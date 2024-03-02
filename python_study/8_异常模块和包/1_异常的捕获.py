"""
    捕获异常的基本语法
    try:
        可能发生错误的代码
    except:
        如果出现异常执行的代码
"""
#捕获单个异常
try:
    f = open("D:/GitHub/study_python/python_study/7_测试文件夹/6_异常捕获测试","r",encoding="UTF-8")
except:
    print("出现异常,将更改文件打开模式")
    f = open("D:/GitHub/study_python/python_study/7_测试文件夹/6_异常捕获测试", "w", encoding="UTF-8")
#捕获指定异常
