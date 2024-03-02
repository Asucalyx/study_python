#案例目标 备份一个文件，同时删除里面的测试行
#打开文件准备读取
fr = open("D:/GitHub/study_python/python_study/7_测试文件夹/4_案例原文件","r",encoding="UTF-8")
#准备写入
fw = open("D:/GitHub/study_python/python_study/7_测试文件夹/5_案例备份文件","w",encoding="UTF-8")

for i in fr:
    i = i.strip() #清除文件前后换行符
    temp = i.split(",")[-1]
    if temp == "测试":
        continue
    fw.write(i)
    fw.write("\n")
fr.close()
fw.close()

