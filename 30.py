#给出三角形的三条边长，求三角形的面积。
import math

a=eval(input("Enter the length of edge a:"))
b=eval(input("Enter the length of edge b:"))
c=eval(input("Enter the length of edge c:"))

if a+b>c and b+c>a and c+a>b:
    p=(a+b+c)/2

    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
#海伦-秦九昭公式

    print('The area of the triangle is:',s)
else:
    print('Invalid input.')

