
list = ["朱宇程","路顺利","金红蕾","邓子林","刘亚楠",'宰俊培','宰俊仙','宰相的宰']

for i in list:

    print("我将邀请%s和我共进晚餐\n"%i)
sd = len(list)
print("总共邀请了%s位与我共进晚餐"%sd)

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
print("由于餐桌无法按时到达，现只能邀请两位客人")
ha = 11
while ha > 2:

    ao = list.pop(0)
    print("你好，%s，由于突发事情，无法邀请您赴约，请见谅！"%ao)
    ha-=1
for a in list:
    print("请您准时到达%s\n"%a)

del list[0:2:1]

print(list)
sd = len(list)
print("总共邀请了%s位与我共进晚餐"%sd)
