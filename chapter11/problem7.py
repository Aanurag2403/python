# Override the __len__() method on vecor of problem5 to deisplay the dimension of the vector.

class Vector:
    def __init__(self,l):
        # self.x = x
        # self.y = y
        # self.z = z
        self.l = l

    def __add__(self,other):
        result = Vector(self.x+other.x , self.y +other.y , self.z + other.z)
        return result
    
    def __mul__(self,other):
        return self.x * other.x + self.y *other.y +self.z *other.z
    
    def __str__(self):
        return(f"Vector({self.x},{self.y},{self.z})")
    
    def __len__(self):
        return (len(self.l))

a1 =Vector([1,2,3])
print(len(a1))