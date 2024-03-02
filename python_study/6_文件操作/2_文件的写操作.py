#文件写入write()方法 直接调用将会写入缓冲区而非真正写入文件,避免频繁操作硬盘
f = open("D:/GitHub/study_python/python_study/7_测试文件夹/2_测试","w",encoding="UTF-8")
f.write("hello asuka!!!")

#内容刷新flush()方法 将内存中积攒的内容写入硬盘的文件中
f.flush()

#close()方法其实内置了flush()方法
f.close()