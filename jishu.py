def hehe(a,d):
    n = 0
    g = 0
    for i in range(a,d):
        if i%2 == 0:
            n+=i
        if i%2 != 0:
            g+=i
    sum=n+g
    print("奇数:%d,偶数:%d,和:%d"%(g,n,sum))
hehe(1,101)
