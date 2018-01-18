#题目：输入三个整数x,y,z，请把这三个数由小到大输出。

n=input()
l=list(n)
#m=l.remove(',')
l.sort()
for i in range(2,5):
    print(l[i],' ',sep='',end='')


