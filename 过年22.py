
name = ['土包子','水包子','火爆子','蛋蛋']
def show_magicians(hh):
    for i in hh:
        print(i)
def make_great(ll):
    for i in range(0,len(ll)):
        ll[i]=ll[i]+'The Great'
    print(ll)
show_magicians(name)
make_great(name)
