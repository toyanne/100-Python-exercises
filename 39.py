#用秦九昭算法求n次多项式f(x)=an*x^n+an-1*x^n-1......+a1*x+a0
#测试用例：f(x)=4*x^5+2*x^4+3.5*x^3-2.6x^2+1.7*x-0.8   f(x)=14130.2

n=eval(input('n='))
a=eval(input('an='))
x=eval(input('x='))
v=a
i=n-1
while i>=0:
    a=eval(input('ai='))
    v=v*x+a
    i=i-1
print('f(x)=',v)


