def judgeTemperature(tem):
    if int(tem)<=37.5:
        print(f"您的体温是{tem}度，体温正常请进")
    else:
        print(f"您的体温是{tem}度，需要隔离！")
def add(a,b):
    '''

    :param a: 形参a加数
    :param b: 形参b加数
    :return:
    '''
    judgeTemperature(a+b)
    return a+b
c=add(10,52)
print(c)
num=200
def testA():
    print(num)
def testB():
    global num
    num=500
    print(num)
testA()
testB()
print(num)