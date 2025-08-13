# write a progeram to make a copy of a text file "text1.txt"

with open("text1.txt") as f:
    content = f.read()

with open("text1_copy.txt","w") as f:
    f.write(content)