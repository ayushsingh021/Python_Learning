
#scoping 
def d():
    animal = "elephant"
    def e():
        nonlocal animal
        animal = "giraffe"
        print("Inside nested func : "  + animal)
    
    print("Before calling fnc : "+ animal)
    e()
    print("After calling fnc : " + animal)


animal = "camel"
d()
print("Global animal : " + animal)