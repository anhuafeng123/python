information = ("欢迎进入个人信息管理系统")
print(information.center(60,"*"))
list=[]
while True:
    gongneng=int(input("请选择功能：1.新增 2.查询 3.修改 4.删除"))
    if gongneng == 1:
        name = input("请输入名字:")
        sge = int(input("请输入年龄:"))
        sex = input("请输入性别:")
        work = input("请输入工作:")
        list.insert(0,name)
        list.insert(1,sge)
        list.insert(2,sex)
        list.insert(3,work)
        print(list)
    elif gongneng == 2:
        suo = int(input("请输入索引："))
        print(list[suo])
    elif gongneng == 3:
        aname = input("请输入要修改的人名：")
        aaname =  input("请输入新的名字")
        list[0]= aaname
        print(list)
    elif gongneng == 4:
        ddname = input("请输入你要删除的人名:")
        list.remove[ddname]
        pring(list)
        break
