###### MAP ##########
menu = ["espresso" , 'matta' , "latte" , "capacino" , "americana", 'calee']

# map(<Function> , var on which function works ) -- takes two args

# Map takes all objects in a list and applies a function
# Filter do the same but take the results and creates a new list with only true values 

# map() returns every item in an iterable and filter() returns values if True.


def find_coffee(menuitems):
    if menuitems[0] == 'c':
        return menuitems

mapped_menu = map(find_coffee , menu)

for val in mapped_menu:
    print(val)


filtered_menu = filter(find_coffee,menu)

for val in filtered_menu:
    print(val)