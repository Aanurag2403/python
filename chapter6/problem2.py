# write a program to find whether a student has passed or failed if it requires a total of 40% and atleast 33% in each subject to pass. Assume 3 subk=jects and take marks as input from user.

m1 = int(input("enter first subject marks: "))
m2 = int(input("enter second subject marks: "))
m3 = int(input("enter third subject marks: "))

t = ((m1+m2+m3)/3)

if(t>=40 and m1>=33 and m2>=33 and m3>=33):
    print("you are pass",t)

else:
    print("failed",t)

