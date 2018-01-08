account = '123456'
passwd = '1234'
print("*"*80)
print("欢迎来到王者的世界")
print("*"*80)
nom = 0
i = 0
while nom <3 and i == 0:
    myaccount = input("请输入账号")
    mypasswd = input("请输入密码")
    if myaccount == account and mypasswd == passwd:
        print("恭喜你登录成功")
        hero =input("请输入您要选择的英雄类型：1：ADC 2：肉盾 3：法师")
        if hero == 1:
            print("恭喜你获得了英雄后裔")
        elif hero == 2:
            print("恭喜你获得了英雄程咬金")
        elif hero == 3:
            print("恭喜你获得了英雄王昭君")
        i = 1
    elif (myaccount != account) or (mypasswd != passwd):
        print("你输入的账号或密码不正确，请重新输入")
        nom+=1
    if nom == 3 and i == 0:
        i = 1

