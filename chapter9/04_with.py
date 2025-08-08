f = open("file.txt")
print(f.read)
f.close()

# same thing can be done with 'with' statement :

with open("file.txt") as f:
    print(f.read())
