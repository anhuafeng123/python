def tt_tt():
    str = input("请输入你的日期：")
    qo = int(str[0:4:1])
    to = int(str[4:6:1])
    bo = int(str[6:8:1])
    ww_ww(qo,to,bo)
def ww_ww(qo,to,bo):
    lo = 0
    gun=[1,3,5,7,8,10,12]
    dan=[4,6,9,11]
    for i in range (1,to):
        if i in gun:
            lo+=31
        elif i in dan:
            lo+=30
        else:
            if to == 2 and rr_rr(qo):
                lo+=29
            else:
                lo+=28
    bo+=lo
    print("%d天"%bo)
def rr_rr(qo):
    if qo%400==0 and (qo%4==0 or qo%100!=0):
        kk = 1
    else:
        kk = 0

tt_tt()
