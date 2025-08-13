# write a program to find out where python word is present in text2.txt file

lineno = 1
with open("text2.txt") as f:
    content = f.readline()

for line in content:
    if("python" in content):
      print(f"yes it is present in line no.: {lineno}")
      break
    lineno += 1
else:
    print("no it is not there")
