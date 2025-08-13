class Employee:
    language = "py"
    salary = 1200000

    def __init__(self,name,salary,language): # dunder method is automatically called
       self.name = name
       self.salary = salary
       self.language = language
       print("this is an object")
    

    def getinfo(self):
        print(f"the salary is {self.salary} and the language is {self.language}")

    @staticmethod
    def greet():
        print("good morning")

hari = Employee("hari",1200001,"java")
# hari.name = "hari"
print(hari.name,hari.salary,hari.language)