def menu(name,money):
    str='主菜单'
    str1="查询余额"
    str2="存款"
    str3="取款"
    str4="退出"
    tip="{:<15}[输入{}]\n"
    print("{:*^30}".format(str))
    print("{},你好。欢迎来到家旭银行ATM。请选择操作：".format(name))
    print(tip.format(str1,1)+
          tip.format(str2,2)+
          tip.format(str3,3)+
          tip.format(str4,4)
          )
    while True:
        choice=input("请输入你的选择(按q退出程序)：")
        if choice=="1":
            banlance(name,money)
        elif choice=="2":
            deposit(name,money)
        elif choice=="3":
            withdrawal(name,money)
        elif choice=="4":
            exit(0)
        elif choice.lower().strip()=="q":
            exit(0)
        else:
            print("error")
def banlance(name,money):
    str="余额查询"
    print("{:*^30}".format(str))
    print("{},您好，您的余额还剩{}".format(name,money))
    while True:
        mes = input("按q返回主菜单")
        if mes.lower().strip() == "q":
            menu(name,money)
def withdrawal(name,money):
    str = "取款"
    print("{:*^30}".format(str))
    withdraw=input("{},您好,您现在有{}，您要取多少钱（按q返回主菜单）".format(name,money))
    if withdraw.lower().strip()=="q":
        menu(name,money)
    money-=int(withdraw)
    print("{}，您好，您取款{}元成功".format(name,withdraw))
    print("{},您好，您的余额还有{}".format(name,money))
    mes=input("按q返回主菜单")
    while True:
        mes = input("按q返回主菜单")
        if mes.lower().strip() == "q":
            menu(name,money)
def deposit(name,money):
    str = "存款"
    print("{:*^30}".format(str))
    withdraw = input("{},您好,您现在有{}，您要存多少钱（按q返回主菜单）".format(name, money))
    if withdraw.lower().strip() == "q":
        menu(name,money)
    money += int(withdraw)
    print("{}，您好，您存款{}元成功".format(name, withdraw))
    print("{},您好，您的余额现在有{}".format(name, money))
    while True:
        mes = input("按q返回主菜单")
        if mes.lower().strip() == "q":
            menu(name,money)
