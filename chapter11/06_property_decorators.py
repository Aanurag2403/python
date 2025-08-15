
# incapsulasion : many other worlking components are under one component.
# abstraction  : implemention details are hidden from users.

class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(cls.a)

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
e = Employee()
e.a = 45
e.show()

e.name = "hari ram"
print(e.name)
