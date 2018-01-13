def print_xinxi():
    list = []
    while True:
        userinfo = {}
        name = input("请输入用户姓名：")
        age = int(input("请输入年龄："))
        sex = input("请输入你的性别：")
        if not list:
            userinfo["name"]=name
            userinfo["age"]=age
            userinfo["sex"]=sex
            list.append(userinfo)
        else:
            ha = False
            for i in list:
                for k,v in i.items():
                    if v == name:
                        print("重复")
                        ha = True
                        break
            if not ha:
                userinfo["name"]=name
                userinfo["age"]=age
                userinfo["sex"]=sex
                list.append(userinfo)
        for i in list:
            print(i)
print_xinxi()
