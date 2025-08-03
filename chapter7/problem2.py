#write a program to greet all the person names stored in a list 'l' and which starts with S.

l = ["Harry","Soham","Sachin","Rahul"]

# using for loop
for name in l:
    if(name.startswith("S")):
        print("Hello", name)

# using while loop
i = 0
while(i<len(l)):
    if(l[i].startswith("S")):
        print(f"{"hello"} {l[i]}")
    i +=1
