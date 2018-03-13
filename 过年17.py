#租聘汽车
car = input("请输入您要租聘的汽车品牌:")
print("让我看看能不能找到您要租聘的%s"%car)
yongcan = int(input("请问有多少人用餐:"))
if yongcan >= 8:
    print("对不起，没有空的餐桌了")
else:
    print("有空的餐桌！祝您用餐愉快!")
ss = int(input("请输入您要输入的数字:"))
if ss % 10 == 0:
    print("您输入的%s是10的倍数"%ss)
else:
    print("您输入的%s不是10的倍数"%ss)

