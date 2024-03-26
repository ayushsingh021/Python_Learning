# ## in python there is majorly,
# A data structure allows you to organize and arrange your data to perform operations on them. Python has the following built-in data structures: List, dictionary, tuple and set. These are all considered non-primitive data structures, meaning they are classed as objects, this will be explored later in the course. 
# Along with the built-in data structures, Python allows users to create their own. Data structures such as Stacks, Queues and Trees can all be created by the user. 
# Each data structure can be designed to solve a particular problem or optimize a current solution to make it much more performant.

# Mutability refers to data inside the data structure that can be modified. For example, you can either change, update, or delete the data when needed. A list is an example of a mutable data structure. The opposite of mutable is immutable. An immutable data structure will not allow modification once the data has been set. 

######  LIST ############

list1 = [1,2,3,4,5] ## list of int
list2 = ['A' , 'B' ,'C' , 'D' ,'E'] # list of char / string
list3 = ["hello" , 1, 'a' , 3.14] # list of different data types

# accesing values from list
print(list1[2])

list4 = [1,2,[4,56,6] , 6]  # nested list
print(list4[2])

# adding value at the last idx of the list1
list1.insert(len(list1) , 14)
list1.append(15) # works same as prev one
list1.extend([4,3,2]) # addes from the last 

# remove
list1.pop(1) # give the index of the listval which will be removed
del list1[0]  # works same as above

# same as map function
for val in list3:
    print("Value is : ",val)

print (list1 , sep =" ")



# list is mutable ( changable )and tuple is immutable( not changable values )
########## TUPLES ###############

my_tuple = (1, "hello" , 4.5 , True)

# my_tuple[0] = 5 # gives error
print(my_tuple[2])
print(my_tuple.index(4.5)) # gives index


###############  SET  #############
# same as set in java stores and give unique values
set_a = {1,2,3,4,5,5}   #-- o/p {1, 2, 3, 4, 5}

set_a.add(40) # adding values
set_a.remove(2) # give the value to be removed

print(set_a)

setA= {1,2,3,4,5}
setB = {4,5,6,7,8}

print(setA.union(setB)) # makes a single list with taking unique values fro both the sets
print(setA | setB) #works same as above

print(setA.intersection(setB)) #gives common values form both the sets
print(setA & setB) #works same as above

print(setA.difference(setB)) #gives values of setA that are in setA but not in setB
print(setA - setB) #works same as above

print(setA.symmetric_difference(setB)) # all the elements that are in setA and setB but not in both
print(setA ^ setB) #works same as above

# print(setA[0]); cant access values like this in sets which was possible for list and tuple cause it does not values in orderly manner 
for val in setB:
    print("setB :" ,val)



############## DICTIONARY ########### JUST LIKE HASHMAP

# it is a key val pair just like a dictionary but keys should be unique always just like hahsmap

# both way works
sample_dict = {1 : 'Ayush' , 2 : "Govind" , 3: "Niraj"}
print(sample_dict[2]) # giving key to get the value from dictionary
sample_dict[2] = "Raj" # changing value of key 2

del sample_dict[3] # deleting values

print(sample_dict[2])

sample_dict = {'a' : 'Ayush' , 2 : "Govind" , 3: "Niraj"}
print(sample_dict['a']) # giving key to get the value from dictionary

#  Iterating in a dictionary --  3 methods ( Standard  , items() , Values()  )

dict = {1 : '01' , 'name' : "Ayush" }
dict['lastName'] = "Singh" #adding key val pair in dictionary

print(dict)

# items() --- iteration in dictionary
for key,val in dict.items():
    print(str(key) , " : ", val)