class Employee:
    def __init__(self):
        print("constructor of Employee")
    a=1
class programmer(Employee):
    def __init__(self):
        print("constructor of programmer")
    b=2
class Manager(programmer):
    def __init__(self):
        super().__init__()  # super constructor will make sure that parent constructor should also work.
        print("constructor of Manager")
    c=3

# o = Employee()
# print(o.a)

# o = programmer()
# print(o.a, o.b)

o = Manager()
print(o.a,o.b,o.c)