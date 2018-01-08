hight = float(input("请输入你的身高"))
shenjia = float(input("请输入你的身价"))
yanzhi = float(input("请输入您的颜值分"))
if hight > 180 and shenjia > 1000000000 and yanzhi > 90:
    print("宇宙超级无敌高富帅，小可爱！")
elif hight < 180 and hight >170 and shenjia < 10000000 and shenjia >1000000 and yanzhi < 90 and yanzhi > 70:
    print("市级版高富帅。")
elif hight < 170 and hight >160 and shenjia < 1000000 and shenjia > 100000 and yanzhi < 70 and yanzhi > 60:
    print("县城版高富帅")
elif hight < 160 and hifht > 150 and shenjia < 100000 and shenjia >100 and yanzhi < 60 and yanzhi >10:
    print("小屌丝一枚")
else:
    print("你是个大屌丝")
