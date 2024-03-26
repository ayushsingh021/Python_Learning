#read / readline / readlines

with open ('sample.txt' ,mode = 'r') as file:
    print(file.read())

with open ('sample.txt' ,mode = 'r') as file:
    print(file.read(10))

#readline -- return single line 
# The Readlines method reads the entire contents of the file and then returns it in an ordered list. This is useful because it allows you to iterate over the list or pick out specific lines based on a condition.
    
# with open('sample.txt' , mode = 'r') as file:
#     for x in file:
#         print(x)

# Additionally, I can get the f_content variable into a list. The string "\n" is used to split the text where a new line is found.
# f_content_list = f_content.split("\n")

import random

try:
    with open("petnames.txt", mode="r") as f:
        f_content = f.read().strip()  # Strip removes leading/trailing whitespaces
        if f_content:
            f_content_list = f_content.split("\n")
            print(f_content)  # Check if file content is read correctly
            print(random.choice(f_content_list))
        else:
            print("File is empty.")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("Error occurred:", e)

        
