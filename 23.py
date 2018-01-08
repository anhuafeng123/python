count = 1
a = 0
while count <= 9:
    row = 1
    while row <= count:
        a= count*row
        print(" %d * %d = %d "%(row, count ,a ),end="" )
        row+=1
    print("")
    count+=1
