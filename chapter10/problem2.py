# write a class "calculator" capable of finding square, cube and square root of a number.

class calculator:
    def __init__(self,num):
        self.num = num
        print(f"square is: {num*num}, cube is: {num*num*num}, and square root is : {num**1/2}")

c = calculator(2)
        