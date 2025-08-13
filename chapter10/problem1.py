# create a class "Programmer" for storing information of few programmers working at microsoft

class Programmer:
    company = "Microsoft"
    
    def __init__(self,name, salary,address):
        self.name = name
        self.salary = salary
        self.address = address

n = Programmer("hari",1300000,"asansol")
print(n.name,n.company,n.salary,n.address)

r = Programmer("rohan",1500000,"kolkata")
print(r.name,r.company,r.salary,r.address)

        