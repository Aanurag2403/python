# write a python function to remove a given word from a list and strip it at the same time.

# n = input("enter your word to remove: ")

def rem(l,word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
l = ["hari","rohan","shubham","an"]
print(rem(l,"an"))