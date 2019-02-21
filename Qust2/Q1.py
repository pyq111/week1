phone=input("请输入手机号:")
list = [185,137,136,176,151,153]
try:
    int(phone)
    if (len(phone)==11):
        head=phone[0:3]
        bool = False
        for i in list:
            if (int(head)==(i)):
                bool = True
                break
        if (bool):
            print("有效手机号")
        else:
            print("无效手机号")
    else:
        print("输入的不是有效手机号")
except ValueError:
    print("输入的不是有效手机号")