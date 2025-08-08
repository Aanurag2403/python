#how to read line by line all at one time

f = open("file.txt")

lines = f.readlines()
print(lines, type(lines))
f.close()
# how to read line by line 

f = open("file.txt")

line1 = f.readline()
print(line1, type(line1))

line2 = f.readline()
print(line2,type(line2))

line3 = f.readline()
print(line3,type(line3))

f.close()
