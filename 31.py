#求解二元一次方程

print('二元一次方程：a1*x+b1*y=c1 a2*x+b2*y=c2')

a1=eval(input('Enter a1:'))
b1=eval(input('Enter b1:'))
c1=eval(input('Enter c1:'))

a2=eval(input('Enter a2:'))
b2=eval(input('Enter b2:'))
c2=eval(input('Enter c2:'))

#等式1*b2-等式2*b1,可推出x
#等式2*a1-等式1*a2,可推出y
if a1*b2-a2*b1!=0:
    x=(b2*c1-b1*c2)/(a1*b2-a2*b1)
    y=(a1*c2-a2*c1)/(a1*b2-a2*b1)

    print('x=',x)
    print('y=',y)

else:
    print('Invalid input.')