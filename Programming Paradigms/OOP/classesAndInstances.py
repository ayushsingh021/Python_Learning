# Everything in python is an object or derived from the object class

#class defintition
class MyClass:
    a = 5

    def greet(self):
        print("Hello Guyzz!!")
   

#instances
newObj = MyClass()
print(newObj.a)
print(newObj.greet())


#definitipn
class Car:
    #constructor
    def __init__(self, model, color):
        self.model = model
        self.color = color

# Main function
def main():
    maruti = Car(22, "Blue")
    print(maruti.color)

if __name__ == "__main__":
    main()
    


class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    num_rooms = 5
    bathrooms = 2
    def cost_evaluation(self):
        print(self.num_rooms)
        pass
        # Functionality to calculate the costs from the area of the house
    # . This is then followed by a function definition, which is empty except for the pass keyword that basically signals Python to continue execution without throwing an error.