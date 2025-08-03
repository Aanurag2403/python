# write a program to find sum of first n natural number

n = int(input("enter your number: "))

# using for loop
sum = 0
for i in range(1,n+1):
   sum = sum+i
print(sum)


#using while loop
i = 1
sum=0
while(i<=n):
   sum = sum+i
   i+=1
print(sum)
   


