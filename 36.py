#用辗转相除法求两个数的最大公约数

m=eval(input('Enter a number:'))
n=eval(input('Enter a number:'))

if n>m:
    m,n=n,m

while True:
    r = m % n
    m = n
    n = r
    if r==0:
        print('The greatest common divisor is %d.'%m)
        break