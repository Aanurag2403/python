# write a python function which converts inches to cms.

n = int(input("enter your value in inches: "))

def con(n):
    n = n*2.54
    return n
print(f"{n} in is ={con(n)}cm" )
