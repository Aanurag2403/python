class Employee:
    a = 1  # this variable wil be considered

    @classmethod   # using @classmethod will make no change in class attribute and it will be as same.
    def show(cls):
        print(cls.a)  

e =Employee()
e.a = 45

e.show()