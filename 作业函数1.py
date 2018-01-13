def chengfabiao(a,b):
    for i in range(a,b):
        for j in range(1,i+1):
            print("%d*%d=%d"%(j,i,j*i),end="\t")
        print("")

chengfabiao(1,10)
