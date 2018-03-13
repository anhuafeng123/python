

def gm():#普通用户购买
    zzx = input("请输入你要购买的商品:")
    aal = int(input("请属于要的数量"))
    mane = 0
    is_have = False
    for i in list:
        if i["商品"]==zzx:
            is_have = True
            mane=i["价格"]*aal
            print("商品:%s,单价:%s,总共:%s"%(i["商品"],i["价格"],mane))
            break
    if not is_have:
        print("没有这种水果")


def ck():#普通用户查看现有商品
    for i in list:
        print("商品:%s 价格:%s"%(i["商品"],i["价格"]))
        agg = int(input("请问您是直接退出还是够买商品:1.购买 2.退出"))
        if agg == 1:
            gm()
        if agg == 2:
            goumai()    
    


def goumai():#普通用户购买

    ahh = int(input("1.查看现有商品请输入，2.直接购买请输入, 3.退出"))
    if ahh == 1:
        ck()
    if ahh == 2:
        gm()
    if ahh == 3:
       xuanzz() 



def xuanzz():#普通用户选择
    choice = int(input("请选择您的选择:1.购买商品 2.退出"))
    if choice == 1:
        goumai()
    if choice == 2:
        tuichu()
        False    


def tuichu():
    print("退出")
    


def shanchu(list):#管理员删除
    shangpinga = input("请输入你要删除的商品:")
    kg = True
    for i in list:
        if i["商品"] == shangpinga:
            list.remove(i)
            print("已成功删除您选择的商品")
            kg = False
    if kg:
        print("没有这个商品")



def chazhao(list):#管理员查找
    shangping = input("请输入你要查询的商品:")
    isShow =True
    for i in list:
        if i["商品"] == shangping:
            print("商品:%s\n价格:%s\n"%(i["商品"],i["价格"]))
            isShow  = False       
    if isShow:
        print("没有这个商品，不好意思!")
            

def zengjia():#管理员增加
    zidian = {}
    shangpi = input("商品名:")
    jiage = input("价格:")
    zidian["商品"]=shangpi
    zidian["价格"]=jiage
    for i in list:
        if i["商品"]==shangpi and i["价格"]!=jiage:
            print("商品已存在,请重新添加")
            return 
    else:
        list.append(zidian)
        print("添加成功")

def xiugai(list):#管理员修改
    shangp = input("商品")
    wo = True
    for i in list:
        if i["商品"] == shangp:
            print("商品:%s\n价格:%s元"%(i["商品"],i["价格"]))
            i["商品"]=input("修改后的商品名:")
            i["价格"]=input("修改后的价格:")
            print("商品:%s\n价格:%s元"%(i["商品"],i["价格"]))
            wo = False
    if wo:
        print("没有这个商品")

def quanxian():#管理者权限
    while True:
        qx = int(input("请输入你要执行的要求: 1.修改 2.增加商品 3.查找商品 4.删除商品 5.退出"))
        if qx == 1:
            xiugai(list)
        if qx == 2:
            zengjia()
        if qx == 3:
            print(list)
            chazhao(list)
        if qx == 4:
            print(list)
            shanchu(list)
        if qx == 5:
            tuichu()
            return

def guanli(a,b):#管理者登录
    accounts = input("账号")
    passwds = input("密码")
    if accounts == a and passwds == b:#判断是否相等
        print("管理者上线")
        quanxian()
    else:
        print("您不是管理者？？？")



def putong():#普通用户登录
    account = input("账号")
    passwd = input("密码")
    if len(account) < 8 and len(passwd) < 6:#判断是否符合要求
        print("登录成功")
        xuanzz()
    else:
        print("不符规定")


stra = "飓风好友水果超市"
print(stra.center(40,"*"))
xz = input("选择您的要求：1.普通登录 2.管理者登录 3.退出")
list = [{"商品":"香蕉","价格":2},{"商品":"苹果","价格":2},{"商品":"葡萄","价格":3},{"商品":"橘子","价格":2},{"商品":"香橙","价格":2},{"商品":"哈密瓜","价格":3},{"商品":"西瓜","价格":2},{"商品":"杨梅","价格":7},{"商品":"菠萝","价格":6},{"商品":"香瓜","价格":5},{"商品":"枇杷","价格":9},{"商品":"杨桃","价格":8},{"商品":"椰子","价格":7},{"商品":"樱桃","价格":6},{"商品":"荔枝","价格":5},{"商品":"芒果","价格":4}]
if xz == '1':
    putong()#普通用户
if xz == '2':
    guanli("anhuafeng","123456")#管理者
if xz == '3':
    print("退出系统")
