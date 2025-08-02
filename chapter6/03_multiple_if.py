a = int(input("enter your age: "))

if(a%2==0):  #if statement no1 #idependent
    print("age is even")
if(a>=18):   #if statement no2
    print("you are an adult")
elif(a<0):
    print("invalid input")
elif(a==0):
    print("invalid input")
else:
    print("you are minor")
