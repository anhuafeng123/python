def chakan():
    name = input("请输入您要查询的账号")
    for i in list:
        if i["账号"] == name:
            print("账号:%s,密码:%s"%(i["账号"],i["密码"]))
        else:
            print("不存在")


def xiugai():
    account = input("旧账号")
    passwd =  input("旧密码")
    for i in list:
        if i["账号"] == account and i["密码"] == passwd:
            print("账号:%s,密码:%s"%(i["账号"],i["密码"]))
            i["密码"] = input("新密码")
            print("账号:%s,密码:%s"%(i["账号"],i["密码"]))


            
def shanchu():

    account = inputh("账号")
    for i in list:
        if i["账号"] == account:
            list.remove(i)
        else:
            print("没有这个人")



def juding():
    xuanze = int(input("请选择您的权限:1.查看 2.修改 3.删除 4.退出"))
    if xuanze == 1:
        chakan()
    if xuanze == 2:
        xiugai()
    if xuanze == 3:
        shanchu()
    if xuanze == 4:
        False

def print_changhenge():
    print("           静夜思")
    print("           唐:李白")
    print("         床前明月光")
    print("         疑是地上霜")
    print("         举头望明月")
    print("         低头思故乡")
    kanshu()



def print_jiangjinjiu():
    print("                     将进酒")
    print("                     唐代:李白 作者介绍")
    print("        君不见，黄河之水天上来，奔流到海不复回。")
    print("        君不见，高堂明镜悲白发，朝如青丝暮成雪。")
    print("        人生得意须尽欢，莫使金樽空对月。")
    print("        天生我材必有用，千金散尽还复来。")
    print("        烹羊宰牛且为乐，会须一饮三百杯。")
    print("        岑夫子，丹丘生，将进酒，杯莫停。")
    print("        与君歌一曲，请君为我倾耳听。    ")
    print("        钟鼓馔玉不足贵，但愿长醉不复醒。")
    print("        古来圣贤皆寂寞，惟有饮者留其名。")
    print("        陈王昔时宴平乐，斗酒十千恣欢谑。")
    print("        主人何为言少钱，径须沽取对君酌。")
    print("        五花马，千金裘，呼儿将出换美酒，与尔同销万古愁。")
    kanshu()



def kanshu():
    shiji = int(input("要看那一本 1.将进酒 2.长恨歌 3.退出"))
    if shiji == 1:
        print_jiangjinjiu()
    elif shiji == 2:
        print_changhenge()
    elif shiji == 3:
        False
        

def xuanzefuwu():
    xuanzea = int(input("请输入您要选择的服务类型：1.看书 2.退出 3.修改"))
    if xuanze == 1:
        kanshu()
    elif xuanze == 3:
        xiugai()
    elif xuanze == 2:
        False

def guanliyuan(q,w):
    account = input("账号")
    passwd = input("密码")
    if account == q and passwd == w:
        print("登录成功，管理员上线")
        juding()
    else:
        print("你确定是管理员?")



def zhuce():
    account = input("账号")
    passwd =input("密码")
    if not list:
        dictiouary["账号"]=account
        dictiouary["密码"]=passwd
        list.append(dictiouary)
        print("恭喜您注册成功,并成功登录")
    else:
        ad = False
        for i in list:
            for k,v in i.items():
                if v == account:
                    print("您输入的账号已存在")
                    ad = True
                break
        if not ad:
            dictiouary["账号"]=account
            dictiouary["密码"]=passwd
            list.append(dictiouary)
    
    for i in list:
        print(i)
    xuanzefuwu()        





str = '飓风图书馆'
print(str.center(60,"*"))
list = []
while True:
    dictiouary = {}
    xuanze = int(input("请输入您的选择: 1.注册 2.退出 3.管理员登录 "))
    if xuanze == 1:
        zhuce()
    if xuanze == 2:
        break
    if xuanze == 3:
        guanliyuan('anhuafeng','123456')
