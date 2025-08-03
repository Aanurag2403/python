# write a program to find the given no. is prime or not


n=int(input("enter your no.: "))

#using for loop
for i in range(2,n):
    if(n%i) == 0:
       print("number is not prime")
       break 
else:
  print("it is a prime no.")


print("\n")

#using while loop
i = 2
while(i<n):
   if (n%i)==0:
     print("it is not a prime no.")
     break
   i+=1
else:
    print("it is a prime no.")
    
 
      

