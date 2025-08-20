# write a program to dispaly a/b where a and b are integer. if b =0 display infinte by handling the 'ZeroDivisionError'.


try:
    a = int(input("enter first no.: "))
    b = int(input("enter second no.: "))
    print(a/b)
except ZeroDivisionError as z:
    print("Infinite")

