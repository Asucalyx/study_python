from my_utils import str_util
from my_utils import file_util
s = "abcdefg"
s1 = str_util.str_reverse(s)
s2 = str_util.substr(s,2,5)
print(s1)
print(s2)

f = "D:/GitHub/study_python/python_study/7_测试文件夹/1_测试"
file_util.print_file_info(f)
print("********************")
f1 = "D:/GitHub/study_python/python_study/7_测试文件夹/9_测试"
file_util.print_file_info(f1)
print("********************")
f2 = "D:/GitHub/study_python/python_study/7_测试文件夹/1_测试"
data = "7这是测试文件\n"
file_util.append_to_file(f2,data)
file_util.print_file_info(f2)
