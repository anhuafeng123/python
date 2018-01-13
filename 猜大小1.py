import random
for i in range(1,11):
    n = random.randint(1,101)
    shuru = int(input("请输入您要猜的数字：1到101之内"))
    if shuru == n:
        print("恭喜你猜对了")
    elif shuru > n and shuru < 101:
        print("你猜大了！")
    elif shuru < n and shuru > 0:
        print("你猜小了！")
    else:
        print("系统出错！")
