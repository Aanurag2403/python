# add a static method in problem2 to print done to the user.


class calculator:

    @staticmethod
    def greet():
        print("done")

    def __init__(self,num):
        self.num = num
        print(f"square is: {num*num}, cube is: {num*num*num}, and square root is : {num**1/2}")

c = calculator(2)
c.greet()

        