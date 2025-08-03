#break statement
#it will exit the loop

for i in range(100):
    if(i==34):
       break
    print(i)

print("\n")

#continue
#it will skip the iteration

for i in range(100):
    if(i==34):
        continue
    print(i)

#pass
#this statement passes the crrent work and allow to move for another one.

for i in range(24):
    pass


i=0
while(i<10):
    print(i)
    i +=1