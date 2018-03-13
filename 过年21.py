#
def make_shirt(size,words):
    print('你选择的是一件%s号的T恤，T恤印有%s的字样.'%(size,words))
make_shirt('大','I love python')
make_shirt('中','I love python')
make_shirt('小','I love python3')



def describe_city(chengshi,guojia):
    print('%s属于%s'%(chengshi,guojia))
describe_city('北京','中国')
describe_city('首尔','韩国')
describe_city('东京','日本')

print("#")

def city_country(chengshis,guojias):
    dd_a = chengshis +','+ guojias
    return dd_a
mi = city_country('北京','中国')
print(mi)


print("#")
def make_album(name,names,named=''):
    a = {'歌手':name,'歌名':names,'歌曲数':named}
    return a
d = make_album('安华锋','我们都一样',0)
print(d)




while True:
    f = int(input('1:添加   2:退出'))
    if f == 1:
        n = input('请输入歌手的名字:')
        s= input('请输入专辑名:')
        print(make_album(n,s))
    else:
        break

