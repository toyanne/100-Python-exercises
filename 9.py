#题目：打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。


def narcissisticNumber(n):
    a=n%10
    b=n//100
    c=(int(n%100))//10
    if n==pow(a,3)+pow(b,3)+pow(c,3):
        return True
    else:
        return False

for n in range(100,1000):
    if narcissisticNumber(n):
        print(n)




