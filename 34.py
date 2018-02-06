#用二分法求x^2-2=0(x>0)的近似解。 测试用例：1，2，0.005，   1.41796875

def f(x):
    if x>0:
        return x**2-2

def fm(a,b) :
    return (a + b) / 2

def is_m(a , b , d ,m):
    return (abs((a-b)) < d ) or f(m) == 0

a=eval(input('输入初始值a:'))
b=eval(input('输入初始值b:'))
d=eval(input('输入精确度d:'))


while True:
    m = fm(a,b)
    if f(a) * f(m) < 0 :
        b = m
    else:
        a = m

    if is_m(a,b,d,m) :
        print("m is %f\n" % m)
        break



