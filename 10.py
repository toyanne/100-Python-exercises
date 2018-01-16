#题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。


n=num=int(input('Enter a number:'))
list=[]
for j in range(int(num/2)+1):
    for i in range(2,n):
        t=n%i
        if t==0:
            list.append(i)
            n=n//i
            break
if len(list)==0:
    print("There is no prime factor.")

else:
    list.append(n)
    list.sort()
    print('%d=%d'%(num,list[0]),end='')
    for i in range(1,len(list)):
        print('*%d'%list[i],end='')




