name = "anurag"
#      [012345]  positive indexing
#     -[654321]  negative indexing
#string is immutable

#slicing

print(name[0:6])
nameshort = name[0:3] #start from index 0 all the way till 3(excluding 3)
print(nameshort)
character1 = name[0]
print(character1)

print(name[:4]) # is same as [0:4]
print(name[1:]) # is same as [1:6]
print(name[-6:-1]) # is same as [0:6]

#slicing skip value

print(name[0:5:2])
