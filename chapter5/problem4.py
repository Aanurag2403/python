# create an empty dictionary allow 4 friends to enter their favorite language as value and use key as their name. Assume that names are unique?

d = {}

f1 = input("enter youur name: ")
f2 = input("enter you language: ")
d.update({f1: f2})

f3 = input("enter youur name: ")
f4 = input("enter you language: ")
d.update({f3: f4})

f5 = input("enter youur name: ")
f6 = input("enter you language: ")
d.update({f5: f6})

f7 = input("enter youur name: ")
f8 = input("enter you language: ")
d.update({f7: f8})


print(d)