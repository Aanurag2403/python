try:
    a = int(input("enter your no."))
    print(a)

except Exception as e:
    print(e)

# our code will run uder else statement when try will work sucessfully.
else:
    print("I'm iside else")
