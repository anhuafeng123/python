y = int(input("请输入年份"))
if y%4==0 and not(y%100==0) or y%400==0:
    print("这是闰年")
else :
    print("这不是闰年")
