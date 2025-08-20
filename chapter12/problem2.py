# write a program to print third,fifth and seventh element from a list using enumerate function.

list = [12,34,56,78,90,32,11,45,67,87]

for i,item in enumerate(list):
    if i == 2 or i == 4 or i == 6:
        print(item)
