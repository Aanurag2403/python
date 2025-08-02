# write a program to create a dictionary of hindi words with values as thier english translation. Provide users with option to look it up

words = {
    "takiya": "pillow",
    "basta": "bag",
    "kitab": "books",
}

word = input("select word from the following to find its meaning in english:\ntakiya\nbasta\nkitab: ")
print(words[word])