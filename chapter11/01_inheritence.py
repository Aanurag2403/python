class Employee:            # base/parent class
    company = "ITC"
    def show(self):
        print(f"the name of the employee is {self.name} and the salary is {self.salary}")

# class programmer:                                                                                      
#     company = "ITC infotech"
#     def show(self):
#         print(f"the name of the employee is {self.name} and the salary is {self.salary}")

#     def showlanguage(self):
#         print(f"the name of the employee is {self.name} and the salary is {self.salary}")



# use of inheritance istead of those upper bunch of codes

class programmer(Employee):    # inherited class
    company = "ITC infotech"
    def showlanguage(self):
        print(f"the name of the employee is {self.name} and he is god in {self.language}")

a = Employee()
b= programmer()

print(a.company,b.company)
