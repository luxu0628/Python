import random
num=random.randint(1,10)
if (num1:=int(input("你有三次机会猜0-10的数字，请输入你第一次猜的数字")))==num:
    print("1次就对，牛")
else:
    if num1 < num:
        print("猜小了，再来")
    else:
        print("猜大了，再来")
    if (num2 := int(input("请输入你第二次猜的数字"))) == num:
        print("2次就对，牛")

    else:
        if num2 < num:
            print("猜小了，再来")
        else:
            print("猜大了，再来")
        if int(input("请输入你第二次猜的数字")) == num:
            print("第三次猜对啦")
        else: print(f"您没有机会了,这个数是{num}")
print(f"这个数字是{num}")