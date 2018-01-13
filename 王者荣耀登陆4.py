count = 123456789
passwd = 12345
for i in range(1,6):
    macount = int(input("请输入账号"))
    mapasswd = int(input("请输入密码"))
    if macount == count and mapasswd == passwd:
        print("欢迎来到王者的世界")

        break
    else:
        print("您输入的账号或者密码错误")
