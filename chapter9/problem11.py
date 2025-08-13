# write a program to rename a file to "renamed_by_python".txt.

with open("text1.txt") as f:
   content =  f.read()

with open("text1_new.txt","w") as f:
   f.write(content)