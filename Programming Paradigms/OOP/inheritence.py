# inheritence  -- creating a new class from a exidting one -- parent child relationship

# polymorphism -- ability of a function to change its behavior when called by different object
#eg -- '+' -- a built in plus operator adds integer values and concatenates string

# Encapsulation -- Limits access to method and variableby encasing them in a single unit of scope

# Abstraction  -- hides implementation details for data security


class Parent:
    Members of the parent class

class Child(Parent):
    Inherited members from parent class
    Additional members of the child class
        
# Python adheres to something called the Method Resolution Order (MRO) that determines the flow of execution.
# MRO is a set of rules, or an algorithm, that Python uses to implement monotonicity, which refers to the order or sequence in which the interpreter will look for the variables and functions to implement.

################################################################################
# Single inheritence -- where the child inherits from a single parent
 #parent class
class P:
    def __init__(self) -> None:
        self.a = 7

#empty child class
class C(P):
    pass
#instance
obj = C()
#we can see the child class is empty but still it inherits the properties of parent class
print(obj.a)



################################################################################


#Multiple Inheritence -- one chaild class inherits from multiple parents
# Example 1
class A:
   a = 1
   
class B:
   b = 2
   
class C(A, B):
   pass

c = C()
print(c.a, c.b)

################################################################################

# Multi-level inheritance -- its like recurrsion

class A:
   a = 1

class B(A):
   a = 2

class C(B):
   pass

c = C()
print(c.a)

# There are two built-in functions that can come in handy when trying to find the relationship between different classes and objects: issubclass() and isinstance().

################################################################################
# Hiearchial Inheritence -- where multiple child inherits from a common class


################################################################################
#Hybrid Inheritence - where its mixture of the inheritence of others