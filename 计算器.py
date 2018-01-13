jia = '+'
jian = '-'
cheng = '*'
chu = '/'
mi = '**'
x = float(input("请x里输入"))
y = float(input("请y里输入"))
qing = input("请输入 + - × / **")
if qing == jia:
    jieguo = x+y
    print("当前公式%.2f+%.2f=%.2f"%(x,y,x+y))
elif qing == jian:
    jieguo1 = x-y
    print("当前公式%.2f-%.2f=%.2"%(x,y,x-y))
elif qing == cheng:
    jieguo2 = x*y
    print("当前公式%.2f*%.2f=%.2"%(x,y,x*y))
elif qing == chu:
    jieguo3 = x/y
    print("当前公式%.2f/%.2f=%.2"%(x,y,x/y))
elif qing == mi:
    jieguo4 = x**y
    print("当前公式%.2f**%.2f=%.2"%(x,y,x**y))
    
