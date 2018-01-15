def g_sum(a,b,c,*args,**kwargs):
    suma =0
    m =0
    g = 0
    for i in args:
        m+=i
    for k,v in kwargs.items():
        g+=v
    suma=a+b+c+m+g
        
    return suma
k =g_sum(1,2,3,4,5,6,7,8,10,age=2,age1=155,age2=200)
print(k)
