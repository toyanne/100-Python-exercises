#2005年生产总值为200万元，年增长率5%，求生产总值超过300万的最早年份。

n=2005
a=200

for i in range(100):
    if a<300:
        a = a * (1 + 0.05)
        n=n+1
    else:
        print(n)
        print('%.2f'%a)
        break
