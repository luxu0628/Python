'''
题 1：基本变量替换

用三种方法（%、.format()、f-string）输出：

我叫小红，钱包里有58.75元


变量：

name = "小红"
money = 58.75
'''
name = "小红"
money = 58.75
print("我叫%s,钱包里有%8.2f元"%(name,money))
print("我叫{0},钱包里有{1:8.2f}元".format(name,money))
print(f"我叫{name},钱包里有{money:8.2f}元")
print(f"我叫{name}，买了3杯咖啡后，钱包还剩{(money-3*12.5):8.2f}元")
num=1234567.89
print("账户余额为{0:,.2f}".format(num))
