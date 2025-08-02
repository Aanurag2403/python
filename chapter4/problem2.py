#write a program to accept marks of 6 students and display them in asorted manner

marks = []
s1 = int(input("enter your marks"))
marks.append(s1)
s2 = int(input("enter your marks"))
marks.append(s2)
s3 = int(input("enter your marks"))
marks.append(s3)
s4 = int(input("enter your marks"))
marks.append(s4)
s5 = int(input("enter your marks"))
marks.append(s5)
s6 = int(input("enter your marks"))
marks.append(s6)

marks.sort()
print(marks)

