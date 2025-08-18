#  way to merge dictionary
 
dict1 = {'a':1,'b':2}
dict2 = {'b':3,'c':4}
merged = dict1 | dict2

print(merged)

# we can process different files using 'with statement'
'''
with (
    open('file.py') as f1,
    open('file.py') as f2
):
 print(f1.read())

 
'''