#题目：求一个3*3矩阵对角线元素之和
l=[]
for i in range(3):
    for j in range(3):
        l.append(int(input("Enter a number:")))
s=0
for i in range(0,9,2):
    s+=l[i]
print(s)

'''
123
456
789'''