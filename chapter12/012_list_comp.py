mylist = [1,2,3,4,5,6]

squaredlist = []

for item in mylist:
    squaredlist.append(item*item)
print(squaredlist)

# using list comprehenssions

squaredlist = [i*i for i in mylist]
print(squaredlist)

