# write a rpogram to convert fahrenheit to celsius using function


def conv(f):
    c = ((f-32)/9) * 5
    return c
f = int(input("enter temp in fahrenheit: "))
print("temperature in celsius is: ",conv(f))