# class A:
#    a = 1

# class B(A):
#    a = 2

# class C(B):
#    pass

# c = C()
# print(c.a)

#tells what type of inheritence it is 
# print(C.mro())
# print(help(c)) #tels in detail


# class A:
#     def c(self):
#         return "Function inside A"

# class B:
#     def c(self):
#         return "Function inside B"

# class C(A, B):
#     def c(self):
#         return "Function inside C"

# class D(A, C):
#     pass

# d = D()
# print(d.a)

# Note that this throws an error. In the code above, class D inherits from both class A and class C.

# Class C is its immediate superclass, but since this is multiple inheritance, the rules are more complicated and it also has to check the classes passed to it for precedence.

# In this particular case, class D is unable to resolve the order that should be followed, while resolving the value for the variable in cases where the variable is not present in the class of the given object.

# It results in a TypeError because it's unable to create method resolution order (MRO). MRO is Python’s way of resolving the order of precedence of classes while dealing with inheritance.


class A:
    def d(self):
        return "Function inside A"

class B:
    def d(self):
        return "Function inside B"


class C:
    def d(self):
        return "Function inside C"


class D(A, B):
    def d(self):
        return "Function inside D"


class E(B, C):
    def d(self):
        return "Function inside E"


class F(E,D,C):
    pass

f = F()
print(f.d())
print(F.mro())