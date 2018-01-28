#题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
#palindromic number

n=input("Enter a 5-digit number:")
def isPalindromic(n):
    if n[0]==n[4] and n[1]==n[3]:
        return True
    else:
        return False

if isPalindromic(n):
    print('This is a palindromic number.')
else:
    print('This is not a palindromic number.')