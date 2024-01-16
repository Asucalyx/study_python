# for循环可以实现遍历
temp_str = "my name is asuka"
print(temp_str)
num1 = 0
for x in temp_str:
    if x == "a":
        num1 += 1
print(f"本句话有{num1}个a")
print("****************")
# range是左闭右开，后面是步数,i临时变量严格意义上只在内部使用，不应该在外部调用
num2 = 0
for i in range(1, 100):
    if i % 2 == 0:
        num2 += 1
        print(i, end=" ")
print()
print(f"有{num2}个偶数")
print("********************")
# continue 跳过本次循环
for i in range(1,3):
    print("语句1")
    for j in range(1,3):
        print("语句2")
        continue
        print("语句3")
print("*******************")
# break 直接终止循环
for i in range(1,10):
    print("语句1")
    break
    print("语句2")
print("语句3")

