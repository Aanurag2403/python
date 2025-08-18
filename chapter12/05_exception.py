# handling exception

try: 
    a = int(input("ente a number: "))
    print(a)

except Exception as e:
    print(e)



# using try statement will help you not to crash you program and will help remaining to deploy
print("thankyou")



# handling specifc exception
try:
    a = int(input("enter your no."))
    print(a)
except ValueError as v:
    print(v)
except Exception as e:
    print(e)
