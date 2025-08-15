# create a class "Employee" and add salary and increment poperties to it. 
#  write a method 'salaryafterincrement' with a @property decorator with a setter which changes the value of increment based on the salary.

class Employees:
    salary =12000
    increment = 10
    
    @property
    def salaryafterincrement(self):
        return(self.salary+self.salary*(self.increment/100))
    
    @salaryafterincrement.setter
    def salaryafterincrement(self,salary):
        self.increment =((salary/self.salary)+1)*100

    @classmethod
    def show(cls):
        print(cls.increment)
       

e = Employees()
print(e.salaryafterincrement)

e.salaryafterincrement = 30000
print(e.increment)
e.show()



    