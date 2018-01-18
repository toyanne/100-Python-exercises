#题目：输出9*9口诀。

for i in range(1,10):
    for j in range(1,i+1):
        #print(j,'*',i,'=',i*j)
        print("%d*%d=%2d" % (i, j, i * j), end=" ") #2d实现两位数位置
    print('')

