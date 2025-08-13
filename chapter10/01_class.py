# class is basically a format or form in which datas are inserted to creat object

class employee:
    language = "py" #this is a class attribute
    salary = 1200000

hari = employee()
hari.name = "hari" # this is a object/instance attribute
print(hari.name,hari.salary,hari.language)

rohan = employee()
rohan.name = "rohan ram"
print(rohan.name,rohan.language,rohan.salary)


# here name is object attribute and language, salary is class attribute as they belong directly to the class.