dict1=dict([(1,2),(3,4)])#传可迭代的键值对
print(dict1)
dict2=dict(a='1',b='2')#传关键字参数，键值不能是数字
print(dict2)
dict3={1:2,3:4}#话括号直接创建
print(dict3)
'''
数字计算
题目：用字典推导式生成一个字典，键是 1 到 10 的整数，值是它们的平方。
'''
dict4={x:x**2 for x in range(1,11)}
print(dict4)
'''基础型：字符串处理
给定列表 words = ["apple", "banana", "pear", "kiwi"]，用字典推导式生成一个字典，键为单词，值为该单词的长度。
要求：一行完成。
'''
words=["apple","banana","kiwi","pear"]
dict_words={x:len(x) for x in words}
print(dict_words)
'''
条件过滤
给定字典
scores = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 60}
用字典推导式生成一个新字典，只保留分数大于等于 80 的键值对。
'''
scores = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 60}
dic_scores={x:y for x,y in scores.items()if y>80}
print(dic_scores)
'''
类型转换
给定字典
prices = {"apple": "2.5", "banana": "3.0", "pear": "4.2"}
用字典推导式把所有值（字符串类型）转换为浮点数类型。
'''
prices = {"apple": "2.5", "banana": "3.0", "pear": "4.2"}
dict_prices={x:float(y) for x,y in prices.items()}
print(dict_prices)
'''
元组作键
题目：给定两个列表
x_coords = [1, 2, 3]
y_coords = [4, 5, 6]
用字典推导式生成一个字典，键是 (x, y) 坐标元组，值是它们的乘积。
'''
x_coords = [1, 2, 3]
y_coords = [4, 5, 6]
dict_coords={(x,y):x*y for x,y in zip(x_coords,y_coords)}
print(dict_coords)

'''
6️⃣ 键值对交换
题目：给定字典
mapping = {"a": 1, "b": 2, "c": 3}
用字典推导式生成一个新字典，将键和值对调。
'''
mapping = {"a": 1, "b": 2, "c": 3}
dict_mapping={y:x for x,y in mapping.items() }
print(dict_mapping)
'''
7️⃣ 高级：多条件嵌套
题目：给定列表 nums = range(1, 11)，用字典推导式生成一个字典：
键为数字本身
值为 "even" 如果是偶数，"odd" 如果是奇数
但只保留能被 3 整除的数字。
'''
nums=range(1,11)
dict_nums={x:"even" if x%2==0 else "odd" for x in nums if x%3==0}
print(dict_nums)
