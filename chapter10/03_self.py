class Employee:
    language = "py"
    salary = 1200000

    def getinfo(self):
        print(f"the lnguage is {self.language}. The salary is{self.salary}")


    
    @staticmethod     # static method helps to avoid object intereference in a function.
    def greet():
        print("good morning")
hari = Employee()
hari.getinfo()
hari.greet()