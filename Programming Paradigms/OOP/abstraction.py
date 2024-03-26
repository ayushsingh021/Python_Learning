# Abstraction can be seen both as a means for hiding important information as well as unnecessary information in a block of code. The core of abstraction in Python is the implementation of something called abstract classes and methods, which can be implemented by inheriting from something called the abc module. "abc" here stands for abstract base class. It is first imported and then used as a parent class for some class that becomes an abstract class. Its simplest implementation can be done as below.


from abc import ABC,   
class ClassName(ABC):
    pass