zidian = {'尼罗河':'非洲','长江':'中国','亚马孙河':'巴西'}
for k,v in zidian.items():
    print("%s流经%s"%(k,zidian[k]))
k = {'姓名':'安华锋','性别':'男'}
s = {'姓名':'宰俊仙','性别':'女'}
j = {'姓名':'路顺利','性别':'男'}
people = []
people.append(k)
people.append(s)
people.append(j)
print(people)
for i in people:
    for k,v in i.items():
        print(k,v)
