try:
    print("请输入你的手机号")
    a=int(input())
    c=str(a)
    b=len(c)
    if len(c)==11:
        print("号码验证通过")
    else:
        print("号码不存在")
except ValueError:
    print("请输入正确的手机号")