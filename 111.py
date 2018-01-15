for i in range(1,10):#从1开始循环，循环9次
    for d in range(1,i+1):#从1循环循环i+1
        print("%d*%d=%d"%(d,i,d*1),end="\t")
    print("")
