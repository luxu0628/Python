word=["apple","banana","pear","kiwi",'melon']
new_word1_kind=[fruit for fruit in word if((n:=len(fruit))>4)]
print(new_word1_kind)
new_word2_length=[n for fruit in word if((n:=len(fruit))>4)]
print(new_word2_length)
while(n:=input("请输入你想说的话，按q退出"))!="q" and (n!="Q"):
    print(n)