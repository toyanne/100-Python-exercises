#题目：对10个数进行排序
print('Enter 10 numbers')
l=[]
for i in range(0,10):
    l.append(int(input('Enter 10 numbers:')))
#l.sort()
for i in range(0,9):
    for j in range(i+1,10):
        if l[i]>l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp

print(l)