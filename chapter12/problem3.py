# write a list comprehension to print a list which contains the multiplication table of a user entered number.


n = int(input("enter a number to find table: "))

table = [n*i for i in range (11)]
print(table)