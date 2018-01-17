
n=int(input("Enter a number:"))
def primeNumber(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True


if primeNumber(n) :
    print("This is a prime number.")
else :
    print("This isn't a prime number.")

