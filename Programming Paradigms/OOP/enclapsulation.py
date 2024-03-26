# . The use of single and double underscores for this purpose in Python is a substitute for this practice. For example, let's examine an example of protected members in Python.

class Alpha:

def __init__(self):
    self._a = 2.  # Protected member ‘a’
    self.__b = 2.  # Private member ‘b’

# self._a is a protected member and can be accessed by the class and its subclasses.
# Private members in Python are conventionally used with preceding double underscores: __. self.__b is a private member of the class Alpha and can only be accessed from within the class Alpha.

# Name Mangling    
# It should be noted that these private and protected members can still be accessed from outside of the class by using public methods to access them or by a practice known as name mangling. Name mangling is the use of two leading underscores and one trailing underscore, for example:
# _class__identifier -- syntax

# Class is the name of the class and identifier is the data member that I want to access.
    