count = 1#计数器
a = 0#乘和
while count <= 9:#总共循环九次
    row = 1#也是计数器，但这个是为了让他从一开始
    while row <= count:
        a= count*row#a等于row乘count
        print(" %d * %d = %d "%(row, count ,a ),end="" )#这里的end=""是不换行的意思
        row+=1#每循环一次加1
    print("")#另起一行的意思
    count+=1#每循环一次加1
