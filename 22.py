#题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

s = input('Input a string:')
l = len(s)
def output(s,l):
    if l==0:
        return
    print(s[l-1],end='')
    output(s,l-1)


output(s,l)
