list = ['香蕉','苹果','梨','橘子','石榴','香瓜','西瓜','樱桃','芒果']
print(list)
print('前三种水果:\n')
print(list[0:3])
print('中间三种水果:\n')
print(list[3:6])
print('末尾三种水果:\n')
print(list[-3:])


    

list = ["培根披萨","奥尔良烤鸡披萨","金枪鱼披萨","火腿披萨","大虾披萨","菠萝虾仁披萨"]
pisa = list[:]
print(list)
print(pisa)
list.append('火辣披萨')
pisa.append('香蕉披萨')
print('My favorite pizzas are:')
for i in list:
    print(i)
print('My friend’s favorite pizzas are:')
for a in pisa:
    print(a)
