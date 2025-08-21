# write a program to input name, marks and phone no. of the student and format it using function like below
#  "The name of the student is hari,his matrks are 72 and phone no. is 999924432"

name = input("enter name: ")
marks = int(input("enter your marks: "))
phone = int(input("enter number: "))


s = "The name of the student is {}, his marks are {} and phone no. is {}".format(name,marks,phone)
print(s)