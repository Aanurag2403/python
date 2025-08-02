s = {1,5,32,54,5,5,"harry"}
print(s, type(s))

# add
s.add(566)
print(s)

#length
d = len(s)
print(d)

#remove
s.remove(1)
print(s)

#pop
s.pop()
print(s)

#union
s1 = {1,23,43,45}
s2 = {2,23,46,45}

print(s1.union(s2))

#intersection
print(s1.intersection(s2))