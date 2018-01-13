def nian_qw(year):
    if year%400 == 0 or (year%4 == 0 and year%100 != 0):
        print("闰年")
    else:
        print("平年")
year = int(input("请输入你要查看的年份："))
nian_qw(year)
