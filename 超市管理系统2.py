

def tuichu():
    print("退出")
    


def shanchu():#删除
    shangpinga = input("请输入你要删除的商品:")
    for i in list:
        if i["商品"] == shangpinga:
            list.remove(i)
            print("已成功删除您选择的商品")
            quanxian()
        else:
            print("没有这个商品")
            break



def chazhao():#查找
    shangping = input("请输入你要查询的商品:")
    for i in list:
        if i["商品"] == shangping:
            print("商品:%s\n价格:%s\n"%(i["商品"],i["价格"]))
            quanxian()
        else:
            print("没有这个商品，不好意思!")
            break
            

def zengjia():#增加
    zidian = {}
    shangpi = input("商品名:")
    jiage = input("价格:")
    zidian["商品"]=shangpi
    zidian["价格"]=jiage
    list.append(zidian)
    print("请在确定一遍")
    for i in list:
        if i["商品"]==shangpi and i["价格"]!=jiage:
            print("商品已存在,请重新添加")
            break
    shangpi = input("商品名:")
    jiage = input("价格:")
    zidian["商品"]=shangpi
    zidian["价格"]=jiage
    list.append(zidian)
    print("添加成功")
    quanxian()

def xiugai():#修改
    shangp = input("商品")
    for i in list:
        if i["商品"] == shangp:
            print("商品:%s\n价格:%s元"%(i["商品"],i["价格"]))
            i["商品"]=input("修改后的商品名:")
            i["价格"]=input("修改后的价格:")
            print("商品:%s\n价格:%s元"%(i["商品"],i["价格"]))
            quanxian()
        else:
            print("没有这个商品")
            break

def quanxian():#管理者权限
    qx = int(input("请输入你要执行的要求: 1.修改 2.增加商品 3.查找商品 4.删除商品 5.退出"))
    if qx == 1:
        xiugai()
    if qx == 2:
        zengjia()
    if qx == 3:
        chazhao()
    if qx == 4:
        shanchu()
    if qx == 5:
        tuichu()
        False
def guanli(a,b):#管理者
    accounts = input("账号")
    passwds = input("密码")
    if accounts == a and passwds == b:#判断是否相等
        print("管理者上线")
        quanxian()
    else:
        print("您不是管理者？？？")



def putong():#普通用户
    account = input("账号")
    passwd = input("密码")
    if len(int(account)) < 8 and len(int(passwd)) < 6:#判断是否符合要求
        print("登录成功")
    else:
        print("不符规定")


stra = "飓风好友水果超市"
print(stra.center(40,"*"))
xz = input("选择您的要求：1.普通登录 2.管理者登录 3.退出")
list = [{"商品":"香蕉","价格":2},{"商品":"苹果","价格":2},{"商品":"葡萄","价格":3},{"商品":"橘子","价格":2},{"商品":"香橙","价格":2},{"商品":"哈密瓜","价格":3},{"商品":"西瓜","价格":2}]
while True:
    if xz == '1':
        putong()#普通用户
    if xz == '2':
        guanli("anhuafeng","123456")#管理者
    if xz == '3':
        print("退出系统")
        break
