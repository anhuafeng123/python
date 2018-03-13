print("*"*30)
#使用变量
msg = "欢迎来到召唤师峡谷"
print(msg)
print("*"*30)
#字符串的大小写转换
name = "wangzherongyao"
print(name.title())#首字母大写
print(name.upper())#全部字母大写
print(name.lower())#全部字母小写
print("*"*30)
#合并字符串
first_name = "郑"
last_name = "开州"
full_name = first_name+""+last_name
print(full_name)
print("尊敬的召唤师:"+full_name+",欢迎来到召唤师峡谷！")
print("*"*30)
#制表符和换行符
print("欢迎来到召唤师峡谷！")
print("\t欢迎来到召唤师峡谷！")#文本向后缩进一个单位
print("\n欢迎来到召唤师峡谷！")#文本换行
print("*"*30)
#删除字符串两端空格
msga = "努力有用的话还要天才干甚？"#文本前后有空格
print(msga)
msga = msga.strip()#移除变量msga两端的空格
print(msga)
print("*"*30)
#数字变量
num = 2
msgs = ("尊敬的召唤师,您在这局对战中的综合评分位于第"+str(num)+"位!")
print(msgs)
print("*"*30)
#查看
heroes = ["安其拉","李白","杨戬","貂蝉","孙悟空"]
print(heroes)
print(heroes[0])
print(heroes[1])
print(heroes[::1])
#更改指定英雄
print("*"*30)
heroes[0]="孙尚香"
print(heroes)
print("*"*30)
#添加英雄
heroes.append("兰陵王")
print(heroes)
print("*"*30)
#添加到指定位置
print(heroes)
print("*"*30)
#列表删除
del heroes[0]
print(heroes)
print("*"*30)
tail = heroes.pop()
print(heroes)
print(tail)
print("*"*30)
heroes.remove("李白")
print(heroes)
print("*"*30)
#列表排序
#按笔画排序
heroes.sort()
print(heroes)
print("*"*30)
#反方向排序
heroes.sort(reverse = True)
print(heroes)
print("*"*30)
#临时排序
print(sorted(heroes))
print(heroes)
print("*"*30)
#反方向排序
heroes.reverse()
print(heroes)
print("*"*30)
#元素计数
print(len(heroes))
print("*"*30)
#遍历真个列表
for i in heroes:
    print("%s是一个很牛的英雄\n"%i)
#数字列表
for i in range(1,5):
    print(i)
print("*"*30)
num = list(range(1,6))
print(num)
print("*"*30)
pfj = []
for i in range(1,21):
    pf = i**2
    pfj.append(pf)
print(pfj)
print("*"*30)
#if
for g in heroes:
    if g == "狄仁杰":
        print("您选择的英雄超级厉害的！")
    else:
        print("你选择的英雄只能说一般般")
print("*"*30)
name = "dengziling"
if name == "dengziling":
    print("对")
if name == "DENGZILING":
    print("错")
print("*"*30)
#字典
zi = {"姓名":"张廷强","性别":"男","电话":"12","地址":"家","邮箱":"1234"}
print(zi)
zi["爱好"]="美女"#增加
print(zi)
zi["姓名"]="白羊"#更改
print(zi)
del zi["性别"]#删除
print(zi)
for k,v in zi.items():
    print(k,v)
list = [zi]
print(list)
