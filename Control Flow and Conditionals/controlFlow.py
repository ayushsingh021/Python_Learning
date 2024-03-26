##########   ELSE IF ###############
# val = input("enter your age : ")

# # conditional -- if ,else ,elif( eqival to else if )
# # input (): This function first takes the input from the user and converts it into a string. 
# val = int(val)

# if val >= 18 and val < 45 :
#     print("Your are adult")
# elif val >= 45 and val < 99 :
#     print("You are old")
# else :
#     print("You are kid")

###########   LOOPs  , WHILE , NESTED LOOP ##############
# for loops -- for ... in and for ... else

# frts = ["apple" , "guava", "lol"];
# for x in frts:
#     print(x)


# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     if fruit == "orange":
#         print("I found an orange!")
#         break
# else:
#     print("I didn't find any oranges.")

#     for...else Loop:

# The for...else loop in Python allows you to execute a block of code in the else clause after the loop has completed its iteration. The else block is executed only if the loop completes without encountering a break statement.



# while loops -- while , while .. else(same as for else)
# same as java/javascript
count = 0
while count < 5:
    print("hey bro")
    count+=1


## for in range
# it witll print 6 times form 0 to 5
for i in range(6):
    print("looping ..." , i )

list_1 = [1,2,3,4,5,6,7,8,9]
list_2 = [1,2,3,4,5,6,7,8,9]

import time
start_time = time.time() # timer start
count = 0
# #outer loop
# for i in list_1 :
#     count+=1
#     #inner loop
#     for j in list_2 :
#         count+=1

#outer loop
for i in range(1000000):
    count+=1
    #inner loop
    for j in range(100) :
        count+=1
print(count)  # count will be 90 due to nested loop 9*9 ( N^2) Time Complexity
print('time taken : ' , round(time.time() - start_time ,2));  ## printed whole time required for execution of nested loop

################# break , continue , pass #############
# break and continue works statement are same 
    

#pass
# The pass statement allows you to run through the loop in its entirety and effectively ignore that the if condition has been satisfied.


favorites = ['Creme Brulee', 'Apple Pie', 'Chur', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Chur':
        pass
    print('Other desserts I like are', dessert) 

#  o/p -- pass ignores that the if statement is valid
    
# Other desserts I like are Creme Brulee
# Other desserts I like are Apple Pie
# Other desserts I like are Chur
# Other desserts I like are Tiramisú
# Other desserts I like are Chocolate Cake



