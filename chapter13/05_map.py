# map :it helps to run same functions for different values

l = [1,2,3,4,5]

square = lambda x: x*x

sqlist = map(square,l)
print(list(sqlist))


# Filter 
def Even(n):
    if(n%2==0):
        return True
    return False

onlyEven = filter(Even,l)
print(list(onlyEven))

# Reduce : it helps to run same functions for different values.

from functools import reduce
def sum(a,b):
    return a+b
print(reduce(sum, l))

mul = lambda a,b: a*b
print(reduce(mul, l))