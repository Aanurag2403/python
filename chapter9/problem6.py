#write a program to mine a text2 file and find out whether it contains "python".

with open("text2.txt") as f:
    content = f.read()

if("python" in content):
    print("yes it is present")
else:
    print("it is not present")
