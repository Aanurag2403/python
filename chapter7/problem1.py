# write a progeam to print multiplication table of the given number using loop.

n = int(input("enter your no.: "))

#using while loop
i = 1
while(i<=10):
    print(f"{n} X {i} = {i*n}")
    i+=1

# using for loop
for i in range(1,11):
    print(f"{n} X {i} = {i*n}")