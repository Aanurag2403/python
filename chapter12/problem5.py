# store the multiplication tables generated in problem3 in a file named Tables.txt.

n = int(input("enter a no.: "))

table = [ n*i for i in range(11)]

with open("tables.txt","a") as f:
    f.write(f"table of {n} is : {str(table)} \n")

