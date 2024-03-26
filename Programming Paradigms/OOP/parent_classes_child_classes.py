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