#题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

l=[0,10,20,30,40,50]
print('The sorted list is:',l)
#c=len(l)
n=int(input('Enter a new number:'))
l.append(n)
l.sort()
'''
for i in range(0,c):
    if n<l[i]:
        for j in range(c,i,-1):
            l[j]=l[j-1]
        l[i] = n
        break'''

print(l)
