list = ["朱宇程","路顺利","金红蕾","邓子林","刘亚楠",'宰俊培','宰俊仙','宰相的宰']

for i in list:

    print("我将邀请%s和我共进晚餐\n"%i)

ad = list[2]
print("%s无法参加参加晚餐"%ad)
list[2]=input("请输入重新要邀请的人:")
for i in list:
    print("我将邀请%s和我共进晚餐\n"%i)
print("当前有一个大的餐桌，还有三个空位")
name1 = input("您要邀请的第一位是:")
name2 = input("您要邀请的第二位是:")
name3 = input("您要邀请的第三位是:")
list.append(name1)
list.insert(0,name2)
list.insert(4,name3)
for i in list:
    print("我将邀请%s和我共进晚餐\n"%i)
