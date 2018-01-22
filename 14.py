#题目：一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.找出1000以内的所有完数。


def perfectNumber(n):
    total=0
    for i in range(1,n):
        if n%i==0:
            total+=i
    if n==total:
        return True
    else:
        return False

for i in range(1,1001):
    if perfectNumber(i):
        print(i)
