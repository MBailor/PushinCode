# Abstraction Assignment
#
# Mark Bailor
#
#
# Python 3.8.3

from abc import ABC, abstractmethod
class car(ABC):
    
    def monthly(self, amount):
        print("Your Monthly Balance Due is: ",amount)

    @abstractmethod
    def payment(self, amount):
        pass

class DebitCardPayment(car):

    def payment(self, amount):
        print('Thank You For Your Payment of {} '.format(amount))

    def balance(self, amount):
        print("Your Remaning Balance is {} ".format(amount))

obj = DebitCardPayment()
obj.monthly("$250")
obj.payment("$400")
obj.balance("$4879.34")
    
