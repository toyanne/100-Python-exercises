#用更相减损术法求两个数的最大公约数."可半者半之，不可半者，副置分母、子之数，以少减多，更相减损，求其等也。以等数约之。"

m=eval(input('Enter a number:'))
n=eval(input('Enter a number:'))

if n>m:
    m,n=n,m

def evenNum(x):
    if x%2==0:
        return True
t=1
if evenNum(m) and evenNum(n):
    m=m//2 #如果用/得出的结果带小数点
    n=n//2
    t*=2

while True:
    r=abs(m-n)
    if n == r:
        print('The greatest common divisor is %d.'%n*t)
        break
    else:
        m=n
        n=r

