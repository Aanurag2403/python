# write a code to find the greatest no. from the four input no.s?

a = int(input("enter a no."))
b = int(input("enter a no."))
c = int(input("enter a no."))
d = int(input("enter a no."))

if(a>b and b>c and c>d):
    print(a,"is greatest no.")
elif(b>a and b>c and b>d):
    print(b,"is greatest no.")
elif(c>a and c>b and c>d):
    print(c,"is greatest no.")
else:
    print(d,"is the greatest no.")