import os 

#specify the directory you want to list
directory_path ='/'

#list all files and directory in the specific path
content = os.listdir(directory_path)

#print each files and directory name
for item in content:
    print(item)

#write a program to print the content of directory using the os module?