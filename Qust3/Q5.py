s='The column above illustrates apparently' \
  ' the polularity of people ' \
  'doing exercise in a certain year ' \
  'from 2013 to 2018.Based upon the data,' \
  'we can see that python is wonderful. ' \
  'python is wonderful. Python '
zi={}
s=s.split(" " or "," or ".")
print(s)
for i in s:
    zi[i]=len(i)
print(zi)
key=[]
val=[]
for i in zi:
    key.append(i)
    val.append(zi[i])
print(key)
print(val)
val.sort()
nzi={}
for i in range(len(key)):
    for j in key:
        if val[i]==len(j):
            nzi[j]=val[i]
print("最终结果",nzi)
