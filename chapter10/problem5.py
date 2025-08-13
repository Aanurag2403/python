# write a class Train which has method to book a ticket , get status(no of seats) and get fare information of train running under Indian Railway.

import random

class Train:

    def __init__(self,trainno):
        self.trainno = trainno

    def book(self,frm,to):
        print(f"train no.{self.trainno} is booked from {frm} to {to}")

    def getstatus(self):
        print(f"train no. {self.trainno} is on time")

    def getfare(self,frm,to):
        print(f"train no. {self.trainno} ticket fare is {random.randint(199,1999)}")


t = Train(12339)
t.book("ASN","HOW")
t.getstatus()
t.getfare("ASN","HOW")