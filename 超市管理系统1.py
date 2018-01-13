name1 = '香蕉'
money1 = 3
name2 = '苹果'
money2 = 2.5
name3 = '梨'
money3 = 1.5
name4 = '方便面'
money4 = 2
name5 = '张燕娜'
money5 = 100
name6 = '崔树'
money6 = 0.25
name7 = '芒果'
money7 = 2.2
name8 = '葡萄'
money8 = 4
name9 = '西瓜'
money9 = 5
print("*"*80)
print("好牛逼超市")
name = input("请输入商品名称")
if name==name1:
    weight1 = input("多少")
    total1 =float(weight1)*money1
    print("商品名称:%s\n 商品重量:%s\n 单价:%d\n 总价:%d\n"%(name1,weight1,money1,total1))
elif name==name2:
    weight2 = input("多少")
    total2 = float(weight2)*money2
    print("商品名称%s\n 商品重量%s\n 单价：%d\n 总价：%.2f"%(name2,weight2,money2,total2))
elif name==name3:
    weight3 = input("多少")
    total3 =float(weight3)*money3
    print("商品名称%s\n 商品重量%s\n 单价：%d\n 总价：%.2f"%(name3,weight3,money3,total3))
elif name==name4:
    weight4 = input("多少")
    total4 =float(weight4)*money4
    print("商品名称%s\n 商品重量%s\n 单价：%d\n 总价：%.2f"%(name4,weight4,money4,total4))
elif name==name5:
    weight5 = input("多少")
    total5 =float(weight5)*money5
    print("商品名称%s\n 商品重量%s\n 单价：%d\n 总价：%.2f"%(name5,weight5,money5,total5))
elif name==name6:
    weight6 = input("多少")
    total6 =float(weight6)*money6
    print("商品名称%s\n 商品重量%s\n 单价：%.2f\n 总价：%.2f"%(name6,weight6,money6,total6))
elif name==name7:
    weight7 = input("多少")
    total7 =float(weight7)*money7
    print("商品名称%s\n 商品重量%s\n 单价：%d\n 总价：%.2f"%(name7,weight7,money7,total7))
elif name==name8:
    weight8 = input("多少")
    total8 =float(weight8)*money8
    print("商品名称%s\n 商品重量%s\n 单价：%d\n 总价：%.2f"%(name8,weight8,money8,total8))
elif name==name9:
    weight9 = input("多少")
    total9 =float(weight9)*money9
    print("商品名称%s\n 商品重量%s\n 单价：%d\n 总价：%.2f"%(name9,weight9,money9,total9))
else :
    print("没有，爱买不买！")


