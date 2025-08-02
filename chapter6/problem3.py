# A spam comment is defined as atext containing following keyword:
#"Make a lot of money","but now","subscribe this","click this",write a program to detect thse spams.

p1 = "Make a lot of money"
p2  ="but now"
p3 = "subscribe this"
p4 = "click this"

message = input("enter your comment: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("this is a spam message")
else:
    print("their is no spame message")