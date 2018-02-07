#任意输入3个数，从大到小输出

a=eval(input('a:'))
b=eval(input('b:'))
c=eval(input('c:'))

if b>a:
    t=a
    a=b
    b=t

if c>a:
    t=a
    a=c
    c=t

if c>b:
    t=b
    b=c
    c=t

print(a,b,c)