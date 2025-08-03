# write a program to find the factorial of a given number 

n = int(input("enter your no:"))

#using for loop
fact=1
for i in range(1,n+1):
    fact = fact * i
    i+=1
print(fact)

#using while loop

fact=1
i=1
while(i<=n):
    fact = fact*i
    i+=1
print(fact)


