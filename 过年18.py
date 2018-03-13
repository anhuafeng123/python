#披萨
'''
while True:
    aa = input("请输入要添加的披萨配料:")
    if aa == 'quit':
        print("我们会在比萨中添加%s"%aa)
        break
    else:

        print("我们会在比萨中添加%s"%aa)
'''
#电影票
w = 3
while w > 0:
    age = int(input("请输入年龄:"))
    if age < 3:
        print("免费")
    elif age < 12:
        print("10美元")
    else:
        print("15美元")
    w-=1

