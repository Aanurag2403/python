# create a class 'Pets from a class "Animals" and further create a class "Dog" from 'Pets. add a method 'Bark' to class 'Dog'.

class Animal:
    pass
    
class Pet(Animal):
    pass

class Dog(Pet):

    @staticmethod
    def bark():
        print("dog barks")

d = Dog()
d.bark()
