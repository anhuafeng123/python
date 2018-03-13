'''
g = list(range(1,1000001))
print(g)
'''
for i in range(1,21):
    print(i)
s = list(range(1,1000001))
print(min(s))
print(max(s))
print(sum(s))
d = list(range(1,21,2))
print(d)
f = list(range(3,31,3))
for i in f:
    print(i)
g = []
for a in range(1,11):
    h = a**3
    g.append(h)
print(g)
k = [j**3 for j in range(1,11)]
print(k)
