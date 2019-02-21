import random
list = []
for i in range(20):
    num=random.choice(range(10))
    list.append(num)
print("list长度：",len(list))
print("未排序list:",list)
list[::2] =sorted(list[::2],reverse=True)
print("排序list:",list)