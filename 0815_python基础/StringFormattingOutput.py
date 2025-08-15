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
'''
题 1：多变量对齐 + 精度控制
用三种方法（%、.format()、f-string）输出下面表格：
姓名     钱包余额
小红     58.75
小明    1234.50
小刚  98765.32
要求：
姓名左对齐，占 6 个字符宽
钱包余额右对齐，占 8 个字符宽，保留 2 位小数
'''
name='姓名'
money='钱包余额'
name1='小红'
money1=58.75
name2='小明'
money2=1234.50
name3='小刚'
money3=98765.32
print("{:<6}{:>8}\n{:<6}{:>8.2f}\n{:<6}{:>8.2f}\n{:<6}{:>8.2f}".format(name,money,name1,money1,name2,money2,name3,money3))
print(f"{name:<6}{money:>8}\n{name1:<6}{money1:>8.2f}\n{name2:<6}{money2:>8.2f}\n{name3:<6}{money3:>8.2f}")
print("%-6s%8s\n%-6s%8.2f\n%-6s%8.2f\n%-6s%8.2f"%(name,money,name1,money1,name2,money2,name3,money3))
'''
题 2：表达式计算 + 精度
小红钱包里有 58.75 元，她买了 3 杯咖啡，每杯 12.5 元，输出：
我叫小红，买了3杯咖啡后，钱包还剩XX.XX元
保留 2 位小数
用 .format() 和 f-string 完成
'''
balance=58.75-3*12.5
print("我叫小红，买了3杯咖啡后，钱包还剩{:.2f}元".format(58.75-3*12.5))
print(f"我叫小红，买了3杯咖啡后，钱包还剩{balance:.2f}元")
'''
题 3：千位分隔 + 精度
有一个大数字 num = 12345678.9，输出：
账户余额为 12,345,678.90 元
保留 2 位小数
用 .format() 和 f-string 完成
'''
num = 12345678.9
print("账户余额为{:,.2f}元".format(num))
print(f"账户余额为{num:,.2f}元")
'''
题 4：百分比显示
假设小红的钱包增加了 20%：
increase_rate = 0.2
money = 58.75
输出：
钱包增加了 20.00%
使用 .format() 和 f-string
保留 2 位小数
显示 %
'''
increase_rate = 0.2
money = 58.75
print("钱包增加了{:.2f}%".format(increase_rate*100))
'''
有一组数据：
users = [
    {"name": "小红", "balance": 58.75},
    {"name": "小明", "balance": 1234.5},
    {"name": "小刚", "balance": 98765.32}
]
coffee_price = 12.5
要求输出每个人买 2 杯咖啡后的钱包余额：
小红买了2杯咖啡后余额: 34.75
小明买了2杯咖啡后余额: 1209.50
小刚买了2杯咖啡后余额: 98740.32
每个余额占 10 个字符宽
保留 2 位小数
千位分隔符可选
'''
users = [
    {"name": "小红", "balance": 58.75},
    {"name": "小明", "balance": 1234.5},
    {"name": "小刚", "balance": 98765.32}
]
coffee_price = 12.5
for use in users:
    print("{}买了两杯咖啡后的余额：{:10,.2f}".format(use['name'],(use['balance']-2*coffee_price)))

for use in users:
    print(f"{use['name']}买了两杯咖啡后的余额：{(use['balance'] - 2 * coffee_price):10,.2f}")