a = int(input("请输入一个数字"))
sume1 = 0
count = 0
suma = 0
while count<a:
    count+=1
    if count%2==0:
        suma = count+suma
    elif count%2!=0:
        sume1+=count
print("偶数总和%d\n 奇数总和%d\n"%(suma,sume1))
print("奇数和偶数总和：%d"%(suma+sume1))

