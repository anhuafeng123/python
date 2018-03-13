list = ['anhuafeng','cuishu','admin','dengzilin','wanghailiang']
'''
if 'admin' in list:
    print("Hello admin, would you like to see a staus repoirt?")
else:
    print("Hello Eric, thank you for logging in again")
'''
del list[0:5:1]
print(list)
if list == [] :
    print("We need to find some users")





current_users = ['liuyanan','anyongli','zhuyucheng','lushunli','jinhonglei']
new_users = ['anhuafeng','jinhonglei','liuyanan','anpengfei','luping']
for i in new_users:
    if i.lower() == 'anhuafeng':
        print("已被使用，请输入别的用户名")
    elif i.lower() == 'jinhonglei':
        print("已被使用，请输入别的用户名")
    elif i.lower() == 'liuyanan':
        print("已被使用，请输入别的用户名")
    elif i.lower() == 'anpengfei':
        print("已被使用，请输入别的用户名")
    elif i.lower() == 'luping':
        print("已被使用，请输入别的用户名")
    else:
        print("用户名未被使用")



shuzi = [1,2,3,4,5,6,7,8,9]
print(shuzi)
for i in shuzi:
    if i == 1:
        print("1st\n")
    elif i == 2:
        print("2nd\n")
    elif i == 3:
        print("3rd\n")
    elif i == 4:
        print("4th\n")
    elif i == 5:
        print("5tn\n")
    elif i == 6:
        print("6th\n")
    elif i == 7:
        print("7th\n")
    elif i == 8:
        print("8th\n")
    else:
        print("9th\n")
