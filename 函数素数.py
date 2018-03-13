def sushu(a,b):
    list = []
    for i in range(a,b):
        if (i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0) or (i/2==1 or i/3==1 or i/5==1 or i/7==1):
            list.append(i)
    print(list)

def hansu(d,k):
    ll = []
    for q in range(d,k):
        for j in range(2,q):
            hh = True
            if q%j == 0:
                hh = False
                break
        else:
            print(q)
        ll.append(q)
        return 



sushu(2,101)
hansu(2,101)
