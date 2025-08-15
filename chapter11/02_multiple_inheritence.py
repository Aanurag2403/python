class Employee:
    company = "ITC"
    name = "default name"
    def show(self):
        print(f"the name of the employee is {self.name} and company is {self.company}")

class coder:
    language = "Python"
    def language(self):
        print(f"out of all the languages here is your language: {self.language}")

class programmer(Employee,coder):
    company="ITC infotech"
    def showlanguage(self):
        print(f"The name is {self.company} and he is good in {self.language} language")

a = Employee()
b = programmer()

b.show()
b.showlanguage()

