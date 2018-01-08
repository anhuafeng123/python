import random
#石头剪刀布
nom = 0
while nom<3:
    me = int(input("请输入：1:石头，2:剪刀，3:布"))
    computer = random.randint(1,3)
    if me<=3 and me>0:
        if me == 1 and computer == 2:
            print("你赢\n电脑显示：%d\n"%(computer))
        elif me == 2 and computer == 3:
            print("你赢\n电脑显示：%d\n"(computer))
        elif me == 3 and computer == 1:
            print("你赢\n电脑显示：%d\n"(computer))
        elif me == computer:
            print("平局\n电脑显示：%d\n"%(computer))
        else:
            print("你输了\n电脑显示：%d\n"%(computer))
    else:
        print("会看题目吗?瞎他妈输")
    nom+=1
    

