#求f(x)=x^5+x^4+x^3+x^2+x+1

x=eval(input('Enter the value of x:'))
s=0
for i in range(0,6):
   s+=x**i
print('f(x)=',s)