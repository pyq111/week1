import random
list = []
for i in range(50):
    num=random.choice(range(-10,11))
    list.append(num)

print("list长度：",len(list))

zheng = []
fu = []
for i in list:
    if (i>0):
        zheng.append(i)
    else:
        fu.append(i)
print("正数",zheng)
print("负数",fu)