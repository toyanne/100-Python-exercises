#题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，70-89分之间的用B表示，60-69分之间的用C表示，60分以下的用C表示。

n=eval(input("Enter a score:"))
if n>=90:
    print("A")
elif n >= 70 and n <= 89:
    print("B")
elif n >= 60 and n <= 69:
    print("C")
else:
    print("D")

