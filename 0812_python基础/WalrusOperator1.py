import random
def get_number():
    return random.randint(1,100)
while (n:=get_number())<=90:
    print(n)
print(f"最终大于90的数字是{n}")