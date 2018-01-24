#题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

def f(n):
    if n<=2:
        return 1
    elif n>2:
        return f(n-1)+f(n-2)

s=0
for n in range(2,22):
    s+=f(n+1)/f(n)
print(s)