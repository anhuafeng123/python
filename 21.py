a = 0
b = 0
while a < 100:
    if a%2 == 0:
        b=b-a
    else:
        b=b+a
    a+=1
print("和%d"%b)
