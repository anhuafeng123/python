def a_sum(b=100,d=0):
    sum = 0
    if not d:
        for i in range(1,b+1):
            sum+=i
    else:
         count = 1
         while count <= b:
            sum+=count
            count+=1
    return sum


qiuhe = a_sum(10,1)
print(qiuhe)
