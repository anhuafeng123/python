accond1 = 123456789
pwd1 = 'woshishuge'
money1 = 1000
nom = 0
while nom <=4:
    accond = int(input("请输入账号"))
    pwd = input("请输入密码")
    if accond == accond1 and pwd == pwd1:
        print("账号密码输入成功")
        mode = int(input("请选择：1存 2取"))
        if mode == 2:
            money = int(input("请输入金额"))
            if money > money1:
                print("没钱，取毛线啊！")
            elif money < money1:
                print("取款:%d元,余额：%d元"%(money,money1-money))
        elif mode == 1:
            money2 = int(input("请输入金额"))
            if money2 > 0:
                print("存款:%d,余额:%d"%(money2,money2+money1)) 
    else:
        print("非法账户")
    nom+1

