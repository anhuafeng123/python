def qiu_sushu(x,y):
    for i in range(x,y):
        if (i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0) or (i/2==1 or i/3==1 or i/5==1 or i/7==1):
            print(i)
qiu_sushu(100,201)
