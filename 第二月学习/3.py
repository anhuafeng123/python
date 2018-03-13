class Kaodigua():
    def __init__(self):
        self.sheng = 0
        self.digua = '生的'
        self.list = []
    def cook(self,timp):
        self.sheng += timp
        if self.sheng > 8:
            self.digua = '糊了'
        elif self.sheng > 5:
            self.digua ='考好了'
        elif self.sheng > 3:
            self.digua = '半生不熟的'
        else:
            self.digua = '生的'
    def __str__(self):
        s = self.digua + '地瓜'
        if len(self.list) > 0:
            s = s+'('
            for i in self.list:
                s=s+i+')'
        return s
    def aajjgg(self,list):
        self.list.append(list)
        
kkddgg = Kaodigua()
print('-------烤地瓜-------')
print(kkddgg.sheng)
print(kkddgg.digua)
print('-------开始烤地瓜-------')
print('-------烤了4分钟--------')
kkddgg.cook(4)
print(kkddgg.digua)
print('-------又烤了3分钟-------')
kkddgg.cook(3)
print(kkddgg.digua)
print('-------接下来添加佐料-------')
kkddgg.aajjgg('辣椒')
print(kkddgg)

