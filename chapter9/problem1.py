#write a program to read the text from givden file 'poem.txt' and find out whether it contains the word 'twinkle'.

f = open('poem.txt')
data = f.read()
if ("twinkle" in data):
    print("twinkle word is in the content")
else:
    print("this content doesnot contain the word twinkle") 
f.close()