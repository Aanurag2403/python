a = int(input("enter you no.: "))
b = int(input("enter your no. :"))

if (b == 0):
    raise ZeroDivisionError("hey please provide divisor not equals to '0'")
else:
    print("your division is", a/b)