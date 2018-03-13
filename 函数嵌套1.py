def chenghe(a):
    if a > 1:
        sum = a*chenghe(a-1)
    else:
        sum =1
    
    return sum
d = chenghe(5)
print(d)
