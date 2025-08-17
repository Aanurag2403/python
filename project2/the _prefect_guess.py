# we are going to write a program that generates a random number and asks the users to guess it.

import random
n = random.randint(1,100)
a = -1
gueses = 1
while(a!=n):
    a = int(input("enter your number: "))
    if(a > n):
        print("lower no. please!!")
    elif(a<n):
        print("higher numbeer please!!")
    gueses += 1

print(f"You have gussed the correct no. {n} in {gueses} attempt")