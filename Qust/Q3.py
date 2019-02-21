import random
a=[random.randrange(100)for i in range(20)]
print("原来的列表",a)
even=a[::2]
print("偶数下标列表",even)
even.sort(reverse=True)
print("降序过后",even)
for i in range(10):
    if i%2==0:
        a[i]=even[i//2]
print("新的列表:",a)