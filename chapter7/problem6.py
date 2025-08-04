# write a rpogram to print the following star pattern
#     *
#    ***
#   *****

n = int(input("enter your no.:"))


# for loop
for i in range(1,n+1):
    print(" " * (n-i),end="")
    print("*" * (2*i-1),end="")
    print("")

print("\n")
          
# while loop
i = 1
while(i<n+1):
    print(" " * (n-i),end="")
    print("*" * (2*i-1),end="")
    print("")
    i+=1