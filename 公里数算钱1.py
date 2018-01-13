a = float(input("请输入你的公里数"))
sum = 0
for i in range(1,61):
    if a <= 6:
        money = 3
    elif a > 6 and a <= 12:
        money = 4
    elif a > 12 and a <= 22:
        money = 5
    elif a > 22 and a <= 32:
        money = 6
    elif a > 32 :
        if (a - 32)% 20 == 0:
            money = 6 + (a - 32)/20
        else:
            money = 6 + int((a - 32)/20)+1
    if sum >= 100 and sum < 150:
        money = money * 0.8
    elif sum >= 150 and sum <= 400:
        money = money * 0.5
    sum += money
print("您一个月消费：%.2f"%sum)

            

