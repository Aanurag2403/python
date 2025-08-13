# write a program to find out where a file is identical & matches the content of another file.

with open("text1.txt") as f:
    content1 = f.read()
with open("text1_copy.txt") as f:
    content2 = f.read()

if (content1 == content2):
    print("yes these files are identical")
else:
    print("no this are not identical")