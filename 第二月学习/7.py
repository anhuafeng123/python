class Dongwu(object):
    def __init__(self):
        self.__name = "打打"
    def cry(self):
        print("啊啊啊啊啊啊")

    def eat(self):
        print("吃")
class Dog(object):
    def __init__(self):
        self.name = 'aa'
    def cry1(self):
        print("ddddd")
    def eat1(self):
        print("和")
class Nnji(Dongwu,Dog):
    def __init__(self):
        self.name = 'kk'
    def cry2(self):
        print('eee')
    def eat2(self):
        print('dddddddd')
mmm = Nnji()
mmm.cry2()
mmm.eat2()
mmm.cry1()
mmm.eat1()
mmm.cry()
mmm.eat()
