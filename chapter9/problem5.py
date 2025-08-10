# repeat  program 4 for a list of such words to be censored

words = ["donkey","bad","ganda"]

with open("text1.txt","r") as f:
    content = f.read()

for word in words:
    content = content.replace(word,"#" * len(word))

with open("text1.txt","w") as f:
    f.write(content)