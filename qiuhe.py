def print_qiuhe():
    sum = 0
    jishu = 0
    oshu = 0
    for i in range(1,101):
        if i%2 == 0:
            oshu += i
        if i%2 != 0:
            jishu += i
        sum = oshu + jishu
    print("总和:%d 奇数:%d 偶数:%d"%(sum,jishu,oshu))

print_qiuhe()
