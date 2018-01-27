#题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

n=input("please enter a number:")
l=len(n)
print('这是%d位数。'%l)
for i in range(l-1,-1,-1):
    print(n[i],end='')


