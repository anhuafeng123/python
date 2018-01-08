account = input("请输入您的账号")
password = input("请输入密码")
nick_name = input("请输入姓名")
money = 90000000000#原有的存款
need_money = input("请输入您要提取的金额")
sum = money - int(need_money)
print("账号：%s\n,密码：******\n,姓名：%s\n,原有存款%d\n,取款金额:%s\n,剩余金额%d"%(account,nick_name,money,need_money,sum))
