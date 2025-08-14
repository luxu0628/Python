'''
清洗 + 转换
raw = {"  Name ": " Alice ", "Age": " 20", "Height(cm)": " 165 "}
# 目标：键去空格并小写，值去空格；能转数字的转成 int，其它保留字符串。
'''
raw = {"  Name ": " Alice ", "Age": " 20", "Height(cm)": " 165 "}
dict_raw={x.strip().lower():int(y.strip()) if y.strip().replace('.','',1).isdigit() else y.strip() for x,y in raw.items()}
print(dict_raw)
'''
按首字母分组
words = ["apple", "apricot", "banana", "blue", "black", "berry"]
# 目标：{'a': ['apple','apricot'], 'b': ['banana','blue','black','berry']}
# 要求：用“推导式 + setdefault/默认字典”等一行或两步内完成（尽量简洁）。
'''
words=["apple","banana","blue","black","berry"]
dict_words={}
[dict_words.setdefault(word[0],[]).append(word) for word in words]
print(dict_words)
'''
筛选并构建索引
users = [
  {"id": 1, "name": "Alice", "age": 19},
  {"id": 2, "name": "Bob", "age": 23},
  {"id": 3, "name": "Cara", "age": 20},
]
# 目标：用推导式生成：{id: name} 只保留 age >= 21 的用户。
'''
users = [
  {"id": 1, "name": "Alice", "age": 19},
  {"id": 2, "name": "Bob", "age": 23},
  {"id": 3, "name": "Cara", "age": 20},
]
dict_users={use['id']:use['name'] for use in users  if use["age"]>=21 }
print(dict_users)

