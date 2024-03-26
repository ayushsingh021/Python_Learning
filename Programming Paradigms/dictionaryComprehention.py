# Dictionary comprehension
# The syntax for dictionary comprehension is:

# dict = { key:value for key, value in <sequence> if <condition> } 
# Dictionary comprehension takes one or two lists as input and creates a dictionary out of it

# Using range() function and no input list
usingrange = {x:x*2 for x in range(12)}
print("Using range(): ",usingrange)

# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# Using one input list
numdict = {x:x**2 for x in number}
print("Using one input list to create dict: ", numdict)

# Using two input lists -- zip(sticks to list values)
# new_dict ={key:value for (key, value) in zip(list1, list2)}
# Here I used the zip function that combines the two lists. When the two lists are of unequal length, the length of the shorter list is the length of the dictionary.
months_dict = {key:value for (key, value) in zip(number, months)}
print("Using two lists: ", months_dict)