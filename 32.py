#求解一元二次方程。
import math
print('一元二次方程：a*x^2+b*x+c=0')
a=eval(input('Enter a:'))
b=eval(input('Enter b:'))
c=eval(input('Enter c:'))

d=b*b-4*a*c
p=-b/(2*a)
q=math.sqrt(d)/(2*a)
if d>0:
    x1=p+q
    x2=p-q
    print('x1=',x1,'x2=',x2)
elif d==0:
    x=p
    print('x1=x2=',x)
elif d<0:
    print('There is no real root.')
