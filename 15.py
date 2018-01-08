zhanghao = 123456
mima = 'abc'
zhanghao1 =int(input("请输入账号"))
mima1 = input("请输入密码")
if zhanghao1 == zhanghao and mima1 == mima:
    print("登录成功")
elif zhanghao1 != zhanghao:
    print("账号不正确")
elif mima1 != mima:
    print("密码不正确")
