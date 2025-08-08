# a file contains a word "Donkey" multiple times you need to write a program w hich eplace this word with #### by updating the same file.


with open("text1.txt","r") as f:
    content = f.read()

newcontent = content.replace("Donkey","####")
newcontent += "\nprevious line was Donkey is nice Donkey but not a bad Donkey."

with open("text1.txt","w") as f:
   
    f.write(newcontent)

