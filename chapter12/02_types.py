from typing import List,Union,Tuple

#list of integers:
numbers: List[int] = [1,22,3,4,55]

# Tuple of string and an integer
person: Tuple[str,int] =("Alice",30)

#dictionary with string  keys and integer values
scores: dict[str, int] ={"Alice":90 , "bob": 85}

# union type for variables that can hold multiple types
identifier: Union[int,str] = "ID123"
identifier =12345 # also valid


#types
n : int = 5

name :str ="hari"

def sum(a:int, b: int) ->int:
    return a+b

print(sum(1,2))
