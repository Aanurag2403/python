#write a program to print multiplication table of n using loop in reversed order

n = int(input("enter your no."))

for i in range(10,0,-1):
    print(f"{n} X {i} = {n*i}")

#using while loop

i=10
while(i>0):
    print(f"{n} X {i} ={n*i}")
    i-=1
