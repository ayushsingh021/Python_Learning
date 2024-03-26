
# Polymorphism refers to something that can have many forms. In this case, a given object.
# Remember that everything in Python is inherently an object, so when I talk about polymorphism, it can be an operator, method or any object of some class. 
# I can illustrate the case for polymorphism using built-in functions and operations, for example:

string = "poly"
num = 7
sequence = [1,2,3]
new_str = string * 3
new_num = 7 * 3
new_sequence = sequence * 3

print(new_str, new_num, new_sequence)


string = "poly"
sequence = [1,2,3]
print(len(string))
print(len(sequence))

# The len() function is able to take variable inputs. In the example above it is a string and a list that provides the output in integer format.