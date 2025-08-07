# write a code usong function to find greatest of three numbers.

n1 = int(input("enter your first no.: "))
n2 = int(input("enter your second no.: "))
n3 = int(input("enter your third no.: "))
def greatest(n1,n2,n3):
    if(n1>n2 and n1>n3):
        return n1
    elif(n2>n1 and n2>n3):
        return n2
    elif(n3>n1 and n3>n2):
        return n3

print(greatest(n1,n2,n3))