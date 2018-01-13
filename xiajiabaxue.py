def xuanze():
    print("八嘎呀路")


def panduan(account,passwd):
    if len(account) < 10 and len(passwd) < 5:
        print("恭喜登录成功")
        xuanze()
    else:
        print("不对")





def shuru():
    account =input("请输入账号")
    passwd = input("请输入密码")
    panduan(account,passwd)
shuru()
