class Reciepe():
    #constructor
    def __init__(self,dish,items,time) -> None:
        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        print("The " + self.dish +" requires ingredients " + str(self.items) + " and take "+ str(self.time) +" minutes")

pizza = Reciepe("Pizza" , ["bread" , "veges" , "paneer"] , 55)
maggi = Reciepe("Maggi" , ["Maggie masala" , "peas"] , 10)

print(pizza.contents())

#O/P : The Pizza requires ingredients ['bread', 'veges', 'paneer'] and take 55 minutes
# None -- The None in the output is coming because the contents() method of the Recipe class doesn't return anything explicitly. In Python, when a function or method does not explicitly return a value, it implicitly returns None
# In this code, the contents() method now returns the recipe information as a string, which you can then print using print(). This way, you won't get the extra None in the output.

print(maggi.contents())
