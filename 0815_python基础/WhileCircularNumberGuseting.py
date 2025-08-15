import random
num=random.randint(1,100)
i=1
while True:
    if((gusetNum:=int(input("请输入你猜的数字")))==num):
        break
    else:
        i+=1
        if(gusetNum>num):
            print("大了")
        else:
            print("小了")
print("一共猜了{}次，最终数字是{}".format(i,num))