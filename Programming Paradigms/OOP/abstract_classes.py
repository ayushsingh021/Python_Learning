#import ABC
# from abc import ABC, abstractmethod

# #creating inheritig class
# class SomeAbstractClass(ABC):

#     #import abstract method
#     @abstractmethod
#     def someabstractmethod(self):
#         pass

#import abc and method
from abc import ABC, abstractmethod

# Define ABC method
class Employee(ABC):
    @abstractmethod
    def donate(self):
        pass

# create subclass
class Donation(Employee):

    # implementation
    def donate(self):
        a = input('How much you want to donate : ')
        return a
    

# class instances

amounts = []
john = Donation()
j = john.donate() #sroting donation amt from john 
amounts.append(j)

peter = Donation()
p = peter.donate()  #storing donation amt from peter
amounts.append(p)

print(amounts)
