#write a program to print
# *
# **
# ***

n = int(input("enter your no.:"))

for i in range(1,n+1):
    print("*" * (2*i-i),end="")
    print("")

print("\n")

#while loop

i = 1
while(i<n+1):
    print("*"*(2*i-1),end="")
    print("")
    i+=1
