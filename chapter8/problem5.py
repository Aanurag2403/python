# write a python function to print n lines of the following pattern:

# ***
# **
# *


n = int(input("enter your  no. of lines want to print: "))

def pat(n):
    for i in range(n,0,-1):
        print("*" * i,end="")
        print("")
    return 1

pat(n)


print("")


# using racursion

def pat2(n):
    if(n==0):
        return 
    print("*"*n)
    pat2(n-1)
pat2(n)



    