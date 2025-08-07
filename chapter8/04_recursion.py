# one fnction callin itself is recursion

n = int(input("enter your no.: "))

def fact(n):
    if(n==1 or n==0):
        return 1
    return n * fact(n-1)

print("factorial of given no. is :",fact(n))