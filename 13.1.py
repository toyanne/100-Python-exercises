#题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
# 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。

def main():
    basis = int(input("Input the basis number:"))
    n = int(input("Input the longest length of number:"))
    b = basis
    sum = 0
    for i in range(0, n):
        if i == n - 1:
            print("%d" % (basis),end='')
        else:
            print("%d+" % (basis),end='')
        sum += basis
        basis = basis * 10 + b
    print('= %d' % (sum))

main()