# write a program to print multiplication table of given no.:

n = int(input("enter a number to find table: "))

def tab(n):
    for i in range(1,11):
       print(n*i)
    
tab(n)
    