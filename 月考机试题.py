def haha(list):
    for i in list:
        a = i["距离"]
        b = i["月份"]
        c = i["次数"]
        sum = 0
        for j in range(0,30*c):
            if a <= 6:
               s=3
            elif a > 6 and a <= 12:
                s=4
            elif a > 12 and a <= 22:
                s=5
            elif a > 22 and a <= 32:
                s=6
            elif a > 32:
                if (a - 32)%20 == 0:
                    s = (6 + (a - 32)/20)
                else:
                    s = (6 + int((a - 32)/20)+1)
            if sum >= 100 and sum < 150:
                    s = s * 0.8
            elif sum >= 150 and sum <= 400:
                    s = s * 0.5
            sum+=s
        print("%d月花了%.2f元"%(b,sum))
        global kej,kea
        kej+=sum
        kea+=c
        print("总共花了%.2f元，总共%d次"%(kej,kea))
def chengzuo(list):
    r = {}
    j = float(input("请输入距离:"))
    y = int(input("请输入月份:"))
    t = int(input("请输入每天的次数"))
    r["距离"]=j
    r["月份"]=y
    r["次数"]=t

    if y < 0 or y > 12 or t < 0:
        print("输入的不和规定")
    else:
        list.append(r)
        
        return list
kej = 0
kea = 0
list = []
while True:
    caidan = int(input("菜单: 1.乘坐 2.计算 3.退出"))
    if caidan == 1:
        gg=chengzuo(list)
    if caidan == 2:
        haha(gg)
    elif caidan == 3:
        break
