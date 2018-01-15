for i in range(1,10):#从1开始循环，循环九次
    count = 1#计数器从一开始
    while count <= i :#
        print("%d*%d=%d"%(count,i,count*i),end="\t")
        count+=1#循环一次加一
    print("")



