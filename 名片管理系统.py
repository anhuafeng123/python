def useradd():
    name = input("请输入您的姓名：")
    phone = input("请输入您的联系方式：")
    email= input("请输入您的邮箱：")
    site= input("请输入您的地址：")
    QQ = input("请输入你的QQ：")
    if not list:#判断空列表
        userinfo["姓名"]=name
        userinfo["联系"]=phone
        userinfo["邮箱"]=email
        userinfo["地址"]=site
        userinfo["QQ"]=QQ
        list.append(userinfo)#字典加入到空列表
        print("恭喜添加成功")
    else:#除非不是空列表
        ad = False
        for i in list:
            for k,v in i.items():
                if v == name:
                    print("您输入的重复了")
                    ad = True#如果重复了，就判断为True，如果布重复就跳出循环
                    break
        if not ad:
            userinfo["姓名"]=name
            userinfo["联系"]=phone
            userinfo["邮箱"]=email
            userinfo["地址"]=site
            userinfo["QQ"]=QQ
            list.append(userinfo)
    for i in list:
        print(i)


def delete():
    name1 = input("请输入你要删除的名字：")
    for de in list:
        if de["姓名"] == name1:
            list.remove(de)
            print("已删除")
        else:
            print("没有这个人")



def amend():
    named = input("请选择要修改的名片(输入名字即可)")
    for i in list:
        if named == i["姓名"]:
            print("姓名:%s\n ,联系方式:%s\n ,邮箱:%s\n ,地址:%s\n , QQ:%s\n"%(i["姓名"],i["联系"],i["邮箱"],i["地址"],i["QQ"]))
            i["姓名"]=input("请输入新名字")
            i["联系"]=input("请输入新的联系方式")
            i["邮箱"]=input("请输入新的邮箱")
            i["地址"]=input("请输入新的地址")
            i["QQ"]=input("请输入新的QQ")
            print("姓名:%s\n ,联系方式:%s\n ,邮箱:%s\n ,地址:%s\n , QQ:%s\n"%(i["姓名"],i["联系"],i["邮箱"],i["地址"],i["QQ"]))


def ademand():
    name4 = input("请输入您要查询的名字")
    for da in list:
        if da["姓名"] ==name4:
            print("%s\n,%s\n,%s\n,%s\n,%s\n"%(da["姓名"],da["联系"],da["邮箱"],da["地址"],da["QQ"]))
        else:
            print("系统里没有这个名字")

def exit():                
    print("退出系统")

    
    
str = "名片管理系统"
print(str.center(60,"*"))
list = []#建立一个空列表
while True:
    userinfo = {}#一个空字典
    choice = int(input("请输入您的选择：1.添加名片，2.删除名片，3.修改名片，4.查询名片，5.退出系统"))
    if choice == 1:#选择添加名片
        useradd()
    if choice == 2:#删除
        delete()
    if choice == 3:#修改
        amend()
    if choice == 4:#查询
        ademand()
    if choice == 5:#退出系统
        exit()
        break
