# write__str__() method to pint the vector as follows:
# 7i+8j+10k


class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self,other):
        return (Vector(self.x + other.x,self.y + other.y , self.z + other.z))
    
    def __mul__(self,other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}"
    
a1 = Vector(1,2,3)
a2 = Vector(4,5,6)
a3 = Vector(7,8,9)

print(a1+a2)
print(a1*a2)

print(a1+a3)
print(a1*a3)
