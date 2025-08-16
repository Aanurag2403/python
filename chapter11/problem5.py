# write a class vector representing a vector of n dimensions. overload the + and * operator which calculates the sum and the dot(.) product of them.

class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self,other):
        result = Vector(self.x+other.x , self.y +other.y , self.z + other.z)
        return result
    
    def __mul__(self,other):
        return self.x * other.x + self.y *other.y +self.z *other.z
    
    def __str__(self):
        return(f"Vector({self.x},{self.y},{self.z})")


a1 =Vector(1,2,3)
a2 = Vector(4,5,6)
a3 = Vector(7,8,9)

print(a1+a2)
print(a1*a2)

print(a1+a3)
print(a1*a3)