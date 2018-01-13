#王者游戏登录
account1 = "anhuafeng"
passwd1 = 867296291
nom = 0
wo = 0
while nom <= 2 and wo == 0:
    account = input("请输入您的账号")
    passwd = int(input("请输入您的密码"))
    if account == account1 and passwd == passwd1:
        print("恭喜登录成功")
        hero = int(input("请选择英雄：0:ADC 1:肉盾 2:法师"))
        if hero == 0:
            print("您选择的是鲁班大师")
        elif hero == 1:
            print("您选择的是程咬金")
        elif hero == 2:
            print("您选择的是王昭君")
        wo = 1
    if (account != account1) or (passwd !=passwd1):
        print("你输入的账号或密码布正确，请重新输入")
        nom+=1
    if nom > 2 and wo == 0:
        wo = 1
        print("系统繁忙")
