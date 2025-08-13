class Employee:
    language = "py"
    salary = 1200000

hari = Employee()
hari.name = "hari"
print(hari.name,hari.language,hari.salary)

roshan = Employee()
roshan.name = "roshan"
roshan.language = "java"  # where class attribute is changed with instance attribute.
print(roshan.name,roshan.language,roshan.salary)


