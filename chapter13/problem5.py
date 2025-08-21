# write a program to find the maximum of the numbers in the list using the reduce function.

from functools import reduce
l = [1,2,32,45,332,45334,5224,45645,66435,15567,238,250]

def greater(a,b):
    if (a>b):
        return a
    return b

print(reduce(greater,l))