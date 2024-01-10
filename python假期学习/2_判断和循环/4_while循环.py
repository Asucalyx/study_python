import random

i = 0
num = random.randint(1, 10)
guess_num = 1
guess = int(input(f"请输入第{guess_num}猜测："))
while guess != num:
    guess_num += 1
    if guess > num:
        print("大了")
        guess = int(input(f"请输入第{guess_num}猜测："))
    else:
        print("小了")
        guess = int(input(f"请输入第{guess_num}猜测："))
print(f"你猜中了，用了{guess_num}次")
