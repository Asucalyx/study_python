# while循环实现
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{i}*{j}={i * j}", end='\t')
        j += 1
    print()
    i += 1
print("*************")
# for循环实现 \t可以实现对齐
for i in range(1, 10):
    j = 1
    for j in range(1, i + 1):
        print(f"{i}*{j}={i * j}", end='\t')
    print()
